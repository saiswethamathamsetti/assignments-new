Q1="SELECT pid AS actor_id,COUNT(mid) AS no_of_movies FROM  cast GROUP BY pid"
Q2="SELECT year,COUNT(name) AS count FROM Movie GROUP BY year ORDER BY year ASC"
Q3="SELECT year,AVG(rank) AS avg_rank FROM Movie GROUP BY year HAVING count(NAME)>=10 ORDER BY year DESC"
Q4="SELECT year,MAX(rank) AS max_rank FROM Movie GROUP BY year ORDER BY year ASC"
Q5="SELECT rank,COUNT(name) AS no_of_movies FROM Movie WHERE name LIKE 'a%' GROUP BY rank"