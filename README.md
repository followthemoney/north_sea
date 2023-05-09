![Bron: Wikimedia](https://github.com/ftmnl/north_sea/blob/main/img/north_sea.jpeg)

# North Sea Project

This repository contains all code and links to data for the FTM's North Sea Project. This project is ongoing, so code will be added during the project. The data will be made available later, but all data sources and code for storing, cleaning and analysing are provided. 

## Use cases

1. The first story is on infrastructure and you can find some jupyter notebooks in the folder [Notebooks - Infrastructure](https://github.com/ftmnl/north_sea/tree/main/notebooks/infrastructure/]. Some modules can be found in [src](https://github.com/ftmnl/north_sea/tree/main/src/)

## How to run

The easiest way to run all code is by using docker and run the command (in this parent directory)

```
docker compose up -d
```

You can access the jupyter notebooks from localhost:8888/lab.


Make sure you set the proper environment variables, for instance the PostgreSQL/PostGIS connection, in an .env file and adapt all configuration in the yaml files to your liking.