import logging
from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, Integer, DateTime, Float, String
from geoalchemy2 import Geometry
from sqlalchemy.engine import Connection
from sqlalchemy.dialects.postgresql import insert as upsert

from dotenv import load_dotenv

load_dotenv('.env')

Conn = Connection

log = logging.getLogger(__name__)
engine = create_engine(os.environ.get('POSTGRES_DB'))
meta = MetaData(bind=engine)

__all__ = ["Conn", "upsert", "create_db"]


def create_db() -> None:
    meta.create_all(checkfirst=True)

nl_fields = Table(
    "nl_fields",
    meta,
    Column("field_dbk", Float, primary_key=True),
    Column("field_name", String(100), nullable=False),
    Column("field_code", String(50), nullable=False),
    Column("first_fiel", String(50)),
    Column("leg_status", String(50)),
    Column("geometry_a", String(50)),
    Column("geometry_l", String(50)),
    Column("geometry", Geometry(geometry_type='POLYGON', srid=28992))
)


nl_licences = Table(
    "nl_licences",
    meta,
    Column("gmlid", String(100), primary_key=True),
    Column("rownum", Float),
    Column("gdnr_objec", String(100)),
    Column("gdnr_colle", String(100)),
    Column("licence_cd", String(100)),
    Column("licence_ty", String(100)),
    Column("licence_st", String(100)),
    Column("licence_re", String(100)),
    Column("legenda_cd", String(100)),
    Column("licenced_a", String(100)),
    Column("licenced_1", String(100)),
    Column("transparen", Float),
    Column("transparen", Integer),
    Column("geometry", Geometry(geometry_type='POLYGON', srid=28992))
) 


nl_boreholes = Table(
    "nl_boreholes",
    meta,
    Column("borehole_d", Float, primary_key=True),
    Column("short_nm", String(100), nullable=False),
    Column("result_cd", String(50), nullable=False),
    Column("purpose_cd", String(50)),
    Column("geometry", Geometry(geometry_type='POINT', srid=28992))
)

nl_platforms = Table(
    "nl_platforms",
    meta,
    Column("facility_d", String(100), primary_key=True),
    Column("facility_c", String(100)),
    Column("type", String(100)),
    Column("operator", String(100)),
    Column("status", String(100)),
    Column("wells", ARRAY(String(100))),
    Column("country_cd", String(10)),
    Column("x_utm31", Integer),
    Column("y_utm31", Integer),
    Column("longitude", Float),
    Column("latitude", Float),
    Column("geometry", Geometry(geometry_type='POINT', srid=28992))
) 

no_companies = Table(
    "no_companies",
    meta,
    Column("cmpnpdidcompany", Integer, primary_key=True),
    Column("cmplongname", String(100)),
    Column("cmporgnumberbrreg", BigInteger),
    Column("cmpgroup", String(100)),
    Column("cmpfactpageurl", String(100)),
    Column("cmpactiveonncscurrent", String(2)),
    Column("cmplicenceoperformer", String(2)),
    Column("cmplicenceopercurrent", String(2)),
    Column("cmplicencelicenseecurrent", String(2)),
    Column("cmpbsnsarrareaoperformer", String(2)),
    Column("cmpbsnsarrareapartnercurrent", String(2)),
    Column("cmpbsnsarrareapartnerformer", String(2)),
    Column("cmptufopercurrent", String(2)),
    Column("cmptufoperformer", String(2)),
    Column("cmptufpartnercurrent", String(2)),
    Column("cmptufpartnerformer", String(2)),
    Column("cmpfacilitymoveableresponsible", String(2)),
    Column("cmpfacilityfixedoperator", String(2)),
    Column("cmpnationcode", String(2)),
    Column("cmpsurveyprefix", String(2)),
    Column("geometry", Geometry(geometry_type='POLYGON', srid=23032), nullable=True)
)

no_discovery_reserves = Table(
    "no_dicovery_reserves",
    meta,
    Column("dscnpdiddiscovery", Integer, primary_key=True),
    Column("dscdateoffresestdisplay", DateTime),
    Column("dscresestcomments", String(500)),
    Column("dscreservesrc", String(50)),
    Column("dscrecoverableoil", Float),
    Column("dscrecoverablegas", Float),
    Column("dscrecoverablengl", Float),
    Column("dscrecoverablecondensate", Float),
    Column("dscrecoverableoe", Float),
    Column("dscreservesdateupdated", DateTime),
    Column("geometry", Geometry(geometry_type='POLYGON', srid=23032), nullable=True)
)

no_facility_function = Table(
    "no_facility_function",
    meta,
    Column("fclname", String(50), primary_key=True),
    Column("fclfunctionname", String(50)),
    Column("fclfromdate", DateTime),
    Column("fclnpdidfacility", BigInteger),
    Column("geometry", Geometry(geometry_type='POLYGON', srid=23032), nullable=True)
)

no_field_activity_hst_status = Table(
    "no_field_activity_hst_status",
    meta,
    Column("fldnpdidfield", BigInteger, primary_key=True),
    Column("fldstatusfromdate", DateTime, primary_key=True),
    Column("fldstatustodate", DateTime),
    Column("fldstatus", String(50)),
    Column("fldstatusdateupdated", DateTime, nullable=True),
    Column("geometry", Geometry(geometry_type='POLYGON', srid=23032), nullable=True)
)



