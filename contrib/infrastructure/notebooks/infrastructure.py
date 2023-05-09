import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import config
import os
import glob

load_dotenv('.env')
os.environ['PROJ_LIB'] = '/opt/conda/share/proj'


def check_countries(countries):
	'''
	Parameters
	----------
	countries : list
	List of iso-2 country codes, use 'all' for all countries
	'''

	if not isinstance(countries, list):
		raise TypeError(f'List of countries is needed, not {type(countries)}')

	# create list if all countries are requested
	if 'all' in countries:
		countries = ['no', 'nl', 'uk', 'be', 'dk', 'de']
	else:
		pass

	return countries

def create_dataframes(cols, table, country, eez):
	'''
	Generic function for creating
	and cleaning a dataframe
	
	Parameters
	----------
	cols : list
		List of columns to filter and rename
	table : string
		Name of the table in PostgreSQL
	country : string
		Country to be queried in PostgreSQL
	eez : bool
		If set to True get all features in the North Sea EEZ's
		If set to False get all features within the official North Sea boundaries
	'''
	#print(f'\nImporting from {country}, table: {table}')
	# create connection
	engine = create_engine(os.environ.get('POSTGRES_DB'), connect_args={'options': '-csearch_path={}'.format('public')})
	connection = engine.connect()
	
	# set standard coordinate reference system for spatial data
	CRS = 25831 # UTM crs that is pretty accurate for North Sea area

	# import company data TODO: add to PostgreSQL
	_com = pd.read_sql(text('SELECT * FROM companies'), connection)
	_eez = gpd.GeoDataFrame.from_postgis(text('SELECT * FROM boundaries_eez'), connection, geom_col='geometry').to_crs(CRS)
	_eez.territory1 = _eez.territory1.map({'Denmark': 'dk', 
										 'Germany': 'de', 
										 'Belgium': 'be',
										 'Norway': 'no',
										 'Netherlands': 'nl',
										 'United Kingdom': 'uk'})
	_northsea = gpd.GeoDataFrame.from_postgis(text('SELECT * FROM boundaries_northsea'), connection, geom_col='geometry').to_crs(CRS)

	# Create generic SQL
	SQL = f'SELECT {", ".join(cols.keys())} FROM {table}'

	df = gpd.GeoDataFrame.from_postgis(text(SQL), connection, geom_col='geometry')
	#print(f'Imported {len(df)} rows from {table}...')

	# get subset of EMODnet data for each country
	if country in ['be', 'de', 'dk']:
		df.country = df.country.map({'Denmark': 'dk', 'Germany': 'de', 'Belgium': 'be'})
		df = df[df.country==country].copy()
		df = df.drop(['country'], axis=1)

	# clean
	df.columns = df.columns.map(cols)
	df['country'] = country
	df['status_normalised'] = df['status'].map(config.infra_status).fillna(df.status)
	if not 'infra_type' in df.columns:
		df['infra_type'] = 'Pipeline'
	else:
		df['type_normalised'] = df['infra_type'].map(config.infra_types).fillna(df.infra_type)

	df = df.drop_duplicates(subset=['feature_id', 'country', 'infra_name']).copy()

	# set right CRS
	if df.crs is None:
		df = df.set_crs(CRS)
	else:
		df = df.to_crs(CRS)

	# clip
	if eez == False:
		df = gpd.clip(df, _northsea)
	else:
		_eez = _eez[_eez.territory1==country].copy()
		df = gpd.clip(df, _eez)


	# merge with company names
	df.operator = df.operator.str.upper().str.strip()
	_com.name_db = _com.name_db.str.upper().str.strip()
	df = pd.merge(df, 
				  _com[['name_db', 'name_local', 'name_international', 'country_international']], # TODO: Import company names
				  left_on = 'operator',
				  right_on = 'name_db',
				  how='left').reset_index().drop('index', axis=1).rename(columns={'name_international': 'name_normalised',
				  																  'country_international': 'country_operator'})
	
	#print(f'Company merge: {len(df[df.name_international.isna()])} rows could not be merged...')
	print(f'Imported {len(df)} rows from {country}: {table}')
	
	return df

def get_platforms(countries, only_platforms=False, eez=False):
	
	'''Imports all pipelines
	from PostgreSQL
	Parameters
	----------
	countries : list
		List of countries
	only_platform : bool
		True for only platforms
	eez : bool
		If set to True get all features in the North Sea EEZ's
		If set to False get all features within the official North Sea boundaries
	'''
	dfs = []
	
	for country in check_countries(countries):

		if country.lower() == 'uk':
			table = 'uk_infrastructure_points'
			cols = config.infra_cols_uk
		elif country.lower() == 'nl':
			table = 'nl_facility'
			cols = config.infra_cols_nl
		elif country.lower() == 'no':
			table = 'no_facility'
			cols = config.infra_cols_no
		else:
			table = 'int_platforms'
			cols = config.infra_cols_int

		df = create_dataframes(cols, table, country, eez)

		dfs.append(df)    
	
	df = pd.concat(dfs).drop_duplicates()

	if only_platforms == True:
		df = df[df.type_normalised == 'Platform'].copy()
		#print('Filtering out platforms...')
	else:
		pass

	return df

def get_pipelines(countries, eez=False):

	'''Imports all pipelines
	from PostgreSQL
	Parameters
	----------
	countries : list
		List of countries
	eez : bool
		If set to True get all features in the North Sea EEZ's
		If set to False get all features within the official North Sea boundaries
	'''
	
	dfs = []
	
	for country in check_countries(countries):

		if country.lower() == 'uk':
			table = 'uk_pipelines_linear'
			cols = config.pipes_cols_uk
		elif country.lower() == 'nl':
			table = 'nl_pipelines'
			cols = config.pipes_cols_nl
		elif country.lower() == 'no':
			table = 'no_pipeline_thin'
			cols = config.pipes_cols_no
		else:
			table = 'int_pipelines'
			cols = config.pipes_cols_int

		df = create_dataframes(cols, table, country, eez)

		dfs.append(df)    
	
	df = pd.concat(dfs).drop_duplicates()

	return df

def get_wellbores(countries, eez=False):

	'''Imports all wellbores
	from PostgreSQLS
	Parameters
	----------
	countries : list
		List of countries
	eez : bool
		If set to True get all features in the North Sea EEZ's
		If set to False get all features within the official North Sea boundaries
	'''

	dfs = []
	
	for country in check_countries(countries):

		if country.lower() == 'uk':
			table = 'uk_wells'
			cols = config.wells_cols_uk
		elif country.lower() == 'nl':
			table = 'nl_wellbores'
			cols = config.wells_cols_nl
		elif country.lower() == 'no':
			table = 'no_wellbore'
			cols = config.wells_cols_no
		else:
			table = 'int_wellbores' # TODO: structually import wellbores
			cols = config.wells_cols_int

		df = create_dataframes(cols, table, country, eez)


		dfs.append(df)    
	
	df = pd.concat(dfs).drop_duplicates()

	return df
