import csv
import cx_Oracle

username = 'LAPLAS_DB'
password = 'laplas228'
database = 'localhost/xe'
connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

tables = ['Games', 'Publishers', 'Developers', 'Rating', 'Genres', 'Platforms', 'GamesPlatforms', 'GamesGenres']
for elem in tables:
    with open(elem + '.csv', 'w', newline='') as ex_file:
        cursor.execute('SELECT * FROM ' + elem)

        row = cursor.fetchone()

        writerCSV = csv.writer(ex_file, delimiter=',')

        while row:
            writerCSV.writerow(row)
            row = cursor.fetchone()
cursor.close()
connection.close()