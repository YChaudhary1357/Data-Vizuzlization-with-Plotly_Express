import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import pandas as pd
import numpy as np

#Task 1: Loading the Data

import plotly.express as px
from plotly.figure_factory import create_table

#Task 2: Quick Visualizations with Custom Bar Charts

gapminder=px.data.gapminder()
table=create_table(gapminder.head(10))
py.iplot(table)

#Task 3: Plot Life Expectancy vs GDP per Capita

data_canada=px.data.gapminder().query("country=='Canada'")
fig=px.bar(data_canada,x='year',y='pop',height=400)
fig.show()

#Task 4: Customize Interactive Bubble Charts

fig=px.bar(data_canada,x='year',y='pop',
           hover_data=['lifeExp','gdpPercap'],
           color='lifeExp',
           labels={'pop':'population of Canada'},height=400)
fig.show()

#Task 5: Create Interactive Animations and Facet Plots

gapminder2007= gapminder.query('year==2007')
px.scatter(gapminder2007,x='gdpPercap',y='lifeExp')

#Task 6: Represent Geographic Data as Animated Maps

px.scatter(gapminder2007,x='gdpPercap',y='lifeExp',color='continent')

px.scatter(gapminder2007,x='gdpPercap',y='lifeExp',color='continent',size='pop',
          size_max=60)

px.scatter(gapminder2007,x='gdpPercap',y='lifeExp',color='continent'
          ,size='pop',size_max=60,hover_name='country')

px.scatter(gapminder2007,x='gdpPercap',y='lifeExp',color='continent'
          ,size='pop',size_max=60,hover_name='country',facet_col='continent',log_x=True)

px.scatter(gapminder,x='gdpPercap',y='lifeExp',color='continent',
          size='pop',size_max=60,hover_name='country',animation_frame='year',
           animation_group='country',log_x=True,range_x=[100,100000],range_y=[25,90],
           labels=dict(pop='Population',gdpPercap='gdp Per capita',lifeExp='Life Expectancy'))

px.choropleth(gapminder,locations='iso_alpha',color='lifeExp',hover_name='country',
             animation_frame='year',color_continuous_scale=px.colors.sequential.Plasma,
             projection='natural earth')

px.choropleth(gapminder,locations='iso_alpha',color='lifeExp',hover_name='country',
             animation_frame='year',color_continuous_scale=px.colors.sequential.Plasma,
             projection='orthographic')

