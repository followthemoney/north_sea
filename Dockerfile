FROM jupyter/scipy-notebook

RUN conda install -q \
	shapely \
	geopandas \
	psycopg2 \
	gdal \
	requests \
	geopy \
	sqlalchemy \
	numpy \
	matplotlib \
	owslib \
	geoalchemy2 \
	hvplot \
	pyproj \
	bokeh \
	cartopy \
	cython \
	geoviews \
	panel \
	movingpandas \
	seaborn \
	jupyterlab \
	jupyterlab-git


RUN pip install python-dotenv ogr

USER root

RUN apt-get update && apt-get --yes install apt-utils 

RUN apt-get --yes install curl

RUN apt-get --yes install nano
