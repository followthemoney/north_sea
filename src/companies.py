
import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv('../../.env')
os.environ['PROJ_LIB'] = '/opt/conda/share/proj'

engine = create_engine(os.environ.get('POSTGRES_DB'), connect_args={'options': '-csearch_path={}'.format('public')})
connection = engine.connect()


def get_licence_and_company(df):
    '''Merges infrastructure dataframes
    with licence info data
    Parameters:
    -----------
    df : dataframe or geodataframe
    TODO: write a more generic function'''

    # First get companies from PostgreSQL
    
    com = pd.read_sql(text('SELECT * FROM current_licences_companies'), connection)
    com_norm = pd.read_sql(text('SELECT * FROM companies'), connection)
    com = pd.merge(com, com_norm, left_on='name', right_on='name_db', how='left')
    com_to_merge = com.groupby(['licence_id'])[['name_international', 'name_local','country_international']].agg(lambda x: list(set(list(x)))).reset_index()
    com_to_merge = com_to_merge.rename(columns={'name_international': 'owner_name_normalised', 
                                                'name_local': 'owner_name',
                                                'country_international': 'owner_country'})
        
    
    # Get licence data
    licence = gpd.GeoDataFrame.from_postgis(text('SELECT * FROM all_current_licences'), connection, geom_col='geometry')
    
    # Perform spatial join on licences
    df = gpd.sjoin(df,
                licence[['geometry', 'licence_name']],
                how='left',
                predicate='intersects')
    df = df.drop(['index_right'], axis=1)
    
    # Perform spatial join on companies
    df = pd.merge(df, 
                com_to_merge,
                left_on = 'licence_name',
                right_on = 'licence_id',
                how='left')

    # Clean it up
    df = df.drop_duplicates(subset=['feature_id', 'country', 'infra_name'], keep='first').copy()
    print(f'Merged {len(df)}, but could not merge {len(df[df.owner_name_normalised.isna()])} because of missing company names')
    
    return df