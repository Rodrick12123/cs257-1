
CREATE TABLE athletes(
       id integer,
       surname text,
       given_name text,
       nickname text   
);

CREATE TABLE nocs(
       id integer,
       noc text,
       region text
);

CREATE TABLE nocs_athletes_events_games(
       noc_id integer,
       athlete_id integer,
       event_id integer,
       games_id integer,
       medal text
);

CREATE TABLE games(
       id integer,
       year integer,
       season text,
       city text
);

CREATE TABLE events(
       id integer,
       event text,
       sport text
);
