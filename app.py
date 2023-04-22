from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
 
 

# initialize Chart

chart = Chart(
    width="640px", height="360px", display=DisplayTarget.MANUAL
)

# create and add data to Chart

data = Data()
data_frame = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/0.15/assets/data/infinite_data.csv",
    dtype={"Year": str, "Timeseries": str},
)
data.add_data_frame(data_frame)

chart.animate(data)

# add config to Chart

chart.animate(
    Config(
        {
            "channels": {
                "x": ["Value 1", "Joy factors"],
                "color": "Joy factors",
                "label": "Value 1",
            },
            "title": "Pie Chart",
            "coordSystem": "polar",
        }
    )
)
 
chart.animate(
    Config(
        {
            "channels": {
                "x": [
                    "Value 1",
                    "Joy factors",
                    "Region",
                    "Country code",
                ],
                "label": None,
            }
        }
    ),
    duration="500ms",
)
 
chart.animate(
    Config(
        {
            "channels": {
                "x": [
                    "Value 1",
                    "Joy factors",
                    "Region",
                    "Country code",
                ],
                "y": {"set": "Value 3", "range": {"min": "-60%"}},
            },
            "title": "Coxcomb Chart",
        }
    ),
    playState="paused",
    position=0.5,
)

chart.feature("tooltip", True) 
# generate Chart's html code
 
CHART = chart._repr_html_()
 
 
# display Chart
 
html(CHART, width=650, height=370)
