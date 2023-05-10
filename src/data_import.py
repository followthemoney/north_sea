from dateutil.relativedelta import relativedelta
import datetime
from owslib.wfs import WebFeatureService
import logging
import geopandas as gpd
import pandas as pd
from dotenv import load_dotenv
import os
import glob
import zipfile, io
import fiona
import json
import requests

from src.utils import check_countries
import src.geo_utils as geo
import src.data_import as imp

# Set some environment variables
load_dotenv('.env')
os.environ['PROJ_LIB'] = '/opt/conda/share/proj'
PATH_RAW = os.environ.get('PATH_RAW')

# Create logger
log = logging.getLogger(__name__)

# Add sources

with open('../../config/sources.json') as f:
	sources = json.load(f)

zipfiles = [file for file in sources if 'zip' in file.get('filetype')]

# For now, only nl, no and uk have zipfiles to download

# The Netherlands is a special case, because the file names are changing every month
# TODO: solve ArcGIS featureserver problems to extract data from WFS

def create_nl_zipfiles(zipfiles):
    
    today = datetime.date.today()# - relativedelta(months=1) #(uncomment if current month hasn't been uploaded yet
    year = today.year
    month_name = today.strftime('%b').lower()
    month_number = today.strftime('%m')
    
    nl_files = [file.get('url') for file in zipfiles if 'nl' in file.get('countries')]

    nl_dict = dict()
    # This is a bit of a hack. Would prefer to use f-strings
    for name, file in zip(nl_names, nl_files):
        file = file.replace('{year}', str(year)).replace('{month_number}', str(month_number)).replace('{month_name}', month_name)
        update = {name:file}
        nl_dict.update(update)
    
    return dict(nl_dict)


def download_zipfiles(countries, zipfiles):
    '''Downloads zipfiles
    Parameters:
    -----------
    countries : list
        List of countries'''
    
    for country in check_countries(countries):
        log.info(f'working on {country}')
        if country not in ['nl', 'uk', 'no']: # change this if zipfiles for other countries are available
            raise ValueError(f'No zipfiles available for {country}, please use function download_wfs')
        
        elif country in ['uk', 'no']:
            urls = [file.get('url') for file in zipfiles if country in file.get('countries')]

        elif country in ['nl']:
            urls = [value for value in create_nl_zipfiles(zipfiles).values()]
        
        
        path = f'{PATH_RAW}{country}/'

        if not os.path.exists(path):
            os.makedirs(path)

        for url in zip(urls):
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
                
                geo.export_to_geopackage(gdf, country, name)
             

def download_wfs(countries):
    
    for country in check_countries(countries):

        path = f'{PATH_RAW}{country}/'
        
        if country in ['uk', 'no']:
            raise ValueError(f'No wfs available for {country}, please use function download_zipfiles')
        
        elif country in ['be', 'dk', 'de', 'int']:
            _country = 'int'
            
            names = ['licences', 'platforms', 'pipes', 'wellbores']
            emod_layers = [0, 78, 79, 24]
            
            url = wfs_dict.get(_country)
            

            for name, layer in zip(names, emod_layers):
                gdf = geo.wfs2gdf(geo.select_wfs_layer(url, layer), url, 'json')
                gdf = gdf[gdf.country == country_dict.get(country)]
                
                geo.export_to_geopackage(gdf, country, name, path)
        
        elif country == 'nl':
            pipes_url = wfs_dict.get('nl') # change config
            gdf = geo.wfs2gdf(geo.select_wfs_layer(pipes_url, 2), pipes_url, 'json')
            geo.export_to_geopackage(gdf, country, 'pipes', path)


def write_to_postgres(countries):
    
    for country in check_countries(countries):
        path = f'PATH_RAW{country}/'
        
        if country == 'no':
            file = f'{path}NPD_FactMapsData_v3_0.gdb/'
        
        else:
            file = f'{path}{country}_geopackage.gpkg'
            
        layers = fiona.listlayers(file)
        for layer in layers:
            geo.export_to_postgres(file, layer, country, engine)
