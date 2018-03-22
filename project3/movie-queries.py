
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
MATCH (any)-[:RATED]->(m:Movie)
RETURN DISTINCT(m.title)
;""")
##########################################




#[Q3]
##########################################
result = transaction.run("""
MATCH (any)-[:RATED]->(m:Movie)
WITH DISTINCT(m.title) as ttl
MATCH (a:Actor)-[:ACTS_IN]->(mov:Movie {title: ttl })
RETURN ttl, count(a.name)
ORDER BY count(a.name) DESC
LIMIT 1
;""")
##########################################



#[Q4]
##########################################
result = transaction.run("""
MATCH (a:Actor)-[:ACTS_IN]->(m:Movie)<-[:DIRECTED]-(d:Director)
WITH a.name as actors, count(DISTINCT d.name) AS directors WHERE directors > 3
RETURN actors, directors
ORDER BY directors DESC
;""")
##########################################



transaction.close()
session.close()
