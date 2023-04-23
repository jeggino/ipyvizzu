from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
 
 

# initialize Chart

chart = Chart(display=DisplayTarget.MANUAL)

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
 
# chart.animate(
#     Config(
#         {
#             "channels": {
#                 "x": [
#                     "Value 1",
#                     "Joy factors",
#                     "Region",
#                     "Country code",
#                 ],
#                 "label": None,
#             }
#         }
#     ),
#     duration="500ms",
# )
 
# chart.animate(
#     Config(
#         {
#             "channels": {
#                 "x": [
#                     "Value 1",
#                     "Joy factors",
#                     "Region",
#                     "Country code",
#                 ],
#                 "y": {"set": "Value 3", "range": {"min": "-60%"}},
#             },
#             "title": "Coxcomb Chart",
#         }
#     )
# )

chart.feature("tooltip", True) 
# generate Chart's html code
 
CHART = chart._repr_html_()
 
 
# display Chart
 
html(CHART, width=650, height=370)


import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import geopandas as gpd

option = st.selectbox('Select a dataset',('df_1', 'df_2', 'gdf_1'))

if option == "df_1":
 df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")

elif option == "df_2":
 df = pd.read_csv("https://ipyvizzu.vizzuhq.com/0.15/assets/data/infinite_data.csv", dtype={"Year": str, "Timeseries": str},)

elif option == "gdf_1":
 gdf = gpd.read_file("https://maps.amsterdam.nl/open_geodata/geojson_lnglat.php?KAARTLAAG=FUNCTIEMIX&THEMA=functiemix")
 df = pd.DataFrame(gdf.drop(columns='geometry'))

 
AgGrid(df,  allow_unsafe_jscode=True, height=500, theme='alpine')
st_profile_report(df.profile_report())
