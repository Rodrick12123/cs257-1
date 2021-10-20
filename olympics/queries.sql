/* List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. These entities, by the way, are mostly equivalent to countries. But in some cases, you might find that a portion of a country participated in a particular games (e.g. one guy from Newfoundland in 1904) or some other oddball situation. */

SELECT nocs.noc
FROM nocs
ORDER BY nocs.noc;

/* List the names of all the athletes from Kenya. If your database design allows it, sort the athletes by last name. */

SELECT DISTINCT nocs.noc, athletes.surname, athletes.given_name, athletes.nickname
FROM athletes, nocs, nocs_athletes_events_games
WHERE athletes.id = nocs_athletes_events_games.athlete_id
AND nocs.id = nocs_athletes_events_games.noc_id
AND nocs.region = 'Kenya'
ORDER BY athletes.surname;

/* List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate. */

SELECT athletes.nickname, athletes.surname, nocs_athletes_events_games.medal, events.event, games.year, games.season, games.city
FROM events, athletes, nocs_athletes_events_games, games
WHERE athletes.id = nocs_athletes_events_games.athlete_id
AND events.id = nocs_athletes_events_games.event_id
AND games.id = nocs_athletes_events_games.games_id
AND athletes.surname = 'Louganis' 
AND athletes.nickname = 'Greg'
AND nocs_athletes_events_games.medal != 'NA'
ORDER BY games.year;


/* List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals. */

/* where I found how GROUP BY method works: https://www.w3schools.com/sql/sql_groupby.asp */

SELECT nocs.noc, COUNT(nocs_athletes_events_games.medal)
FROM nocs, athletes, events, games, nocs_athletes_events_games
WHERE nocs.id = nocs_athletes_events_games.noc_id
AND athletes.id = nocs_athletes_events_games.athlete_id
AND events.id = nocs_athletes_events_games.event_id
AND games.id = nocs_athletes_events_games.games_id
AND nocs_athletes_events_games.medal = 'Gold'
GROUP BY nocs.noc
ORDER BY COUNT(nocs_athletes_events_games.medal) DESC;
