import pandas as pd
import plotly.express as px

# Read dataset
data = pd.read_csv("sales.csv")

# Display dataset
print("Dataset:")
print(data)

# Create bar chart
fig = px.bar(
    data,
    x="Month",
    y="Sales",
    title="Monthly Sales"
)

# Display chart
fig.show()