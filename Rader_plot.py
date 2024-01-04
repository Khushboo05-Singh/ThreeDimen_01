import plotly.express as px
import pandas as pd
data=pd.DataFrame(dict(keys=[10,20,30,40],values=["Labour cost","Manufacturing cost","Promotion cost","selling cost"]))
figure=px.line_polar(data,r='keys',theta='values',line_close=True)
figure.update_traces(fill="toself")
figure.show()