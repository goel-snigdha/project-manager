import pandas as pd
import plotly.express as px
import streamlit as st

# Load the CSV file into a DataFrame
df = pd.read_csv('activities.csv')

# Ensure the 'Delay' column is numeric
df['Delay'] = pd.to_numeric(df['Delay'], errors='coerce')

# Pivot the DataFrame to have projects as columns and activities as rows
heatmap_data = df.pivot_table(index='Activity', columns='Project', values='Delay', aggfunc='mean').reset_index()

# Melt the DataFrame to long format for Plotly Express
# heatmap_data_melted = heatmap_data.melt(id_vars='Activity', var_name='Project', value_name='Delay')

# Create the heatmap with Plotly Express
fig = px.imshow(
    heatmap_data.set_index('Activity'),
    color_continuous_scale='RdYlGn_r',
    labels={'color': 'Delay (days)'},
    aspect='auto'
)

# Add titles and labels
fig.update_layout(
    title='Project Activity Delays Heatmap',
    xaxis_title='Project',
    yaxis_title='Activity'
)

# Rotate x-axis labels if needed
fig.update_xaxes(tickangle=45)

# Display the heatmap full-screen in the Streamlit app
st.set_page_config(layout="wide")
fig.update_layout(height=700)
st.plotly_chart(fig, use_container_width=True, height=700)