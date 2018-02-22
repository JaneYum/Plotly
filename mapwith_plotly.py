
import plotly.plotly as py
import csv
import requests

#f = open('2011_february_us_airport_traffic.csv')
f = open('2011_february_CA_airport_traffic.csv')
csv_data = csv.reader(f)

lat_vals = []
lon_vals = []
text_vals = []
for row in csv_data:
    if row[0] != 'iata':
        lat_vals.append(row[5])
        lon_vals.append(row[6])
        text_vals.append(row[0])

data = [ dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = lon_vals,
        lat = lat_vals,
        text = text_vals,
        mode = 'markers',
        marker = dict(
            size = 8,
            symbol = 'star',
        ))]

## get the lat axis and lon axis by looking at the data...

min_lat = 10000
max_lat = -10000
min_lon = 10000
max_lon = -10000

for str_v in lat_vals:
    v = float(str_v)
    if v < min_lat:
        min_lat = v
    if v > max_lat:
        max_lat = v
for str_v in lon_vals:
    v = float(str_v)
    if v < min_lon:
        min_lon = v
    if v > max_lon:
        max_lon = v

center_lat = (max_lat+min_lat) / 2
center_lon = (max_lon+min_lon) / 2

max_range = max(abs(max_lat - min_lat), abs(max_lon - min_lon))
padding = max_range * .10
lat_axis = [min_lat - padding, max_lat + padding]
lon_axis = [min_lon - padding, max_lon + padding]

layout = dict(
        title = 'US airports<br>(Hover for airport names)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(100, 217, 217)",
            countrycolor = "rgb(217, 100, 217)",
            lataxis = {'range': lat_axis},
            lonaxis = {'range': lon_axis},
            center= {'lat': center_lat, 'lon': center_lon },
            countrywidth = 3,
            subunitwidth = 3
        ),
    )

fig = dict(data=data, layout=layout )
py.plot( fig, validate=False, filename='usa - airports' )
