import os
from dotenv import load_dotenv
from neo4j import GraphDabase

URI = os.environ.get('NEO4J_URI')
USER = os.environ.get('NEO4J_USER')
PASSWORD = os.environ.get('NEO4J_PASSWORD')

# Initialize connection

class Neo4jConnection:
    
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, parameters=None, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query, parameters))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response

conn = Neo4jConnection(uri=URI, 
                       user=USER,              
                       pwd=PASSWORD)


# Create node constraints
def create_node_constraints():
    conn.query('CREATE CONSTRAINT company IF NOT EXISTS ON (c:Company) ASSERT c.registration_number IS UNIQUE')
    conn.query('CREATE CONSTRAINT asset IF NOT EXISTS ON (a:Asset) ASSERT a.mps_uuid IS UNIQUE')
    conn.query('CREATE CONSTRAINT ownership IF NOT EXISTS on (o:Ownership) ASSERT o.id IS UNIQUE')
    return print('Created constraints')