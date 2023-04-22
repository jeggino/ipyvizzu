import pandas as pd
import streamlit as st

from streamlit_vizzu import Config, Data, Style, VizzuChart

data_frame = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/0.15/assets/data/infinite_data.csv",
    dtype={"Year": str, "Timeseries": str},
)
data = Data()
data.add_data_frame(data_frame)


chart = VizzuChart(height=360)

chart.animate(data)
chart.feature("tooltip", True)

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

    )

)
    
output = chart.show()

st.multiselect(
    "Products",
    ["Shoes", "Handbags", "Gloves", "Accessories"],
    ["Shoes", "Handbags", "Gloves", "Accessories"],
    key="items",
)

col1, col2, col3, col4, col5 = st.columns(5)

measure: str = col1.radio(  # type: ignore
    "Measure",
    ["Sales", "Revenue [$]"],
    key="measure",
)
compare_by = col2.radio("Compare by", ["Product", "Region", "Both"], key="compare_by")
coords = col3.radio(
    "Coordinate system", ["Cartesian (desktop)", "Polar (mobile)"], key="coords"
)
order = col4.radio("Order items", ["Alphabetically", "By value"], key="order")

bg_color = col5.color_picker("Background color", "#fff", key="bg_color")
