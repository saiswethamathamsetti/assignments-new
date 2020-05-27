Q2="SELECT year,COUNT(Movie) FROM Movie GROUP BY year"
Q4="SELECT year,MAX(rank) AS max_rank FROM Movie GROUP BY year ORDER BY year ASC"