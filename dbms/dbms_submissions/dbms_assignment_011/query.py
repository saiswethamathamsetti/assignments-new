Q1="SELECT `Actor`.id,`Actor`.fname,`Actor`.lname,`Actor`.gender FROM Actor INNER JOIN Cast ON `Actor`.id=`Cast`.pid INNER JOIN Movie ON `Movie`.id=`Cast`.mid WHERE `Movie`.name LIKE 'Annie%'"
Q2="SELECT Movie.id,Movie.name,Movie.rank,Movie.year FROM Movie INNER JOIN MovieDirector ON Movie.id=MovieDirector.mid INNER JOIN Director ON Director.id=MovieDirector.did WHERE Director.fname='Biff' AND Director.lname='Malibu' AND Movie.year IN (1999,1994,2003) ORDER BY rank DESC,year ASC"
Q3="SELECT year,COUNT(year) AS no_of_movies FROM Movie AS M GROUP BY year HAVING (SELECT AVG(rank) FROM Movie)<AVG(rank) ORDER BY year ASC"
Q4="SELECT id,name,year,rank FROM Movie WHERE year=2001 AND rank<(SELECT AVG(rank) FROM Movie) ORDER BY rank DESC LIMIT 10"
Q7="SELECT fname,COUNT(fname) AS count FROM Director GROUP BY fname HAVING COUNT(fname)>1"
Q6="SELECT DISTINCT `Actor`.`id` FROM Cast INNER JOIN Actor ON `Actor`.`id`=`Cast`.`pid` INNER JOIN Movie ON `Movie`.`id`=`Cast`.`mid` GROUP BY `Actor`.`id`,`Movie`.`id` HAVING COUNT(DISTINCT role)>1 ORDER BY `Actor`.id ASC Limit 100;"

Q8="""SELECT `Director`.id,`Director`.fname,`Director`.lname FROM Director WHERE EXISTS
(SELECT * FROM MovieDirector INNER JOIN Cast ON `MovieDirector`.mid=`Cast`.mid WHERE `Director`.id=`MovieDirector`.did
GROUP BY `MovieDirector`.did,`Cast`.mid HAVING COUNT(DISTINCT `Cast`.pid)>=100) AND
NOT EXISTS (SELECT * FROM MovieDirector INNER JOIN Cast ON `MovieDirector`.mid=`Cast`.mid WHERE `Director`.id=`MovieDirector`.did
GROUP BY `MovieDirector`.did,`Cast`.mid HAVING COUNT(DISTINCT `Cast`.pid)<100)"""  
