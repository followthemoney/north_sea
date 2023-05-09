'''
Purpose: create a module with classes:
- General functions (Northsea)
	- change CRS
	- check stuff
	- update_data
- Infrastructure:
	- get_platforms
	- get_pipelines
	- get_infrastructure
	- get_wellbores
	- get_turbines
	- get_grid
	- get_telecom
- Energy
	- get_production
- Spatial
	- get_blocks
	- get_quadrants
	- get_eez
'''

import geopandas as gpd
import logging
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import config
import os
import glob

load_dotenv('.env')
os.environ['PROJ_LIB'] = '/opt/conda/share/proj'


# General functions

def check_countries(countries):
	'''
	Parameters
	----------
	countries : list
	List of iso-2 country codes, 
	use 'all' for all countries
	'''

	if not isinstance(countries, list):
		raise TypeError(f'List of countries is needed, not {type(countries)}')

	# create list if all countries are requested
	if 'all' in countries:
		countries = ['no', 'nl', 'uk', 'be', 'dk', 'de']
	else:
		pass

	return countries


def get_wfs_layers(url):
    '''
    Get list of available layers
    and their index
    '''
    
    wfs = WebFeatureService(url, version='2.0.0')
    
    for i, layer in enumerate(wfs.contents):
        print(i, layer)


def check_crs(gdf):
	'''Takes a geodataframe and
	checks if CRS is set.
	Parameters:
	-----------
	gdf : geodataframe
		Geodataframe to check
	'''

	if not gdf.crs:
		raise ValueError('CRS is not set. Please set the CRS parameter')

	return logging.info(f'CRS is set to {gdf.crs}')


def select_wfs_layer(url, index):
    '''
    Select a wfs layer by index
    '''
    wfs = WebFeatureService(url, version='2.0.0')
    layer = list(wfs.contents)[index]
    
    return layer


def wfs2gdf(layer, url, output_format, wfs_version="2.0.0"):
    '''
    Needs layer, wfs_url and output_format
    as input and creates a geodataframe
    '''
    
    params = dict(service='WFS', 
                  version=wfs_version, 
                  request='GetFeature', 
                  typeName=layer, 
                  outputFormat=output_format)
    
    if 'xml' in output_format:
        with BytesCollection(requests.get(url, params=params).content) as f:
            gdf = gpd.GeoDataFrame.from_features(f)
    
    elif 'json' in output_format:
            r = requests.get(url, params=params)
            gdf = gpd.read_file(r.text)
        
    return gdf


def update_fossil_fuel_data(countries):

	for country in check_countries(countries):

		if not os.path.exists(f'../data/{country}'):
	   		os.makedirs(f'../data/{country}')

		if country == 'no' or country == 'uk':
			# Write geopackage to file
			r = requests.get(config.get(country))
			z = zipfile.ZipFile(io.BytesIO(r.content))
			z.extractall(f'../data/{country}/')

		

		if country == 'nl':
			pipes = wfs2gdf(select_wfs_layer(config.fossil_fuel_urls.get('nl').get('infra'), 2), url, 'json')

	# Import layers
	file = '../data/NO/NPD_FactMapsData_v3_0.gdb/'
	layers = fiona.listlayers(file)

	# Write to postgis/postgres
	for layer in layers:
		gdf = pd.read_file(file, layer=layer)
		gdf.crs = "EPSG:23032"
	    gdf.columns = gdf.columns.str.lower()
	    try:
	        gdf.to_postgis(f'no_{layer.lower()}', POSTGIS_ENGINE, if_exists='append', index=False)
	    except ValueError:
	        gdf = pd.DataFrame(gdf)
	        gdf.to_sql(f'no_{layer.lower()}', POSTGIS_ENGINE, if_exists='append', index=False)
	    except AttributeError:
	        gdf = gdf[gdf['geometry'] != None]
	        gdf.to_postgis(f'no_{layer.lower()}', POSTGIS_ENGINE, if_exists='append', index=False)

	# Import monthly production to Postgres
	production_monthly_url = 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/tableview/field_production_monthly&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&IpAddress=not_used&CultureCode=en&rs:Format=CSV&Top100=false'
	p = production_monthly.melt(['prfInformationCarrier', 'prfYear', 'prfMonth'], var_name='commodity', value_name='sm3')



