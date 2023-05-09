import logging

import geopandas as gpd
import pandas as pd
from dotenv import load_dotenv
import os
import glob
from dateutil.relativedelta import relativedelta
from owslib.wfs import WebFeatureService
import datetime
import zipfile
import fiona
import shutil
import yaml

from north_sea.src.utils import check_countries
import north_sea.src.geo_utils as geo

# Set some environment variables
load_dotenv('.env')
os.environ['PROJ_LIB'] = '/opt/conda/share/proj'

# Create logger
log = logging.getLogger(__name__)

# Add sources

with open('../config/sources.json') as f:
	sources = json.load(f)

# For now, only nl, no and uk have zipfiles to download

# The Netherlands is a special case, because the file names are changing every month
# TODO: solve ArcGIS featureserver problems to extract data from WFS

def create_nl_zipfiles():
    
    today = datetime.date.today()# - relativedelta(months=1) #(uncomment if current month hasn't been uploaded yet
    year = today.year
    month_name = today.strftime('%b').lower()
    month_number = today.strftime('%m')
    
    nl_dict = {'platforms': f'https://www.nlog.nl/sites/default/files/{year}-{month_number}/{month_name}-{year}-nlog-facility_utm.zip',
               'licences': f'https://www.nlog.nl/sites/default/files/{year}-{month_number}/{month_name}-{year}-nlog-licences_utm.zip',
               'fields': f'https://www.nlog.nl/sites/default/files/{year}-{month_number}/{month_name}-{year}-nlog-fields_utm.zip',
               'wellbores': f'https://www.nlog.nl/sites/default/files/{year}-{month_number}/{month_name}-{year}-nlog-boreholes_utm.zip'}
    
    
    return dict(nl_dict)



def download_zipfiles(countries):
    '''Downloads zipfiles
    Parameters:
    -----------
    countries : list
        List of countries'''
    
    for country in check_countries(countries):
        log.info(f'working on {country}')
        if country not in ['nl', 'uk', 'no']: # change this if zipfiles for other countries are available
            raise ValueError(f'No zipfiles available for {country}, please use function download_wfs')

        if isinstance(zip_dict.get(country), dict):
            names = [key for key in zip_dict.get(country).keys()] # get names for logging purposes
            urls = [value for value in zip_dict.get(country).values()]
            
        else:
            names = country.split()
            urls = zip_dict[country].split()
        
        path = f'../data/{country}/'

        if not os.path.exists(path):
            os.makedirs(path)

        for name, url in zip(names, urls):
            r = requests.get(url)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(path)
        
        # Write files to geopackage, this is not necessary per se, but makes life a little bit easier later on
        if country in ['nl', 'uk']:
            for file in glob.glob(f'{path}/*.shp'):
                if country == 'uk':
                    name = os.path.basename(file)[5:-9].lower()
                elif country == 'nl':
                    name = os.path.basename(file)[14:-8].lower()
                
                gdf = gpd.read_file(file)
                gdf = gdf[~gdf.geometry.isna()]
                
                export_to_geopackage(gdf, country, name)
        
        

def download_wfs(countries):
    
    for country in check_countries(countries):
        
        if country in ['uk', 'no']:
            raise ValueError(f'No wfs available for {country}, please use function download_zipfiles')
        
        elif country in ['be', 'dk', 'de', 'int']:
            _country = 'int'
            
            names = ['licences', 'platforms', 'pipes', 'wellbores']
            emod_layers = [0, 78, 79, 24]
            
            url = wfs_dict.get(_country)
            
            for name, layer in zip(names, emod_layers):
                gdf = wfs2gdf(select_wfs_layer(url, layer), url, 'json')
                gdf = gdf[gdf.country == country_dict.get(country)]
                
                export_to_geopackage(gdf, country, name)
        
        elif country == 'nl':
            pipes_url = wfs_dict.get('nl') # change config
            gdf = wfs2gdf(select_wfs_layer(pipes_url, 2), pipes_url, 'json')
            export_to_geopackage(gdf, country, 'pipes')



def write_to_pg(countries):
    
    for country in check_countries(countries):
        path = f'../data/{country}/'
        
        if country == 'no':
            file = f'{path}NPD_FactMapsData_v3_0.gdb/'
        
        else:
            file = f'{path}{country}_geopackage.gpkg'
            
        layers = fiona.listlayers(file)
        for layer in layers:
            export_to_postgres(file, layer, country, engine)
