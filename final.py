import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
# TRL_987

student_df=df.loc[df["student_id"] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    y=student_df.groupby("level")["attempt"].mean(),
    x=["level 1", "level 2", "level 3", "level 4 "],
    orientation="v"
))
fig.show()