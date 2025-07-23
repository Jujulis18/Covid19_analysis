import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


def melt_data(confirmed, deaths, recovered):
    confirmed_melted = confirmed.melt(id_vars=confirmed.columns[:4], var_name="Date", value_name="Count")
    deaths_melted = deaths.melt(id_vars=deaths.columns[:4], var_name="Date", value_name="Count")
    recovered_melted = recovered.melt(id_vars=recovered.columns[:4], var_name="Date", value_name="Count")

    for df in [confirmed_melted, deaths_melted, recovered_melted]:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

    return confirmed_melted, deaths_melted, recovered_melted

def plot_temporal_trends(data, selected_countries):
    fig, ax = plt.subplots(figsize=(10, 5))
    for country in selected_countries:
        country_data = data[data["Country/Region"] == country]
        ax.plot(country_data["Date"], country_data["Count"], label=country)
    ax.set_title("COVID-19 Confirmed Cases Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Confirmed Cases")
    ax.legend()
    ax.grid(True)
    return fig

def plot_geographical_distribution(data):
    latest_data = data.iloc[:, -1]
    data['Latest Confirmed'] = latest_data
    country_data = data.groupby('Country/Region')['Latest Confirmed'].sum().reset_index()

    fig = px.choropleth(country_data,
                        locations="Country/Region",
                        locationmode='country names',
                        color="Latest Confirmed",
                        hover_name="Country/Region",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="Global Distribution of COVID-19 Confirmed Cases")
    return fig

def plot_summary_metrics(confirmed, deaths, recovered, selected_countries):
    for country in selected_countries:
        confirmed_count = confirmed[confirmed["Country/Region"] == country].iloc[:, -1].sum()
        deaths_count = deaths[deaths["Country/Region"] == country].iloc[:, -1].sum()
        recovered_count = recovered[recovered["Country/Region"] == country].iloc[:, -1].sum()

        st.subheader(country)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Confirmed", confirmed_count)
        col2.metric("Total Deaths", deaths_count)
        col3.metric("Total Recovered", recovered_count)

        if deaths_count > 0:
            mortality_rate = (deaths_count / confirmed_count) * 100
            st.progress(mortality_rate, text=f"Mortality Rate: {mortality_rate:.2f}%")

        if recovered_count > 0:
            recovery_rate = (recovered_count / confirmed_count) * 100
            st.progress(recovery_rate, text=f"Recovery Rate: {recovery_rate:.2f}%")
