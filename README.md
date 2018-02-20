# Plotly
pip install plotly

Plotly provides a web-service for hosting graphs! Create a free account to get started. Graphs are saved inside your online Plotly account and you control the privacy. Public hosting is free, for private hosting, check out our paid plans. 

After installing the Plotly package, you're ready to fire up python: 

$ python 

and set your credentials:

In [10]:
import plotly
plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
You'll need to replace 'DemoAccount' and 'lr1c37zw81' with your Plotly username and API key.
Find your API key here. 

The initialization step places a special .plotly/.credentials file in your home directory. Your ~/.plotly/.credentials file should look something like this: 

{
    "username": "DemoAccount",
    "stream_ids": ["ylosqsyet5", "h2ct8btk1s", "oxz4fm883b"],
    "api_key": "lr1c37zw81"
}

# Don't name your file name as plotly

import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='stacked-bar')
