import geopandas as gpd
import pandas as pd
from owslib.wfs import WebFeatureService
from fiona import BytesCollection
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import requests
import logging

log = logging.getLogger(__name__)

# Create SQL engine
load_dotenv('.env')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
engine = create_engine(POSTGRES_DB)

def set_crs(gdf, source_crs, target_crs):
    '''
    Parameters:
    -----------
    gdf : geodataframe
        geodataframe to check
    source_crs: int
        country to set crs
    target_crs: int
    '''
    
    gdf = gdf.set_crs(crs_dict.get(source_crs))
    gdf = gdf.to_crs(target_crs)
        
    return log.info(f'CRS is set to {gdf.crs}')


def get_wfs_layers(url):
    '''Get list of available WFS layers
    and their index'''
    wfs = WebFeatureService(url, version='2.0.0')
    for i, layer in enumerate(wfs.contents):
        print(i, layer)
        

def select_wfs_layer(url, index):
    '''Select a WFS layer by index
    Parameters:
    -----------
    url: str
        url of WFS
    index: int
        index of the layer, can be requested with get_wfs_layers
    '''
    wfs = WebFeatureService(url, version='2.0.0')
    layer = list(wfs.contents)[index]
    
    return layer


def wfs2gdf(layer, url, output_format, wfs_version="2.0.0"):
    '''Creates a geodataframe from WFS
    Parameters:
    -----------
    layer: str
        Find name of layer with function select_wfs_layer
    url: str
        url of wfs
    output_format: str
        xml or json, depending on wfs
    wfs_version: str
        change when version is not 2.0.0.
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


def gdf_to_geopackage(gdf, country, layer, path):
    '''
    Parameters:
    -----------
    gdf: geodataframe
        geodataframe to write
    country: str
        geopackage country
    layer: str
        layer name
    path: str
        path of folder to geopackage
    '''

    path = f'path/{country}/'

    if not os.path.exists(path):
        os.makedirs(path)

    if len(gdf) > 0:
        gdf.to_file(f'{path}{country}_geopackage.gpkg', layer=layer, driver='GPKG')

    return log.info(f'exported {country} -- {name} -- to: {path}')


def gdf_to_postgres(gdf, name, method, country=None):
    '''Writes (geo)dataframe
    to postgis or postgres
    Parameters:
    -----------
    gdf: str
        dataframe or geodataframe
    name: str
        table_name
    country: str
        iso-2 country code, default is None
    method: string
        postgres write method ('replace' or 'append')
    '''
    
    if country is None:
        country = ''
    else:
        country = f'{country}_'

    if 'geometry' in gdf.columns:
        if not gdf.crs:
            raise ValueError('CRS not set')
        
        if len(gdf[gdf['geometry'] != None]) > 0:
            gdf = gdf[gdf['geometry'] != None]

        gdf.to_postgis(f'{country}{name.lower()}', engine, if_exists=method, index=False)
        
    else:
        df = pd.DataFrame(gdf)
        df.to_sql(f'{country}{name.lower()}', engine, if_exists=method, index=False)
    
    return log.info(f'Written {len(gdf)} rows of {gdf.name} to postgres') # TODO: make sure all geodataframes have a name


def write_to_geojson(df, name):
    '''Write infrastructure to geojson
    Parameters:
    -----------
    df : geodataframe
        geodataframe to write
    name : str
        name of the file
    TODO: create a more generic writer that 
    differentiates in dtypes in stead of 
    column names'''

    df = df.to_crs(4326)
    if name != 'pipes':
        df['longitude'] = df.geometry.x
        df['latitude'] = df.geometry.y
    if 'radius' in df.columns:
        df = df.drop('radius', axis=1)
    df['dataset'] = name
    
    def has_list(x):
        return any(isinstance(i, list) for i in x)

    mask = df.apply(has_list)
    cols = df.columns[mask].tolist()
    df[cols] = df[cols].astype(str)
    
    df.to_file(f'../../data/infrastructure/visuals/{name}.geojson', driver='GeoJSON')