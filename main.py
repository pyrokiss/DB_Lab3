import cx_Oracle
import chart_studio
import re
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash

chart_studio.tools.set_credentials_file(username='Laplas', api_key='0OWdaMuViqDOpQD2oAIF')

def fileId_from_url(url):
    raw_fileId = re.findall("~[0-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

username = 'LAPLAS_DB'
password = 'laplas228'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

Genre = []
GamesGenreCount = []
GamesGenresQuery = '''
SELECT GamesGenres.genre AS genre, COUNT(GamesGenres.genre) AS GamesGenreCount
FROM Games
INNER JOIN GamesGenres
ON Games.gname = GamesGenres.gname
GROUP BY GamesGenres.genre
ORDER BY GamesGenreCount DESC
'''
cursor.execute(GamesGenresQuery)
for row in cursor.fetchall():
    Genre.append(row[0])
    GamesGenreCount.append(row[1])

BarData = [go.Bar(x=Genre, y=GamesGenreCount)]
BarLayout = go.Layout(
    title='Games & Genres',
    xaxis=dict(
        title='Genres',
        titlefont=dict(
            family='Courier New, monospace',
            size=16,
            color='#CB4335'
        )
    ),
    yaxis=dict(
        title='Games',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=16,
            color='#CB4335'
        )
    )
)
GameGenresBar = go.Figure(data = BarData, layout=BarLayout)
TotalGameGenres = py.plot(GameGenresBar, filename = "Plot1")

Platform = []
GamePercent = []
GamesPlatformsQuery = '''
SELECT GamesPlatforms.platform as platform, round(count(*)*100 / (SELECT count(*) FROM Games ), 2 ) as GamePercent
FROM GamesPlatforms
JOIN Games
ON Games.gname = GamesPlatforms.gname
GROUP BY platform
ORDER BY GamePercent DESC
'''
cursor.execute(GamesPlatformsQuery)
for row in cursor.fetchall():
    Platform.append(row[0])
    GamePercent.append(row[1])

PieData = [go.Pie(labels=Platform, values=GamePercent)]
PlatformPie = go.Figure(data = PieData)
TotalPlatformPercent = py.plot(PlatformPie, auto_open=True, file_name="Plot2",)

Release_date = []
GameRelease = []
GameReleaseQuery = '''
SElECT release_date, count(gname) AS GameRelease
FROM Games
GROUP BY release_date
ORDER BY release_date
'''
cursor.execute(GameReleaseQuery)
for row in cursor.fetchall():
    Release_date.append(row[0])
    GameRelease.append(row[1])

ScatterData = [go.Scatter(x=Release_date, y=GameRelease)]
ScatterLayout = go.Layout(
    title="ReleaseDateScatter",
    xaxis=dict(
        title="Date",
        titlefont=dict(
            family='Courier New, monospace',
            size=16,
            color='#CB4335'
        )
    ),

    yaxis=dict(
        title='GameCount',
        titlefont=dict(
            family='Courier New, monospace',
            size=16,
            color='#CB4335'
        )
    )
)
ReleaseDateScatter = go.Figure(data = ScatterData, layout = ScatterLayout)
TotalReleaseDate = py.plot(ReleaseDateScatter, auto_open=True, file_name="Plot3")

my_dashboard = dash.Dashboard()

bar_id = fileId_from_url(TotalGameGenres)
pie_id = fileId_from_url(TotalPlatformPercent)
scatter_id = fileId_from_url(TotalReleaseDate)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': 'QUERY 1'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_id,
    'title': 'QUERY 2'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_id,
    'title': 'QUERY 3'
}

my_dashboard.insert(box_1)
my_dashboard.insert(box_2, 'below', 1)
my_dashboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dashboard, 'DB_LAB2')
cursor.close()
connection.close()