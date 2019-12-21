########################################## Host plotly on webiste ###############################################
# https://towardsdatascience.com/how-to-create-a-plotly-visualization-and-embed-it-on-websites-517c1a78568b

# Install chart studio
!pip install chart_studio
import chart_studio.plotly as py
import plotly.io as pio
import chart_studio.tools as tls


# Generate chart
gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
fig.show()

# Access plotly chart studio
username = 'gloriazxl0204' # your username
api_key = 'sF3FeGwnGcd7EohLNXtS' # your api key - go to profile > settings > regenerate key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

# Save the chart on chart studio
py.plot(fig, filename = 'gdp_per_cap', auto_open=True)

# After the step above, a webpage will pop up: https://plot.ly/~gloriazxl0204/1/#/
# The last step is: go to Medium, copy paste the http link above, tada!


# The following are optional. The goal is to generate an html file and upload to github.
pio.write_html(fig, file='index.html', auto_open=True)

tls.get_embed('https://plot.ly/~gloriazxl0204/1/#/') #change to your url
# auto pop up: '<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~gloriazxl0204/1.embed" height="525" width="100%"></iframe>'
# In the medium article, it says use this embeb in the blog site. But for me, using the http link works.

# My plotly chart studio: https://chart-studio.plot.ly/organize/home/


