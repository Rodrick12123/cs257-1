
CREATE TABLE athletes(
       id SERIAL,
       surname text,
       given_name text
       team_id integer,
       
       event_id integer,
       games_id integer,
       medal text
);

CREATE TABLE nocs(
       id SERIAL,
       noc text,
       region text

);

CREATE TABLE nocs_athletes(
       noc_id integer,
       athlete_id integer
);

CREATE TABLE athletes_medals(
       athlete_id integer,
       medal_id integer
);

CREATE TABLE games(
       id SERIAL,
       year integer,
       season text,
       city text
);

CREATE TABLE events(
       id SERIAL,
       event text,
       sport text
);

CREATE TABLE medals(
       id SERIAL,
       finish text,
       games_id integer,
       event_id integer,
       athlete_id integer
);       
       