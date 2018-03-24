
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

output.write("### Q1 ###\n")
#[Q1]
##########################################
result = transaction.run("""
MATCH (d:Director)-[:DIRECTED]->(m:Movie)
RETURN d.name, count(m)
ORDER BY count(m) DESC
LIMIT 20
;""")
##########################################

for record in result:
    output.write(record['d.name'])
    output.write(", ")
    output.write(str(record['count(m)']))
    output.write("\n")

output.write("\n### Q2 ###\n")

#[Q2] 
##########################################
result = transaction.run("""
MATCH (any)-[:RATED]->(m:Movie)
RETURN DISTINCT(m.title)
;""")
##########################################

for record in result:
    output.write(record['(m.title)'])
    output.write("\n")



output.write("\n### Q3 ###\n")
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

for record in result:
    output.write(record['ttl'])
    output.write(", ")
    output.write(str(record['count(a.name)']))
    output.write("\n")



output.write("\n### Q4 ###\n")
#[Q4]
##########################################
result = transaction.run("""
MATCH (a:Actor)-[:ACTS_IN]->(m:Movie)<-[:DIRECTED]-(d:Director)
WITH a.name as actors, count(DISTINCT d.name) AS directors WHERE directors > 2
RETURN actors, directors
ORDER BY directors DESC
;""")
##########################################

for record in result:
    output.write(record['actors'])
    output.write(", ")
    output.write(str(record['directors']))
    output.write("\n")


output.write("\n### Q5 ###\n")
#[Q5]
##########################################
result = transaction.run("""
MATCH (bacon:Actor {name: "Kevin Bacon"})-[:ACTS_IN]->(m)<-[:ACTS_IN]-(b1:Actor)-[:ACTS_IN]->(m2)<-[:ACTS_IN]-(b2:Actor)
RETURN b2.name
;""")
##########################################
for record in result:
    output.write(record['b2.name'])
    output.write("\n")


output.write("\n### Q6 ###\n")
#[Q6]
##########################################
result = transaction.run("""
MATCH (bacon:Actor {name: "Kevin Bacon"})-[:ACTS_IN]->(m:Movie)
RETURN DISTINCT(m.genre)
;""")
##########################################


output.write("\n### Q7 ###\n")
#[Q7]
##########################################
result = transaction.run("""
MATCH (d:Director)-[:DIRECTED]->(m:Movie)
WITH d.name AS dcts, count(DISTINCT m.genre) AS genres WHERE genres > 2
RETURN dcts, genres
ORDER BY genres DESC
;""")
##########################################


output.write("\n### Q8 ###\n")
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