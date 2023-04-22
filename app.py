# import streamlit, pandas and ipyvizzu
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Data, Config, Style
from ipyvizzustory import Story, Slide, Step
import pathlib
import shutil
from bs4 import BeautifulSoup
import ssl
import streamlit as st 





def create_chart():

    # initialize Chart



    chart = Chart(

	width="640px", height="360px", display=DisplayTarget.MANUAL

    )



    # create and add data to Chart



    data = Data()

    data_frame = pd.read_csv(

	"https://ipyvizzu.vizzuhq.com/0.15/showcases/titanic/titanic.csv"

    )

    data.add_data_frame(data_frame)



    chart.animate(data)



    # add config to Chart



    chart.animate(

	Config(

	    {

		"x": "Count",

		"y": "Sex",

		"label": "Count",

		"title": "Passengers of the Titanic",

	    }

	)

    )

    chart.animate(

	Config(

	    {

		"x": ["Count", "Survived"],

		"label": ["Count", "Survived"],

		"color": "Survived",

	    }

	)

    )

    chart.animate(Config({"x": "Count", "y": ["Sex", "Survived"]}))



    # add style to Chart



    chart.animate(Style({"title": {"fontSize": 35}}))



    # return generated html code



    return chart._repr_html_()





# generate Chart's html code



CHART = create_chart()





# display Chart



html(CHART, width=650, height=370)
