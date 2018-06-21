******
Plotly
******

Installation
============
.. code-block:: console

    $ pip install plotly

Offline usage
=============
.. code-block:: python

    # Change from
    import plotly.plotly as py

    # to
    import  plotly.offline as py


.. code-block:: python

    import  plotly.offline as py
    import  plotly.graph_objsplotly  as go

    x = [1, 2, 3, 4]
    y = [4, 3, 2, 1]

    py.plot({
        "data": [go.Scatter(x=x, y=y)],
        "layout": go.Layout(title="hello world")
    })

Jupyter Usage
=============
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go


    x = [1, 2, 3, 4]
    y = [4, 3, 2, 1]

    py.iplot({
        "data": [go.Scatter(x=x, y=y)],
        "layout": go.Layout(title="hello world")
    })

Plotting
========

Simple
------
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go
    import math
    import numpy as np

    x = [x for x in np.arange(0, 10, 0.1)]
    y = [math.sin(y) for y in np.arange(0, 5, 0.1)]

    py.iplot({
        "data": [go.Scatter(x=x, y=y)],
        "layout": go.Layout(title="Sin(x)")
    })

Box Plot
--------

Basic Box Plot
^^^^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go
    import numpy as np


    y0 = np.random.randn(50)-1
    y1 = np.random.randn(50)+1

    py.iplot([
        go.Box(y=y0),
        go.Box(y=y1),
    ])

Colored Box Plot
^^^^^^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    import numpy as np

    y0 = np.random.randn(50)
    y1 = np.random.randn(50)+1

    trace0 = go.Box(
        y=y0,
        name = 'Sample A',
        marker = dict(
            color = 'rgb(214, 12, 140)',
        )
    )
    trace1 = go.Box(
        y=y1,
        name = 'Sample B',
        marker = dict(
            color = 'rgb(0, 128, 128)',
        )
    )
    data = [trace0, trace1]
    py.iplot(data)

Groupped
^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    x = ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1',
         'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2']

    trace0 = go.Box(
        y=[0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
        x=x,
        name='kale',
        marker=dict(
            color='#3D9970'
        )
    )
    trace1 = go.Box(
        y=[0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
        x=x,
        name='radishes',
        marker=dict(
            color='#FF4136'
        )
    )
    trace2 = go.Box(
        y=[0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
        x=x,
        name='carrots',
        marker=dict(
            color='#FF851B'
        )
    )
    data = [trace0, trace1, trace2]
    layout = go.Layout(
        yaxis=dict(
            title='normalized moisture',
            zeroline=False
        ),
        boxmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig)

Outlayers
^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    trace0 = go.Box(
        y = [0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
           8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name = "All Points",
        jitter = 0.3,
        pointpos = -1.8,
        boxpoints = 'all',
        marker = dict(
            color = 'rgb(7,40,89)'),
        line = dict(
            color = 'rgb(7,40,89)')
    )

    trace1 = go.Box(
        y = [0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
            8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name = "Only Whiskers",
        boxpoints = False,
        marker = dict(
            color = 'rgb(9,56,125)'),
        line = dict(
            color = 'rgb(9,56,125)')
    )

    trace2 = go.Box(
        y = [0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
            8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name = "Suspected Outliers",
        boxpoints = 'suspectedoutliers',
        marker = dict(
            color = 'rgb(8,81,156)',
            outliercolor = 'rgba(219, 64, 82, 0.6)',
            line = dict(
                outliercolor = 'rgba(219, 64, 82, 0.6)',
                outlierwidth = 2)),
        line = dict(
            color = 'rgb(8,81,156)')
    )

    trace3 = go.Box(
        y = [0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15,
            8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
        name = "Whiskers and Outliers",
        boxpoints = 'outliers',
        marker = dict(
            color = 'rgb(107,174,214)'),
        line = dict(
            color = 'rgb(107,174,214)')
    )

    data = [trace0,trace1,trace2,trace3]

    layout = go.Layout(
        title = "Box Plot Styling Outliers"
    )

    fig = go.Figure(data=data,layout=layout)
    py.iplot(fig, filename = "Box Plot Styling Outliers")

Time Series
===========

Simple
^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    import pandas as pd

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

    data = [go.Scatter(
              x=df.Date,
              y=df['AAPL.Close'])]

    py.iplot(data)

Manually Set Range
^^^^^^^^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    import pandas as pd

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

    trace_high = go.Scatter(
                    x=df.Date,
                    y=df['AAPL.High'],
                    name = "AAPL High",
                    line = dict(color = '#17BECF'),
                    opacity = 0.8)

    trace_low = go.Scatter(
                    x=df.Date,
                    y=df['AAPL.Low'],
                    name = "AAPL Low",
                    line = dict(color = '#7F7F7F'),
                    opacity = 0.8)

    data = [trace_high,trace_low]

    layout = dict(
        title = "Manually Set Date Range",
        xaxis = dict(
            range = ['2016-07-01','2016-12-31'])
    )

    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename = "Manually Set Range")

Rangeslider
^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    import pandas as pd

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

    trace_high = go.Scatter(
        x=df.Date,
        y=df['AAPL.High'],
        name = "AAPL High",
        line = dict(color = '#17BECF'),
        opacity = 0.8)

    trace_low = go.Scatter(
        x=df.Date,
        y=df['AAPL.Low'],
        name = "AAPL Low",
        line = dict(color = '#7F7F7F'),
        opacity = 0.8)

    data = [trace_high,trace_low]

    layout = dict(
        title='Time Series with Rangeslider',
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(),
            type='date'
        )
    )

    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename = "Time Series with Rangeslider")

Two plots
=========

Multiple x-axis
^^^^^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    trace1 = go.Scatter(
        x=[1, 2, 3],
        y=[40, 50, 60],
        name='yaxis data'
    )
    trace2 = go.Scatter(
        x=[2, 3, 4],
        y=[4, 5, 6],
        name='yaxis2 data',
        yaxis='y2'
    )
    data = [trace1, trace2]
    layout = go.Layout(
        title='Double Y Axis Example',
        yaxis=dict(
            title='yaxis title'
        ),
        yaxis2=dict(
            title='yaxis2 title',
            titlefont=dict(
                color='rgb(148, 103, 189)'
            ),
            tickfont=dict(
                color='rgb(148, 103, 189)'
            ),
            overlaying='y',
            side='right'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.iplot(fig, filename='multiple-axes-double')

Multiple y-axis
^^^^^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    trace1 = go.Scatter(
        x=[1, 2, 3],
        y=[4, 5, 6],
        name='yaxis1 data'
    )
    trace2 = go.Scatter(
        x=[2, 3, 4],
        y=[40, 50, 60],
        name='yaxis2 data',
        yaxis='y2'
    )
    trace3 = go.Scatter(
        x=[4, 5, 6],
        y=[40000, 50000, 60000],
        name='yaxis3 data',
        yaxis='y3'
    )
    trace4 = go.Scatter(
        x=[5, 6, 7],
        y=[400000, 500000, 600000],
        name='yaxis4 data',
        yaxis='y4'
    )
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(
        title='multiple y-axes example',
        width=800,
        xaxis=dict(
            domain=[0.3, 0.7]
        ),
        yaxis=dict(
            title='yaxis title',
            titlefont=dict(
                color='#1f77b4'
            ),
            tickfont=dict(
                color='#1f77b4'
            )
        ),
        yaxis2=dict(
            title='yaxis2 title',
            titlefont=dict(
                color='#ff7f0e'
            ),
            tickfont=dict(
                color='#ff7f0e'
            ),
            anchor='free',
            overlaying='y',
            side='left',
            position=0.15
        ),
        yaxis3=dict(
            title='yaxis4 title',
            titlefont=dict(
                color='#d62728'
            ),
            tickfont=dict(
                color='#d62728'
            ),
            anchor='x',
            overlaying='y',
            side='right'
        ),
        yaxis4=dict(
            title='yaxis5 title',
            titlefont=dict(
                color='#9467bd'
            ),
            tickfont=dict(
                color='#9467bd'
            ),
            anchor='free',
            overlaying='y',
            side='right',
            position=0.85
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.iplot(fig, filename='multiple-axes-multiple')

Line Plot Modes
^^^^^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    # Create random data with numpy
    import numpy as np

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N)+5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N)-5

    # Create traces
    trace0 = go.Scatter(
        x = random_x,
        y = random_y0,
        mode = 'lines',
        name = 'lines'
    )
    trace1 = go.Scatter(
        x = random_x,
        y = random_y1,
        mode = 'lines+markers',
        name = 'lines+markers'
    )
    trace2 = go.Scatter(
        x = random_x,
        y = random_y2,
        mode = 'markers',
        name = 'markers'
    )
    data = [trace0, trace1, trace2]

    py.iplot(data, filename='line-mode')

Labels with annotations
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    title = 'Main Source for News'

    labels = ['Television', 'Newspaper', 'Internet', 'Radio']

    colors = ['rgba(67,67,67,1)', 'rgba(115,115,115,1)', 'rgba(49,130,189, 1)', 'rgba(189,189,189,1)']

    mode_size = [8, 8, 12, 8]

    line_size = [2, 2, 4, 2]

    x_data = [
        [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
        [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
        [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
        [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
    ]

    y_data = [
        [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69],
        [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
        [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
        [18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 23],
    ]

    traces = []

    for i in range(0, 4):
        traces.append(go.Scatter(
            x=x_data[i],
            y=y_data[i],
            mode='lines',
            line=dict(color=colors[i], width=line_size[i]),
            connectgaps=True,
        ))

        traces.append(go.Scatter(
            x=[x_data[i][0], x_data[i][11]],
            y=[y_data[i][0], y_data[i][11]],
            mode='markers',
            marker=dict(color=colors[i], size=mode_size[i])
        ))

    layout = go.Layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            autotick=False,
            ticks='outside',
            tickcolor='rgb(204, 204, 204)',
            tickwidth=2,
            ticklen=5,
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            showticklabels=False,
        ),
        autosize=False,
        margin=dict(
            autoexpand=False,
            l=100,
            r=20,
            t=110,
        ),
        showlegend=False,
    )

    annotations = []

    # Adding labels
    for y_trace, label, color in zip(y_data, labels, colors):
        # labeling the left_side of the plot
        annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                      xanchor='right', yanchor='middle',
                                      text=label + ' {}%'.format(y_trace[0]),
                                      font=dict(family='Arial',
                                                size=16,
                                                color=colors,),
                                      showarrow=False))
        # labeling the right_side of the plot
        annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
                                      xanchor='left', yanchor='middle',
                                      text='{}%'.format(y_trace[11]),
                                      font=dict(family='Arial',
                                                size=16,
                                                color=colors,),
                                      showarrow=False))
    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                                  xanchor='left', yanchor='bottom',
                                  text='Main Source for News',
                                  font=dict(family='Arial',
                                            size=30,
                                            color='rgb(37,37,37)'),
                                  showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                                  xanchor='center', yanchor='top',
                                  text='Source: PewResearch Center & ' +
                                       'Storytelling with data',
                                  font=dict(family='Arial',
                                            size=12,
                                            color='rgb(150,150,150)'),
                                  showarrow=False))

    layout['annotations'] = annotations

    fig = go.Figure(data=traces, layout=layout)
    py.iplot(fig, filename='news-source')

Filled Line
^^^^^^^^^^^
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x_rev = x[::-1]

    # Line 1
    y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1_upper = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y1_lower = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y1_lower = y1_lower[::-1]

    # Line 2
    y2 = [5, 2.5, 5, 7.5, 5, 2.5, 7.5, 4.5, 5.5, 5]
    y2_upper = [5.5, 3, 5.5, 8, 6, 3, 8, 5, 6, 5.5]
    y2_lower = [4.5, 2, 4.4, 7, 4, 2, 7, 4, 5, 4.75]
    y2_lower = y2_lower[::-1]

    # Line 3
    y3 = [10, 8, 6, 4, 2, 0, 2, 4, 2, 0]
    y3_upper = [11, 9, 7, 5, 3, 1, 3, 5, 3, 1]
    y3_lower = [9, 7, 5, 3, 1, -.5, 1, 3, 1, -1]
    y3_lower = y3_lower[::-1]

    trace1 = go.Scatter(
        x=x+x_rev,
        y=y1_upper+y1_lower,
        fill='tozerox',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        showlegend=False,
        name='Fair',
    )
    trace2 = go.Scatter(
        x=x+x_rev,
        y=y2_upper+y2_lower,
        fill='tozerox',
        fillcolor='rgba(0,176,246,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='Premium',
        showlegend=False,
    )
    trace3 = go.Scatter(
        x=x+x_rev,
        y=y3_upper+y3_lower,
        fill='tozerox',
        fillcolor='rgba(231,107,243,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        showlegend=False,
        name='Fair',
    )
    trace4 = go.Scatter(
        x=x,
        y=y1,
        line=dict(color='rgb(0,100,80)'),
        mode='lines',
        name='Fair',
    )
    trace5 = go.Scatter(
        x=x,
        y=y2,
        line=dict(color='rgb(0,176,246)'),
        mode='lines',
        name='Premium',
    )
    trace6 = go.Scatter(
        x=x,
        y=y3,
        line=dict(color='rgb(231,107,243)'),
        mode='lines',
        name='Ideal',
    )

    data = [trace1, trace2, trace3, trace4, trace5, trace6]

    layout = go.Layout(
        paper_bgcolor='rgb(255,255,255)',
        plot_bgcolor='rgb(229,229,229)',
        xaxis=dict(
            gridcolor='rgb(255,255,255)',
            range=[1,10],
            showgrid=True,
            showline=False,
            showticklabels=True,
            tickcolor='rgb(127,127,127)',
            ticks='outside',
            zeroline=False
        ),
        yaxis=dict(
            gridcolor='rgb(255,255,255)',
            showgrid=True,
            showline=False,
            showticklabels=True,
            tickcolor='rgb(127,127,127)',
            ticks='outside',
            zeroline=False
        ),
    )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename= 'shaded_lines')

Plotting Inline
---------------
.. code-block:: python

    import plotly.offline as py
    import plotly.figure_factory as ff
    import pandas as pd

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")

    table = ff.create_table(df)
    py.iplot(table, filename='jupyter-table1')

.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    data = [go.Bar(x=df.School, y=df.Gap)]
    py.iplot(data, filename='jupyter-basic_bar')

.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    trace_women = go.Bar(x=df.School,
                      y=df.Women,
                      name='Women',
                      marker=dict(color='#ffcdd2'))

    trace_men = go.Bar(x=df.School,
                    y=df.Men,
                    name='Men',
                    marker=dict(color='#A2D5F2'))

    trace_gap = go.Bar(x=df.School,
                    y=df.Gap,
                    name='Gap',
                    marker=dict(color='#59606D'))

    data = [trace_women, trace_men, trace_gap]

    layout = go.Layout(title="Average Earnings for Graduates",
                    xaxis=dict(title='School'),
                    yaxis=dict(title='Salary (in thousands)'))

    fig = go.Figure(data=data, layout=layout)

    py.iplot(fig, filename='jupyter-styled_bar')

Plotting Interactive Maps
-------------------------
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    import pandas as pd

    mapbox_access_token = 'ADD YOUR TOKEN HERE'

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Nuclear%20Waste%20Sites%20on%20American%20Campuses.csv')
    site_lat = df.lat
    site_lon = df.lon
    locations_name = df.text

    data = [
        go.Scattermapbox(
            lat=site_lat,
            lon=site_lon,
            mode='markers',
            marker=dict(
                size=17,
                color='rgb(255, 0, 0)',
                opacity=0.7
            ),
            text=locations_name,
            hoverinfo='text'
        ),
        go.Scattermapbox(
            lat=site_lat,
            lon=site_lon,
            mode='markers',
            marker=dict(
                size=8,
                color='rgb(242, 177, 172)',
                opacity=0.7
            ),
            hoverinfo='none'
        )]


    layout = go.Layout(
        title='Nuclear Waste Sites on Campus',
        autosize=True,
        hovermode='closest',
        showlegend=False,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=38,
                lon=-94
            ),
            pitch=0,
            zoom=3,
            style='light'
        ),
    )

    fig = dict(data=data, layout=layout)

    py.iplot(fig, filename='jupyter-Nuclear Waste Sites on American Campuses')


3D Plotting
-----------
.. code-block:: python

    import plotly.offline as py
    import plotly.graph_objs as go

    import numpy as np

    s = np.linspace(0, 2 * np.pi, 240)
    t = np.linspace(0, np.pi, 240)
    tGrid, sGrid = np.meshgrid(s, t)

    r = 2 + np.sin(7 * sGrid + 5 * tGrid)  # r = 2 + sin(7s+5t)
    x = r * np.cos(sGrid) * np.sin(tGrid)  # x = r*cos(s)*sin(t)
    y = r * np.sin(sGrid) * np.sin(tGrid)  # y = r*sin(s)*sin(t)
    z = r * np.cos(tGrid)                  # z = r*cos(t)

    surface = go.Surface(x=x, y=y, z=z)
    data = [surface]

    layout = go.Layout(
        title='Parametric Plot',
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            )
        )
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='jupyter-parametric_plot')


Plot Controls & IPython widgets
-------------------------------
.. code-block:: python

    import plotly.offline as py
    import numpy as np

    data = [dict(
            visible = False,
            line=dict(color='00CED1', width=6),
            name = '𝜈 = '+str(step),
            x = np.arange(0,10,0.01),
            y = np.sin(step*np.arange(0,10,0.01))) for step in np.arange(0,5,0.1)]
    data[10]['visible'] = True

    steps = []
    for i in range(len(data)):
        step = dict(
            method = 'restyle',
            args = ['visible', [False] * len(data)],
        )
        step['args'][1][i] = True # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active = 10,
        currentvalue = {"prefix": "Frequency: "},
        pad = {"t": 50},
        steps = steps
    )]

    layout = dict(sliders=sliders)
    fig = dict(data=data, layout=layout)

    py.iplot(fig, filename='Sine Wave Slider')