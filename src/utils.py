from typing import List, Optional, Union

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


