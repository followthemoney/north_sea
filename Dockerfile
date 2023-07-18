FROM jupyter/scipy-notebook

RUN conda install -q \
	shapely \
	geopandas \
	psycopg2 \
	gdal \
	requests \
	geopy \
	numpy \
	matplotlib \
	owslib \
	geoalchemy2 \
	hvplot \
	pyproj \
	cartopy \
	geoviews \
	panel \
	movingpandas

RUN pip install python-dotenv ogr missingno

ENV PYTHONPATH "${PYTHONPATH}:/home/jovyan/work"

USER root

RUN apt-get update && apt-get --yes install apt-utils 

RUN apt-get --yes install curl

RUN apt-get --yes install nano

RUN DEBIAN_FRONTEND="noninteractive" apt-get install libmagickwand-dev --no-install-recommends -y

