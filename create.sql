CREATE TABLE Games(
    gname VARCHAR(100) NOT NULL,
    rating VARCHAR(5) NOT NULL,
    publisher VARCHAR(50) NOT NULL,
    developer VARCHAR(50) NOT NULL,
    release_date VARCHAR(50) NOT NULL
);
ALTER TABLE Games ADD CONSTRAINT gname_pk PRIMARY KEY (gname);

CREATE TABLE Platforms(
    platform VARCHAR(50) NOT NULL
);
ALTER TABLE Platforms ADD CONSTRAINT platform_pk PRIMARY KEY (platform);

CREATE TABLE Genres(
    genre VARCHAR(50) NOT NULL
);
ALTER TABLE Genres ADD CONSTRAINT genre_pk PRIMARY KEY (genre);

CREATE TABLE Publishers(
    publisher VARCHAR(50) NOT NULL
);
ALTER TABLE Publishers ADD CONSTRAINT publisher_pk PRIMARY KEY (publisher);

CREATE TABLE Developers(
    developer VARCHAR(50) NOT NULL
);
ALTER TABLE Developers ADD CONSTRAINT developer_pk PRIMARY KEY (developer);

CREATE TABLE Rating(
    rating VARCHAR(50) NOT NULL
);
ALTER TABLE Rating ADD CONSTRAINT rating_pk PRIMARY KEY (rating);

CREATE TABLE GamesGenres(
    gname VARCHAR(100) NOT NULL,
    genre VARCHAR(50) NOT NULL
);
ALTER TABLE GamesGenres ADD CONSTRAINT gname_genre_pk PRIMARY KEY (gname);

CREATE TABLE GamesPlatforms(
    gname VARCHAR(100) NOT NULL,
    platform VARCHAR(50) NOT NULL
);
ALTER TABLE GamesPlatforms ADD CONSTRAINT gname_platform_pk PRIMARY KEY (gname);

--FOREIGN KEY GAMES--
        
ALTER TABLE Games
    ADD CONSTRAINT rating_fk FOREIGN KEY ( rating )
        REFERENCES Rating ( rating );
        
ALTER TABLE Games
    ADD CONSTRAINT publisher_fk FOREIGN KEY ( publisher )
        REFERENCES Publishers ( publisher );        

ALTER TABLE Games
    ADD CONSTRAINT developer_fk FOREIGN KEY ( developer )
        REFERENCES Developers ( developer );
        
--FOREIGN KEY GAMESGENRES--
ALTER TABLE GamesGenres
    ADD CONSTRAINT genre_fk FOREIGN KEY ( genre )
        REFERENCES Genres ( genre );
        
--FOREIGN KEY GAMESPLATFORMS--
ALTER TABLE GamesPlatforms
    ADD CONSTRAINT platform_fk FOREIGN KEY ( platform )
        REFERENCES Platforms ( platform );        
