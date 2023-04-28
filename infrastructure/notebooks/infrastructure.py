import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import ontology
import os

load_dotenv('.env')
os.environ['PROJ_LIB'] = '/opt/conda/share/proj'


class Infrastructure:

	'''
	Class with subclasses for importing raw datasets of 
	north sea platforms (and infrastructure), pipelines
	and wellbores and returns a clean dataframe.
	For cleaning the ontology module is used (and can be adapted)
	
	Parameters
	----------
	countries : list
		List of iso-2 country codes, use 'all' for all countries
	'''

	def __init__(self, countries):
		self.countries = countries

		# check if countries parameter is a list
		if not isinstance(self.countries, list):
			raise TypeError(f'List of countries is needed, not {type(self.countries)}')

		# create list if all countries are requested
		if 'all' in self.countries:
			self.countries = ['no', 'nl', 'uk', 'be', 'dk', 'de']

		# create connection
		engine = create_engine(os.environ.get('POSTGRES_DB'))
		connection = engine.connect()
		print('Establishing connection...')

		# set standard coordinate reference system for spatial data
		CRS = 25831 # UTM crs that is pretty accurate for North Sea area

		# import company data TODO: add to PostgreSQL
		_com = pd.read_sql(text('SELECT * FROM company_names'), connection)

	def create_dataframes(cols, table):
		'''
		Generic function for creating
		and cleaning a dataframe
		
		Parameters
		----------
		cols : list
			List of columns to filter and rename
		table : string
			Name of the table in PostgreSQL
		'''

		# Create generic SQL
		SQL = f'SELECT {cols.keys()} FROM \"{table}"'

		df = gpd.read_file(SQL, connection, geom_col='geometry')
		print(f'Imported {len(df)} rows from {table}...')

		# clean
		df.columns = df.columns.map(cols)
		df['status_normalised'] = df['status'].map(ontology.infra_status).fillna(infra.status)
		df['type_normalised'] = df['infra_type'].map(ontology.infra_type).fillna(infra.infra_type)
		
		# get subset of EMODnet data for each country
		if country in ['be', 'de', 'dk']:
			df.country = df.country.map({'Denmark': 'dk', 'Germany': 'de', 'Belgium': 'be'})
			df = df[df.country==country].copy()
			df = df.drop(['country'], axis=1)

		# set right CRS
		if df.crs is None:
			df = df.set_crs(CRS)
		else:
			df = df.to_crs(CRS)

		print('Merge with company names...')

		# merge with company names
		df = pd.merge(df, 
					  _com[['name_db', 'name_international']], # TODO: Import company names
					  left_on = 'operator',
					  right_on = 'name_db',
					  how='left')
		
		print(f'{len(df[df.name_international.isna()])} rows could not be merged...')
		
		return df

	def get_platforms(self, only_platform=False):
		'''
		Imports all platforms from
		PostgreSQL instance
		'''

		dfs = []
		
		for country in countries:

			if country.lower() == 'uk':
				table = 'uk_infrastructure_points'
				cols = ontology.infra_cols_uk
			elif country.lower() == 'nl':
				table = 'nl_facility'
				cols = ontology.infra_cols_nl
			elif country.lower() == 'no':
				table = 'no_facility'
				cols = ontology.infra_cols_no
			else:
				table = 'int_platforms'
				cols = ontology.infra_cols_int

			df = create_dataframes(cols, table)

			dfs.append(df)    
		
		df = pd.concat(dfs).drop_duplicates()

		if only_platforms == True:
			df = df[df.type_normalised == 'Platform'].copy()
			print('Filtering out platforms...')
		else:
			pass

		return df

	def get_pipelines(self):
		
		dfs = []
		
		for country in self.countries:

			if country.lower() == 'uk':
				table = ['uk_pipelines_linear']
				cols = ontology.pipes_cols_uk
			elif country.lower() == 'nl':
				table = 'nl_pipelines'
				cols = ontology.pipes_cols_nl
			elif country.lower() == 'no':
				table = 'no_pipeline_thin'
				cols = ontology.pipes_cols_no
			else:
				table = 'int_pipelines'
				cols = ontology.pipes_cols_int

			df = create_dataframes(cols, table)

			dfs.append(df)    
		
		df = pd.concat(dfs).drop_duplicates()

		return df

	def get_wellbores(self):

		dfs = []
		
		for country in self.countries:

			if country.lower() == 'uk':
				table = ['uk_wells']
				cols = ontology.wells_cols_uk
			elif country.lower() == 'nl':
				table = 'nl_wellbores'
				cols = ontology.wells_cols_nl
			elif country.lower() == 'no':
				table = 'no_wellbore'
				cols = ontology.wells_cols_no
			else:
				table = 'int_wellbores' # TODO: structually import wellbores
				cols = ontology.wells_cols_int

			df = create_dataframes(cols, table)

			if country.lower() == 'nl':
				df = df[df.status.dropna()].copy()

			dfs.append(df)    
		
		df = pd.concat(dfs).drop_duplicates()

		return df
	