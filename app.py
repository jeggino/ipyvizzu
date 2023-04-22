# import streamlit, pandas and ipyvizzu
from streamlit.components.v1 import html
import streamlit as st 
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
 
 
data_frame = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/0.15/showcases/music/music.csv",
    dtype={"Year": str},
)
data = Data()
data.add_data_frame(data_frame)
 
chart = Chart()
 
chart.animate(data)
 
chart.animate(
    Config(
        {
            "x": "Year",
            "y": ["Format", "Revenue [m$]"],
            "color": "Format",
            "geometry": "area",
            "align": "center",
            "title": "Music Revenue by Format 1973-2020",
        }
    ),
    Style(
        {
            "plot": {
                "xAxis": {"label": {"fontSize": 9, "angle": 2.0}},
                "marker": {
                    "colorPalette": "#b74c20FF #c47f58FF #1c9761FF"
                    + " #ea4549FF #875792FF #3562b6FF"
                    + " #ee7c34FF #efae3aFF"
                },
            }
        }
    ),
)
 
chart.animate(
    Config(
        {
            "align": "stretch",
            "title": "Music Revenue by Format 1973-2020(%)",
        }
    ),
    delay=1,
)
 
chart.animate(
    Config(
        {
            "align": "center",
            "title": "Music Revenue by Format 1973-2020",
        }
    ),
    delay=1,
)
 
chart.animate(Config({"split": True}), delay=1)
 
chart.animate(
    Data.filter(
        "record.Format == 'Vinyl' ||record.Format == 'Streaming'"
    ),
    Config({"title": "Revenue of Vinyl & Streaming 1973-2020"}),
    delay=1,
)
 
chart.animate(
    Data.filter(None),
    Config(
        {"title": "Music Revenue by Format 1973-2020", "split": False}
    ),
    delay=1,
)
 
chart.animate(
    Config(
        {
            "x": "Year",
            "y": "Revenue [m$]",
            "noop": "Format",
            "align": "none",
            "geometry": "line",
        }
    ),
    delay=1,
)
 
html(chart._repr_html_())
