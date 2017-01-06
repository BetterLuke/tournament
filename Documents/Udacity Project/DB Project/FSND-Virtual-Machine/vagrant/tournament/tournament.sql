-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop database tournament;

-- create the tournament database

create database tournament;

-- connect to the database
\c tournament

-- players database
create table players (
  id SERIAL primary key,
  name text
);

-- matches database
create table matches (
  match_id SERIAL primary key,
  winner INTEGER REFERENCES players(id),
  loser INTEGER REFERENCES players(id)
);

-- view for wins
CREATE VIEW v_wins AS
  select players.id AS player, count(matches.winner) as wins
   from players left join matches
   on players.id = matches.winner
   group by players.id;
-- view for losers
CREATE VIEW v_loser AS
  select players.id AS player, count(matches.loser) as losses
   FROM players LEFT JOIN matches
   ON players.id = matches.loser
   GROUP BY players.id;

-- view for matches played
CREATE VIEW v_matches AS
  select players.id AS player, count(matches) as matches
  FROM players left join matches
  ON(players.id = matches.winner) OR(players.id= matches.loser)
  GROUP BY players.id;

  -- view for player standings
  CREATE VIEW v_standings AS
    SELECT players.id, players.name, v_wins.wins, v_matches.matches
    from players
    LEFT JOIN v_wins on players.id = v_wins.player
    LEFT JOIN v_matches on players.id = v_matches.player
    GROUP BY players.id, players.name, v_wins.wins, v_matches.matches
    ORDER BY v_wins.wins DESC;
