# North Sea infrastructure

The notebooks in this repository is part of an investigation into the infrastructure in the North Sea by:
1. NRK ([story](https://www.nrk.no/klima/xl/hver-plattform-i-nordsjoen-ma-ryddes-etter-nedstenging_-men-noen-blir-staende-i-havet-1.16404390))
2. De Tijd ([story](https://multimedia.tijd.be/noordzee-afval))
3. DeSmog 
4. Follow the Money ([story - English](https://www.ftm.eu/articles/north-sea-clean-up-of-rotten-infrastructure-costs-billions-but-no-one-wants-to-pay?share=94b6RpOzWb6IdB%2BPfW%2FrT0VdiqRFrE5u4oUolg%2F2JtTzxewyRrQJRsjQz%2FmX%2BOg%3D%26utm_medium=social&utm_campaign=sharebuttonleden&utm_source=linkbutton)) | ([story - Dutch](https://www.ftm.nl/artikelen/noordzee-opruimen-infrastructuur-kost-miljarden-maar-niemand-wil-betalen?share=mTM7237jIoGsK9ZI9Y1RFHT3wt2h6MXf28rerUacQ1fdrhI%2BrpisHmtJbMzsjWM%3D%26utm_medium=social&utm_campaign=sharebuttonleden&utm_source=linkbutton))

This investigation is part of a larger project on the future of the North Sea and the ongoing and intensifying battle for space.

Below you will find the code used for the stories:

## Goal of this project

Import, load, clean and analyse data on infrastructure in the North Sea (EEZs).

## Run this project

The easiest way to use this code is with Docker. Make sure you have installed Docker. From the parent directory run:

```
docker compose up -d
```

You can access the jupyter notebooks from localhost:8888/lab.

Change the ```.env```, ```sources.json``` and ```yaml``` files to your liking.

The .env file should contain a link to your postgreSQL instance, for instance:

```
POSTGRES_DB = 'postgresql+psycopg2://postgres:postgres@192.01.01.01/north_sea'
```

If you run PostgreSQL locally, you can find the localhost of your PostgreSQL instance by running the following command in your terminal:

```
ifconfig -a | grep inet
```

Make sure you have created a database in PostgreSQL and activated the PostGIS extension.

All database execution is done with SQLAlchemy, so it should be easy to adapt the code to use another SQL dialect, but PostgreSQL/PostGIS is advised for its advanced spatial capabilities.

The sources.json file contains information on data sources, with links to wfs, zipfiles and REST services with some metadata on the sources, like coordinate reference systems of spatial data.

The ontology.yaml file contains all choices we made in normalising the data. This is always an imperfect excercise, with many trade-offs. So make sure you are familiar with this file. 

## TODO

- Preferably I use some ArcGIS data sources, but the [arcgis python api](https://developers.arcgis.com/python/) has trouble running on MacOS silicon. For now I use alternative sources, but in the future I want to change this.
- Refactor all code: create a proper module suitable for all North Sea projects, so generalise a lot of code.
- Move code to the parent directory as much as possible for reusability
- Create online PostgreSQL/PostGIS instance
- Automate import with Argo (Aleph Memorious) or directly in Google Cloud.
- Setup EDA process ([example for movement data](https://github.com/anitagraser/EDA-protocol-movement-data))
- Add more notebook examples

## Data

The data is available in a PostgreSQL/PostGIS instance. Currently the instance is run locally, but will move online soon.

**Datasets for the UK**:

1. [North Sea Transition Authority](https://www.nstauthority.co.uk/)

2. [The Crown Estate Open Data Portal](https://opendata-thecrownestate.opendata.arcgis.com/). Has grid data, but only for power lines connecting wind farms. The shapes cover rough outlines of the grid and don't show the cables connecting the different wind turbines.

**Datasets for the Netherlands**:
1. In the Netherlands, the company TenneT is solely responsible for the offshore grid. Rijkswaterstaat has a high resolution dataset, which is available through the [EMODnet WFS service](https://emodnet.ec.europa.eu/en/emodnet-web-service-documentation). 

2. [NLOG](https://nlog.nl)

**Datasets for Norway**:
1. High resolution data can be downloaded from the [NVE website](https://www.nve.no/map-services/). Look for 'sjokabel'. One important line - The North Sea Link - between the UK and Norway seems to be missing though, so it needs to be validated if the data is complete. 

2. [Oljedirektoratet, NPD](https://npd.no/)

**Datasets for Germany**:
1. Marine data can be downloaded from the [BSH website](https://www.bsh.de/EN/DATA/GeoSeaPortal/geoseaportal_node.html;jsessionid=EF13EF81A7B022395391958E30AF2BE3.live21301). There is a WSF service available, but that seems defunct. Shapefiles can be downloaded as well on the Raumordnungsplannen, which were updated in juni 2021. The shapes are not very detailed and also contain pipelines. 

2. [EMODnet](https://www.emodnet-humanactivities.eu/view-data.php) (European Commission)

**Datasets for Denmark**:
1. There is [a dataset](https://geodata-info.dk/srv/dan/catalog.search#/metadata/44b34117-cf77-40ed-a099-6ec1a5e6bb75) on the North Sea Marine Spatial Plannings, but the data is rather coarse. It doesn't provide much information on features. There seem to be scant resources, which I find a bit strange, since Denmark has a high quality public data infrastructure. More information can [be found here](https://dma.dk/growth-and-framework-conditions/maritime-spatial-plan).

2. [EMODnet](https://www.emodnet-humanactivities.eu/view-data.php) (European Commission)

**Datasets for Belgium**
1. There are some datasets available for Vlaanderen, with many download options. The main source is [Kustportaal](https://www.kustportaal.be/nl). 

2. [EMODnet](https://www.emodnet-humanactivities.eu/view-data.php) (European Commission)


## Limitations and data quality

There are some important limitations for the data, most have to do with missing data and ontology:

1. As becomes clear from the paragraph above, multiple data sources were used with different data, omissions, definitions - sometimes even within datasets. For instance the registration of status of wellbores in the Dutch dataset has changed since January 1st 2022, which makes a comparission between new and old data in this dataset problematic. Within the EMODnet dataset, platforms are defined differently depending on the country. For the UK a platform is called a platform, for other countries it might be called a facility or Condeep (in the case of Norway). We had to make many choices how to deal with these inconsistencies and usually erred on the side of caution. See all the relevant choices in [ontology.yaml](../../config/ontology.yaml).
2. Data for the UK, Netherlands and Norway is much more recent and elaborate than data from Germany, Denmark and Belgium. We found 60 kilometers of pipelines for Denmark in the European registries, but there might be more that is just not reported. 
3. The registries are not always up to date.
4. The registries are not always correct. The status might have changed in reality, but is not updated in the registry. We encountered wellbores that haven't produced any oil or gas in over ten years, but are still registered as active. 
5. For pipelines: the UK EEZ contains far more pipelines than other countries. This probably is largely due to the differences in types of registration. Where possible we used kilometers and not number of pipes, because the length is more telling in the end. 
6. Wellbores cannot be removed and often the status is unknown. If a well is inactive it could be permanent or temporary. Only Norway makes a distinction in the registry between the two statusses. Also it's not clear if permanently plugged means that there are no obligations for the operators or licence holders.
7. We've enriched company data (for operators and licence holders) with data from the national company registries and own research. Where possible we tried to find the mother company, but because of a high consolidation in the fossil fuel business, this data might be outdated soon. The used data reflects the situation of January 1st 2023. We cannot release this data yet, but will add it later on.
8. In some cases we have decided not to use the WFS services for spatial data, but to download zipfiles at the source. It's our experience that the zipfiles contain more information than the WFS services provide. 
9. If you want to download the data yourself, it's highly adviced to use a PostGIS instance, because of the spatial data and some spatial masking that is performed (EEZs vs North Sea boundaries for instance)
10. The North Sea countries are in different jurisdictions (UK, Norway, EU, OSPAR). Be mindful of those differences when analysing the data. The UK has other requirements, for instance, when it comes to plugging wellbores, than Norway or the EU.
11. A good resource for checking or acquiring data is [Mapstand](https://mapstand.com). 
