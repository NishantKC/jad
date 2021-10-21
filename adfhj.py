import pandas as pd
data =pd.read_csv("data.csv")
import plotly.figure_factory as ff
fig=ff.create_distplot([data["Avg Rating"].tolist()],["fhs"],show_hist=False)
fig.show()