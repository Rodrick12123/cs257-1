CREATE TABLE players (
    playerid integer,
    tid integer,
    firstname text,
    lastname text,
    captain text,
    starter text

);

CREATE TABLE matches (
    roundid integer,
    matchid integer,
    time integer,
    stage text,
    homename text,
    awayname text,
    homescore text,
    awayteam text,
    wincond text
);

CREATE TABLE stadium (
    matchid integer,
    stadiumname text,
    city text
);

CREATE TABLE teams (
    teamid integer,
    coach text,
    teamname text
);

CREATE TABLE cups (
    cupid integer,
    year text,
    loc text,
    attendance text,
    totalgoals integer,
    firstplace text,
    secoundplace text,
    thirdplace text
);