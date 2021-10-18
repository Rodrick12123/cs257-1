
CREATE TABLE athletes(
       id integer,
       surname text,
       given_name text
     
);

CREATE TABLE nocs(
       id integer,
       noc text,
       region text
);

CREATE TABLE nocs_athletes(
       noc_id integer,
       athlete_id integer
);

CREATE TABLE athletes_events(
       athlete_id integer,
       event_id integer
       medal text
);

CREATE TABLE events_games(
       event_id integer,
       game_id integer,
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





#maybe not this
CREATE TABLE medals(
       id SERIAL,
       finish text,
       games_id integer,
       event_id integer,
       athlete_id integer
);       
 