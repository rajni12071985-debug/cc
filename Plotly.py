import matplotlib.pyplot as plt
import plotly.express as px

import plotly.graph_objects as go



x = [1,2,3,4,5,6,7,8,9,10]
y= [7,2,4,5,3,1,2,7,8,9]

 

#fig = px.line(x = x , y = y , title ="line graph")

#fig.show()


fig= go.Figure (go.Scatter(x=x , y=y))

fig.show()

