#List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. These entities, by the way, are mostly equivalent to countries. But in some cases, you might find that a portion of a country participated in a particular games (e.g. one guy from Newfoundland in 1904) or some other oddball situation.

SELECT nocs.noc
FROM nocs
ORDER BY nocs.noc

#List the names of all the athletes from Kenya. If your database design allows it, sort the athletes by last name.

SELECT athletes.surname, athletes.given_name, athletes.nickname
FROM athletes, nocs, nocs_athletes
WHERE athletes.id = nocs_athletes.athlete_id
AND nocs.id = nocs_athletes.noc_id
AND nocs.noc LIKE 'Kenya'
ORDER BY athletes.surname


#List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate.

SELECT events_athletes.medal, events.event, games.year, games.season, games.city
FROM events, athletes, events_athletes, events_games, games
WHERE athletes.id = events_athletes.athlete_id
AND events.id = events_athletes.event_id
AND athletes.surname LIKE 'Louganis'
AND athletes.given_name LIKE 'Greg' 
AND events.id = events_games.event_id
AND games.id = events_games.games_id
ORDER BY games.year


#List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.

SELECT 
FROM
WHERE
AND
ORDER BY