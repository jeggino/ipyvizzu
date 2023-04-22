# import streamlit, pandas and ipyvizzu
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Data, Config, Style, Chart
from ipyvizzustory import Story, Slide, Step
import pathlib
import shutil
from bs4 import BeautifulSoup
import ssl
import streamlit as st 

import pandas as pd

from ipyvizzu import Chart, Data, Config, Style



data_frame = pd.read_csv(

    "https://ipyvizzu.vizzuhq.com/0.15/assets/data/chart_types_eu_data_14.csv",

    dtype={"Year": str, "Timeseries": str},

)

data = Data()

data.add_data_frame(data_frame)



chart = Chart()

chart.animate(data)

chart.animate(

    Config(

	{

	    "channels": {

		"x": "Year",

		"y": ["Value 2 (+)", "Country"],

		"color": "Country",

	    },

	    "title": "Stacked Area Chart",

	    "geometry": "area",

	}

    )

)



chart.animate(

    Config({"title": "100% Stacked Area Chart", "align": "stretch"})

)



chart.animate(

    Config(

	{

	    "channels": {"y": {"range": {"max": "100%"}}},

	    "title": "Split Area Chart",

	    "align": "min",

	    "split": True,

	}

    )

)





# display Chart



html(chart, width=650, height=370)
