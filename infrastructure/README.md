# Infrastructure

## Electricity grid North Sea

### Goal

To assess the difficulties in building an integrated North Sea electricty grid. 

### Steps

1. Map the current electricity grid infrastructure in the North Sea from several countries (UK, NL, NO, DK, DE, BE, FR, IS).
2. Enrich data with ownership and technical information
3. Map several projections and scenarios


### Data

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
1. There is [a dataset](https://geodata-info.dk/srv/dan/catalog.search#/metadata/44b34117-cf77-40ed-a099-6ec1a5e6bb75) on the North Sea Marine Spatial Plannings, but the data is rather course. It doesn't provide much information on features. There seem to be scant resources, which I find a bit strange, since Denmark has a high quality public data infrastructure. More information can [be found here](https://dma.dk/growth-and-framework-conditions/maritime-spatial-plan).

2. [EMODnet](https://www.emodnet-humanactivities.eu/view-data.php) (European Commission)

**Datasets for Belgium**
1. There are some datasets available for Vlaanderen, with many download options. The main source is [Kustportaal](https://www.kustportaal.be/nl). 

2. [EMODnet](https://www.emodnet-humanactivities.eu/view-data.php) (European Commission)