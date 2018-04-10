# Alessio Mazzone
# CS 1656 Data Science
# Project 4


import sqlite3 as lite
#import pandas
import csv
import re
con = lite.connect('cs1656.sqlite')

with con:
	cur = con.cursor() 

	########################################################################		
	### CREATE TABLES ######################################################
	########################################################################		
	# DO NOT MODIFY - START 
	cur.execute('DROP TABLE IF EXISTS Actors')
	cur.execute("CREATE TABLE Actors(aid INT, fname TEXT, lname TEXT, gender CHAR(6), PRIMARY KEY(aid))")

	cur.execute('DROP TABLE IF EXISTS Movies')
	cur.execute("CREATE TABLE Movies(mid INT, title TEXT, year INT, rank REAL, PRIMARY KEY(mid))")

	cur.execute('DROP TABLE IF EXISTS Directors')
	cur.execute("CREATE TABLE Directors(did INT, fname TEXT, lname TEXT, PRIMARY KEY(did))")

	cur.execute('DROP TABLE IF EXISTS Cast')
	cur.execute("CREATE TABLE Cast(aid INT, mid INT, role TEXT)")

	cur.execute('DROP TABLE IF EXISTS Movie_Director')
	cur.execute("CREATE TABLE Movie_Director(did INT, mid INT)")
	# DO NOT MODIFY - END

	########################################################################		
	### READ DATA FROM FILES ###############################################
	########################################################################		
	# actors.csv, cast.csv, directors.csv, movie_dir.csv, movies.csv
	# UPDATE THIS
	
	#df1 = pandas.read_csv('actors.csv', header=None)
	#df2 = pandas.read_csv('cast.csv', header=None)
	#df3 = pandas.read_csv('directors.csv', header=None)
	#df4 = pandas.read_csv('movie_dir.csv', header=None)
	#df5 = pandas.read_csv('movies.csv', header=None)

	with open('actors.csv', newline='') as rawfile:
		data = csv.reader(rawfile, delimiter=',', quotechar='|')
		for row in data:
			cur.execute("INSERT INTO Actors VALUES(" + row[0] + ", '" + row[1]+ "', '" + row[2] + "', '" + row[3] + "')")

	with open('cast.csv', newline='') as rawfile:
		data = csv.reader(rawfile, delimiter=',', quotechar='|')
		for row in data:
			cur.execute("INSERT INTO Cast VALUES(" + row[0] + ", " + row[1] + ", '" + row[2] + "')")

	with open('directors.csv', newline='') as rawfile:
		data = csv.reader(rawfile, delimiter=',', quotechar='|')
		for row in data:	
			cur.execute("INSERT INTO Directors VALUES(" + row[0] + ", '" + row[1] + "', '" + row[2] + "')")		

	with open('movie_dir.csv', newline='') as rawfile:
		data = csv.reader(rawfile, delimiter=',', quotechar='|')
		for row in data:
			cur.execute("INSERT INTO Movie_Director VALUES(" + row[0] + ", " + row[1] + ")")

	with open('movies.csv', newline='') as rawfile:
		data = csv.reader(rawfile, delimiter=',', quotechar='|')
		for row in data:
			cur.execute("INSERT INTO Movies VALUES(" + row[0] + ", '" + row[1] + "', " + row[2] + ", " + row[3] + ")")


	########################################################################		
	### INSERT DATA INTO DATABASE ##########################################
	########################################################################		
	# UPDATE THIS TO WORK WITH DATA READ IN FROM CSV FILES
	#cur.execute("INSERT INTO Actors VALUES(1001, 'Harrison', 'Ford', 'Male')") 
	#cur.execute("INSERT INTO Actors VALUES(1002, 'Daisy', 'Ridley', 'Female')")   

	#cur.execute("INSERT INTO Movies VALUES(101, 'Star Wars VII: The Force Awakens', 2015, 8.2)") 
	#cur.execute("INSERT INTO Movies VALUES(102, 'Rogue One: A Star Wars Story', 2016, 8.0)")
	
	#cur.execute("INSERT INTO Cast VALUES(1001, 101, 'Han Solo')")  
	#cur.execute("INSERT INTO Cast VALUES(1002, 101, 'Rey')")  

	#cur.execute("INSERT INTO Directors VALUES(5000, 'J.J.', 'Abrams')")  
	
	#cur.execute("INSERT INTO Movie_Director VALUES(5000, 101)")  

	con.commit()
    
    	

	########################################################################		
	### QUERY SECTION ######################################################
	########################################################################		
	queries = {}

	# DO NOT MODIFY - START 	
	# DEBUG: all_movies ########################
	queries['all_movies'] = '''
SELECT * FROM Movies
'''	
	# DEBUG: all_actors ########################
	queries['all_actors'] = '''
SELECT * FROM Actors
'''	
	# DEBUG: all_cast ########################
	queries['all_cast'] = '''
SELECT * FROM Cast
'''	
	# DEBUG: all_directors ########################
	queries['all_directors'] = '''
SELECT * FROM Directors
'''	
	# DEBUG: all_movie_dir ########################
	queries['all_movie_dir'] = '''
SELECT * FROM Movie_Director
'''	
	# DO NOT MODIFY - END

	########################################################################		
	### INSERT YOUR QUERIES HERE ###########################################
	########################################################################		
	# NOTE: You are allowed to also include other queries here (e.g., 
	# for creating views), that will be executed in alphabetical order.
	# We will grade your program based on the output files q01.csv, 
	# q02.csv, ..., q12.csv


	# Q01 ########################
    # List all the actors (first and last name) who acted in at least one film in the 80s (1980-1990, both ends inclusive) and in at least one film in the 21st century (>=2000).
	queries['q01'] ='''
SELECT Actors.fname, Actors.lname
FROM Actors
JOIN Cast AS cast1
    ON cast1.aid = Actors.aid
JOIN Cast AS cast2
    ON cast2.aid = Actors.aid
JOIN Movies AS movie1
    ON movie1.mid = cast1.mid
JOIN Movies AS movie2
    ON movie2.mid = cast2.mid
WHERE movie1.year BETWEEN 1980 AND 1990
    AND movie2.year >= 2000
GROUP BY Actors.fname, Actors.lname
'''


	# Q02 ########################
    # List all the movies (title, year) that were released in the same year as the movie entitled "Rogue One: A Star Wars Story", but had a better rank (Note: the higher the value in the rank attribute, the better the rank of the movie).
	queries['q02'] ='''
SELECT Movies.title, Movies.year
FROM Movies
JOIN Movies AS r1
    ON r1.title = "Rogue One: A Star Wars Story"
WHERE Movies.year = r1.year AND Movies.rank > r1.rank
'''
    
	# Q03 ########################
    # List all the actors (first and last name) who played in a Star Wars movie (i.e., title like '%Star Wars%') in decreasing order of how many Star Wars movies they appeared in. If an actor plays multiple roles in the same movie, count that still as one movie.
	queries['q03'] = '''
SELECT a.fname, a.lname, count(DISTINCT m.mid) AS num
FROM Actors AS a
JOIN Cast AS c
    ON c.aid = a.aid
JOIN Movies AS m
    ON c.mid = m.mid
WHERE m.title LIKE '%Star Wars%'
GROUP BY a.fname, a.lname
ORDER BY num DESC
'''

	# Q04 ########################
    # Find the actor(s) (first and last name) who only acted in films released before 1985.
	queries['q04'] = '''
SELECT a.fname, a.lname
FROM Actors AS a
WHERE a.aid IN
    (SELECT a.aid
     FROM Actors AS a
     JOIN Cast AS c ON c.aid = a.aid
     WHERE c.mid IN
        (SELECT Movies.mid
         FROM Movies
         WHERE Movies.year < 1985))
AND a.aid NOT IN
    (SELECT a.aid
     FROM Actors AS a
     JOIN Cast AS c ON c.aid = a.aid
     WHERE c.mid IN
        (SELECT Movies.mid
         FROM Movies
         WHERE Movies.year >= 1985))
GROUP BY a.fname, a.lname
'''	

	# Q05 ########################
    #  List the top 20 directors in descending order of the number of films they directed (first name, last name, number of films directed). For simplicity, feel free to ignore ties at the number 20 spot (i.e., always show up to 20 only).
	queries['q05'] = '''
SELECT d.fname, d.lname, COUNT(*) AS num
FROM Directors AS d
JOIN Movie_Director AS m
WHERE d.did = m.did
GROUP BY d.fname, d.lname
ORDER BY num DESC
LIMIT 20
'''	


# Actors (aid, fname, lname, gender)
# Movies (mid, title, year, rank)
# Cast (aid, mid, role)
# Directors (did, fname, lname)
# Movie_Director (did, mid)

# Find the top 10 movies with the largest cast (title, number of cast members) in decreasing order. Note: show all movies in case of a tie.

#SELECT m.title, COUNT(c.aid) AS num
#FROM Movies AS m
#JOIN Cast AS c ON m.mid = c.mid
#GROUP BY m.title
#ORDER BY num DESC
#LIMIT 10

#DOES NOT SHOW TIES!!!

	# Q06 ########################
    # Find the top 10 movies with the largest cast (title, number of cast members) in decreasing order. Note: show all movies in case of a tie.
	queries['q06'] = '''
SELECT c.mid, m.title, COUNT(c.aid) AS num
FROM Movies AS m
JOIN Cast AS c ON m.mid = c.mid
GROUP BY m.title
ORDER BY num DESC
LIMIT 10
'''	

	# Q07 ########################
    # Find the movie(s) whose cast has more actresses than actors (i.e., gender=female vs gender=male). Show the title, the number of actresses, and the number of actors in the results.
	queries['q07'] = '''
SELECT f.title, f.females, m.males
FROM
    (SELECT m.mid, m.title, count(*) AS females
    FROM Actors AS a
    JOIN Cast AS c ON c.aid = a.aid
    JOIN Movies AS m ON m.mid = c.mid
    WHERE a.gender = 'Female'
    GROUP BY m.title) AS f
JOIN
    (SELECT m.mid, m.title, count(*) AS males
    FROM Actors AS a
    JOIN Cast AS c ON c.aid = a.aid
    JOIN Movies AS m ON m.mid = c.mid
    WHERE a.gender = 'Male'
    GROUP BY m.title) AS m ON f.title = m.title
WHERE f.females > m.males
GROUP BY f.title
ORDER BY f.females DESC
'''
    
	# Q08 ########################
    # Find all the actors who have worked with at least 7 different directors. Do not consider cases of self-directing (i.e., when the director is also an actor in a movie), but count all directors in a movie towards the threshold of 7 directors. Show the actor's first, last name, and the number of directors he/she has worked with. Sort in decreasing order of number of directors.
	queries['q08'] = '''
SELECT a.aid, a.fname, a.lname, count(DISTINCT d.did) numDir
FROM Actors AS a
JOIN Cast AS c ON c.aid = a.aid
JOIN Movies AS m ON m.mid = c.mid
JOIN Movie_Director AS md ON md.mid = m.mid
JOIN Directors AS d ON d.did = md.did
WHERE a.fname != d.fname AND a.lname != d.lname
GROUP BY a.fname, a.lname
ORDER BY numDir DESC
'''
    
	# Q09 ########################
    # For all actors whose first name starts with an S, count the movies that he/she appeared in his/her debut year (i.e., year of their first movie). Show the actor's first and last name, plus the count. Sort by decreasing order of the count.
	queries['q09'] = '''
SELECT x.fname, x.lname, x.cnt
FROM
    (SELECT j.fname, j.lname, j.cnt, MIN(j.year) AS debut
    FROM
            (SELECT sa.aid, sa.fname, sa.lname, count(*) AS cnt, m.year
            FROM
                 (SELECT a.aid, a.fname, a.lname
                  FROM Actors AS a
                  WHERE a.fname LIKE 'S%') AS sa
            JOIN Cast AS c ON c.aid = sa.aid
            JOIN Movies AS m ON m.mid = c.mid
            GROUP BY m.year) AS j
    GROUP BY j.aid) AS x
ORDER BY x.cnt DESC
'''

	# Q10 ########################
    # Find instances of nepotism between actors and directors, i.e., an actor in a movie and the director having the same last name, but a different first name. Show the last name and the title of the movie, sorted alphabetically by last name.
	queries['q10'] = '''
SELECT d.lname, m.title
FROM Actors AS a
JOIN Cast AS c ON a.aid = c.aid
JOIN Movies AS m ON m.mid = c.mid
JOIN Movie_Director AS md ON md.mid = c.mid
JOIN Directors AS d ON d.did = md.did
WHERE d.lname = a.lname AND d.fname != a.fname
ORDER BY a.lname ASC
'''	

# Actors (aid, fname, lname, gender)
# Movies (mid, title, year, rank)
# Cast (aid, mid, role)
# Directors (did, fname, lname)
# Movie_Director (did, mid)


	# Q11 ########################
    # The Bacon number of an actor is the length of the shortest path between the actor and Kevin Bacon in the "co-acting" graph. That is, Kevin Bacon has Bacon number 0; all actors who acted in the same movie as him have Bacon number 1; all actors who acted in the same film as some actor with Bacon number 1 have Bacon number 2, etc. List all actors whose Bacon number is 2 (first name, last name). You can familiarize yourself with the concept, by visiting The Oracle of Bacon.
	queries['q11'] = '''
        SELECT a2.fname, a2.lname
        FROM
            (SELECT m.mid
            FROM Actors AS a
            JOIN Cast AS c On a.aid = c.aid
            JOIN Movies AS m ON m.mid = c.mid
            WHERE a.fname = 'Kevin' AND a.lname = 'Bacon') AS baconMovies
        JOIN Cast AS c1 ON c1.mid = baconMovies.mid
        JOIN Actors AS a1 ON a1.aid = c1.aid
        JOIN Cast AS c2 ON c2.aid = a1.aid
        JOIN Movies AS m1 ON m1.mid = c2.mid
        JOIN Cast AS c3 ON c3.mid = m1.mid
        JOIN Actors AS a2 ON a2.aid = c3.aid
        WHERE c3.mid != baconMovies.mid AND a1.aid != a2.aid AND a1.fname != "Kevin" AND a1.lname != "Bacon"
        GROUP BY a2.fname, a2.lname
'''	

	# Q12 ########################
    # Assume that the popularity of an actor is reflected by the average rank of all the movies he/she has acted in. Find the top 20 most popular actors (in descreasing order of popularity) -- list the actor's first/last name, the total number of movies he/she has acted, and his/her popularity score. For simplicity, feel free to ignore ties at the number 20 spot (i.e., always show up to 20 only).
	queries['q12'] = '''
'''	


	########################################################################		
	### SAVE RESULTS TO FILES ##############################################
	########################################################################		
	# DO NOT MODIFY - START 	
	for (qkey, qstring) in sorted(queries.items()):
		try:
			cur.execute(qstring)
			all_rows = cur.fetchall()
			
			print ("=========== ",qkey," QUERY ======================")
			print (qstring)
			print ("----------- ",qkey," RESULTS --------------------")
			for row in all_rows:
				print (row)
			print (" ")

			save_to_file = (re.search(r'q0\d', qkey) or re.search(r'q1[012]', qkey))
			if (save_to_file):
				with open(qkey+'.csv', 'w') as f:
					writer = csv.writer(f)
					writer.writerows(all_rows)
					f.close()
				print ("----------- ",qkey+".csv"," *SAVED* ----------------\n")
		
		except lite.Error as e:
			print ("An error occurred:", e.args[0])
	# DO NOT MODIFY - END
	
