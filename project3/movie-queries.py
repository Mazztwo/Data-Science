
from neo4j.v1 import GraphDatabase, basic_auth

#connection with authentication
#driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "cs1656"), encrypted=False)

#connection without authentication
driver = GraphDatabase.driver("bolt://localhost", encrypted=False)
session = driver.session()
transaction = session.begin_transaction()





#[Q1]
##########################################
result = transaction.run("""
MATCH (d:Director)-[:DIRECTED]->(m:Movie)
RETURN d.name, count(m)
ORDER BY count(m) DESC
LIMIT 20
;""")
##########################################

#for record in result:
#  print (record['people.name'])





#[Q2]
##########################################
result = transaction.run("""

;""")
##########################################





transaction.close()
session.close()
