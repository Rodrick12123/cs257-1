CREATE TABLE players (
    playerid integer,
    tmid integer,
    firstname text,
    lastname text,
    captain text,
    starter text,
    pnumber integer,
    position text
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
    cupid integer,
    coach text,
    teamname text,
    year integer
);

CREATE TABLE cups (
    cupid integer,
    year integer,
    loc text,
    attendance text,
    totalgoals integer,
    firstplace text,
    secoundplace text,
    thirdplace text
);