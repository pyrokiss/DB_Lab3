CREATE OR REPLACE VIEW GamesInfo AS
SELECT Games.gname,
       Games.release_date,
       Gamesgenres.genre,
       Gamesplatforms.platform
FROM
Games
JOIN gamesgenres
    ON Games.gname = Gamesgenres.gname
JOIN gamesplatforms
    ON Games.gname = Gamesplatforms.gname;