
from neo4j.v1 import GraphDatabase, basic_auth
import sys

#connection with authentication
#driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "cs1656"), encrypted=False)

#connection without authentication
driver = GraphDatabase.driver("bolt://localhost", encrypted=False)
session = driver.session()
transaction = session.begin_transaction()

# Open output file
output = open("output.txt", "w+")

# TO WRITE


output.write("### Q1 ###\n")
output.write("\n")
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

output.write("### Q2 ###\n")
output.write("\n")
#[Q2]
##########################################
result = transaction.run("""
MATCH (any)-[:RATED]->(m:Movie)
RETURN DISTINCT(m.title)
;""")
##########################################

output.write("### Q3 ###\n")
output.write("\n")
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


output.write("### Q4 ###\n")
output.write("\n")
#[Q4]
##########################################
result = transaction.run("""
MATCH (a:Actor)-[:ACTS_IN]->(m:Movie)<-[:DIRECTED]-(d:Director)
WITH a.name as actors, count(DISTINCT d.name) AS directors WHERE directors > 3
RETURN actors, directors
ORDER BY directors DESC
;""")
##########################################



output.write("### Q5 ###\n")
output.write("\n")
#[Q5]
##########################################
result = transaction.run("""
MATCH (bacon:Actor {name: "Kevin Bacon"})-[:ACTS_IN]->(m)<-[:ACTS_IN]-(b1:Actor)-[:ACTS_IN]->(m2)<-[:ACTS_IN]-(b2:Actor)
RETURN b2.name
;""")
##########################################

output.write("### Q6 ###\n")
output.write("\n")
#[Q6]
##########################################
result = transaction.run("""
MATCH (bacon:Actor {name: "Kevin Bacon"})-[:ACTS_IN]->(m:Movie)
RETURN DISTINCT(m.genre)
;""")
##########################################


output.write("### Q7 ###\n")
output.write("\n")
#[Q7]
##########################################
result = transaction.run("""
MATCH (d:Director)-[:DIRECTED]->(m:Movie)
WITH d.name AS dcts, count(DISTINCT m.genre) AS genres WHERE genres > 2
RETURN dcts, genres
ORDER BY genres DESC
;""")
##########################################


output.write("### Q8 ###\n")
output.write("\n")
#[Q8]
##########################################
result = transaction.run("""
MATCH (a:Actor)-[:ACTS_IN]->(m)<-[:DIRECTED]-(d:Director)
RETURN DISTINCT a.name, d.name, count(m)
ORDER BY count(m) DESC
LIMIT 10
;""")
##########################################


transaction.close()
session.close()
output.close()