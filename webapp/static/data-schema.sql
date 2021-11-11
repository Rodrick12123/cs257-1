CREATE TABLE players (
    id integer,
    surname text,
    given_name text,
    coach text
);

CREATE TABLE matches (
    id integer,
    date_time text,
    stage text,
    stadium text,
    city text,
    home_team text,
    home_score integer,
    away_team text,
    away_score integer,
    win_conditions text,
    attendance text,
    home_first_half_goals integer,
    home_second_half_goals integer,
    away_first_half_goals integer,
    away_second_half_goals integer
    
);

CREATE TABLE teams (
    id integer,
    team_abbreviation text,
    team_name text
);

CREATE TABLE worldcups (
    id integer,
    year integer,
    location text,
    firstplace text,
    secoundplace text,
    thirdplace text,
    fourthplace text,
    attendance text,
    totalgoals integer
);