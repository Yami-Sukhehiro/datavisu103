from google.colab import files 
dataupload = files.upload()
import pandas as pd
import plotly.express as px
df  = pd.read_csv("datawut.csv")
fig = px.scatter(df, x= "date", y= "cases", color = "country" )
fig.show()