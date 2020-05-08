import csv
import io
import cx_Oracle
username = 'LAPLAS_DB'
password = 'laplas228'
database = 'localhost/xe'
connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()
filename = "metacritic_games.csv"
with io.open(filename, newline='', encoding="utf-8") as import_file:
    readerCSV = csv.DictReader(import_file)
    tables = ['Games', 'Publishers', 'Developers', 'Rating', 'Genres', 'Platforms', 'GamesPlatforms', 'GamesGenres']
    for elem in tables:
        cursor.execute("DELETE FROM " + elem)

    Games_names = []
    Games_genres = []
    Games_platforms = []
    Games_ratings = []
    Games_publishers = []
    Games_developers = []
    Games_release_dates = []

    try:
        for row in readerCSV:
            name = row['name']
            if name not in Games_names:
                Games_names.append(name)
            genre = row['genre(s)']
            if genre not in Games_genres:
                Games_genres.append(genre)
            platform = row['platform']
            if platform not in Games_platforms:
                Games_platforms.append(platform)
            publisher = row['publisher']
            if publisher not in Games_publishers:
                Games_publishers.append(publisher)
            developer = row['developer']
            if developer not in Games_developers:
                Games_developers.append(developer)
            rating = row['rating']
            if rating not in Games_ratings:
                Games_ratings.append(rating)
            release_date = row['release_date']
            if release_date not in Games_release_dates:
                Games_release_dates.append(release_date)

            publisher_query = """INSERT INTO Publishers(publisher)
                VALUES (:publisher)"""
            cursor.execute(publisher_query, publisher=publisher)
            developer_query = """INSERT INTO Developers(developer)
                            VALUES (:developer)"""
            cursor.execute(developer_query, developer=developer)
            rating_query = """INSERT INTO Rating(rating)
                            VALUES (:rating)"""
            cursor.execute(rating_query, rating=rating)

            Games_query = """INSERT INTO Games(gname, rating, publisher, developer, release_date)
                                        VALUES (:name, :rating, :publisher, :developer, :release_date)"""
            cursor.execute(Games_query, name=name, rating=rating, publisher=publisher, developer=developer, release_date=release_date)

            genre_query = """INSERT INTO Genres(genre)
                                        VALUES (:genre)"""
            cursor.execute(genre_query, genre=genre)
            platform_query = """INSERT INTO Platforms(platform)
                                        VALUES (:platform)"""
            cursor.execute(platform_query, platform=platform)

            GamesGenres_query = """INSERT INTO GamesGenres(gname, genre)
                                                    VALUES (:name, :genre)"""
            cursor.execute(GamesGenres_query, name=name, genre=genre)

            GamesPlatforms_query = """INSERT INTO GamesPlatforms(gname, platform)
                                                                VALUES (:name, :platform)"""
            cursor.execute(GamesGenres_query, name=name, platform=platform)
    except:
        raise
    finally:
        connection.commit()
        cursor.close()
        connection.close()