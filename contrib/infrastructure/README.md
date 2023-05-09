# Infrastructure

## Goal

Import, load, clean and analyse data on infrastructure in the North Sea (EEZs).

## Run

The easiest way to use this code is with Docker. From the parent directory run:

```
docker compose up -d
```

You can access the jupyter notebooks from localhost:8888/lab.

Change the ```.env``` and ```config``` files to your liking.

## Steps

1. Automate imports, store the raw data in an online PostgreSQL/PostGIS.
2. I have chosen to clean the data while importing it. There is some time loss, but the original records are always available. 
3. Check data quality with EDA process
4. Create several analysis notebooks

## TODO

- Preferably I use some ArcGIS data sources, but the [arcgis python api](https://developers.arcgis.com/python/) has trouble running on MacOS silicon. For now I use alternative sources, but in the future I want to change this.
- Refactor all code: create a proper module suitable for all North Sea projects.
- Move code to the parent directory as much as possible for reusability
- Create online PostgreSQL/PostGIS instance
- Automate import with Argo (Aleph Memorious) or directly in Google Cloud.
- Setup EDA process ([example for movement data](https://github.com/anitagraser/EDA-protocol-movement-data))
- Clean analysis notebooks

## Data

The data is available in a PostgreSQL instance. Currently the instance is run locally, but will move online soon.

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