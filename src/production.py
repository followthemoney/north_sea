
'''
WORK IN PROGRESS
'''






# Import monthly production to Postgres
production_monthly_url = 'https://factpages.npd.no/ReportServer_npdpublic?/FactPages/tableview/field_production_monthly&rs:Command=Render&rc:Toolbar=false&rc:Parameters=f&IpAddress=not_used&CultureCode=en&rs:Format=CSV&Top100=false'
p = production_monthly.melt(['prfInformationCarrier', 'prfYear', 'prfMonth'], var_name='commodity', value_name='sm3')





sm3dict = {'Oil': 1000000,
           'Gas': 1000000000,
           'NGL': 1000000,
           'Condensate': 1000000,
           'OeNet': 1000000,
           'WaterInField': 1000000}

for k, v, in sm3dict.items():
    p['sm3'] = np.where(p['commodity'].str.contains(k),
                    p['sm3'] * v,
                    p['sm3'])
    
p.commodity = p.commodity.str.replace('prfPrd|NetMillSm3|NetBillSm3|MillSm3', '', regex=True)

p = p[p.commodity != 'prfNpdidInformationCarrier']

p.columns = p.columns.str.lower()

p['date'] = pd.to_datetime(p['year'].astype(str) + '-' + p['month'].astype(str) + '-01')

p.to_sql('no_production_monthly', POSTGIS_ENGINE, if_exists='append')

# Remove folder and contents

shutil.rmtree('..data/NO/')