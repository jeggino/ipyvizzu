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


data_frame = pd.read_csv(
    "https://ipyvizzu.vizzuhq.com/0.15/assets/data/infinite_data.csv",
    dtype={"Year": str, "Timeseries": str},
)

keyword = st.text_input('choose keyword')
standards_df = data_frame[data_frame['Joy factors'].str.contains(keyword)]

# Display the DataFrame
gd=GridOptionsBuilder.from_dataframe(standards_df)
gd.configure_column("id", headerName="id", cellRenderer=JsCode('''function(params) {return '<a href="https://drive.google.com/file/d/' + params.value + '/view" target="_blank">' + params.value + '</a>'}'''),
                width=300)
gridoptions=gd.build()


AgGrid(standards_df, gridOptions=gridoptions, allow_unsafe_jscode=True, height=500, theme='alpine')



