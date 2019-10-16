USE lahman2019clean;

DROP TABLE IF EXISTS JOHNS;
DROP VIEW IF EXISTS AverageHeightWeight, AverageHeight;

/*QUESTION 0
EXAMPLE QUESTION
What is the highest salary in baseball history?
*/
SELECT MAX(salary) AS max_salary
FROM Salaries;

/*QUESTION 1
Select the first name, last name, and given name of players who are taller than 6 ft
[hint]: Use "People"
*/
SELECT nameFirst, nameLast, nameGiven
FROM People
WHERE height > 72;

/*QUESTION 2
Create a Table of all the distinct players with a first name of John who were born in the United States and
played at Fordham university
Include their first name, last name, playerID, and birth state
Add a column called nameFull that is a concatenated version of first and last
[hint] Use a Join between People and CollegePlaying
*/
CREATE TABLE JOHNS AS
	SELECT DISTINCT p.nameFirst, p.nameLast, p.playerID, p.birthState
    FROM people AS p
    JOIN collegeplaying as cp
    ON p.playerID = cp.playerID
    WHERE p.nameFirst = "John" and p.birthCountry = "USA" and cp.schoolID = "fordham"
;

/*QUESTION 3
Delete all Johns from the above table whose total career runs batted in is less than 2
[hint] use a subquery to select these johns from people by playerid
[hint] you may have to set sql_safe_updates = 1 to delete without a key
*/
SET SQL_SAFE_UPDATES = 0;
DELETE FROM JOHNS
WHERE EXISTS (
	SELECT p.playerID
    FROM people AS p
    JOIN batting AS b
	ON p.playerID = b.playerID
    WHERE b.RBI < 2
		AND JOHNS.playerID = p.playerID
);
SET SQL_SAFE_UPDATES = 1;

/*QUESTION 4
Group together players with the same birth year, and report the year, 
 the number of players in the year, and average height for the year
 Order the resulting by year in descending order. Put this in a view
 [hint] height will be NULL for some of these years
*/
CREATE VIEW AverageHeight(birthYear, nPlayers, avgHeight)
AS
  SELECT birthYear, count(playerID), avg(height)
  FROM people
  GROUP BY birthYear
  ORDER BY birthYear DESC;
;

/*QUESTION 5
Using Question 3, only include groups with an average weight >180 lbs,
also return the average weight of the group. This time, order by ascending
*/
CREATE VIEW AverageHeightWeight(birthYear, nPlayers, avgHeight, avgWeight)
AS
	SELECT aw.birthYear, nPlayers, avgHeight, avgWeight
	FROM (
		SELECT birthYear, avg(weight) as avgWeight
        FROM people
        GROUP BY birthYear
	) aw
	JOIN AverageHeight AS ah
    ON ah.birthYear = aw.birthYear
	WHERE avgWeight > 180
	ORDER BY birthYear ASC
;

/*QUESTION 6
Find the players who made it into the hall of fame who played for a college located in NY
return the player ID, first name, last name, and school ID. Order the players by School alphabetically.
Update all entries with full name Columbia University to 'Columbia University!' in the schools table
*/
SELECT DISTINCT people.playerID, nameFirst, nameLast, schoolID
FROM people
JOIN (
	SELECT hof.playerID as playerID, schoolID
	FROM HallOfFame AS hof
    JOIN (
		SELECT playerID, CollegePlaying.schoolID 
		FROM CollegePlaying
		JOIN schools
        ON CollegePlaying.schoolID = schools.schoolID
		WHERE schools.state = "NY"
	) school 
	ON hof.playerID = school.playerID
) nyhof
ON people.playerID = nyhof.playerID
ORDER BY schoolID;

SET SQL_SAFE_UPDATES = 0;
UPDATE Schools set name_full = "Columbia University!" where name_full = "Columbia University";
SET SQL_SAFE_UPDATES = 1;

/*QUESTION 7
Find the team id, yearid and average HBP for each team using a subquery.
Limit the total number of entries returned to 100
group the entries by team and year and order by descending values
[hint] be careful to only include entries where AB is > 0
*/
SELECT teamID, yearID, avg(HBP) AS avgHBP
FROM (
	SELECT teamID, yearID, HBP
	FROM teams
	WHERE AB > 0
) t
GROUP BY teamID, yearID
ORDER BY avgHBP DESC
LIMIT 100;
