import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def melt_data(confirmed, deaths, recovered):
    confirmed_melted = confirmed.melt(id_vars=confirmed.columns[:4], var_name="Date", value_name="Count")
    deaths_melted = deaths.melt(id_vars=deaths.columns[:4], var_name="Date", value_name="Count")
    recovered_melted = recovered.melt(id_vars=recovered.columns[:4], var_name="Date", value_name="Count")

    for df in [confirmed_melted, deaths_melted, recovered_melted]:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

    return confirmed_melted, deaths_melted, recovered_melted

def process_data(confirmed_melted, deaths_melted, recovered_melted, selected_countries):
    confirmed_filtered = confirmed_melted[confirmed_melted["Country/Region"].isin(selected_countries)]
    deaths_filtered = deaths_melted[deaths_melted["Country/Region"].isin(selected_countries)]
    recovered_filtered = recovered_melted[recovered_melted["Country/Region"].isin(selected_countries)]

    return confirmed_filtered, deaths_filtered, recovered_filtered

def plot_temporal_trends(data, selected_countries):
    fig, ax = plt.subplots(figsize=(14, 7))
    for country in selected_countries:
        country_data = data[data["Country/Region"] == country]
        ax.plot(country_data["Date"], country_data["Count"], label=country)
    ax.set_title("COVID-19 Confirmed Cases Over Time by Country")
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

def plot_comparison(confirmed, deaths, recovered, selected_countries):
    comparison_data = pd.DataFrame({
        'Country': selected_countries,
        'Total Confirmed': [confirmed[confirmed["Country/Region"] == country].iloc[:, -1].sum() for country in selected_countries],
        'Total Deaths': [deaths[deaths["Country/Region"] == country].iloc[:, -1].sum() for country in selected_countries],
        'Total Recovered': [recovered[recovered["Country/Region"] == country].iloc[:, -1].sum() for country in selected_countries]
    })

    fig = px.bar(comparison_data, x='Country', y=['Total Confirmed', 'Total Deaths', 'Total Recovered'],
                 title='Comparison of COVID-19 Statistics by Country', barmode='group')
    return fig

def display_summary_statistics(confirmed, deaths, recovered, selected_countries):
    for country in selected_countries:
        confirmed_count = confirmed[confirmed["Country/Region"] == country].iloc[:, -1].sum()
        deaths_count = deaths[deaths["Country/Region"] == country].iloc[:, -1].sum()
        recovered_count = recovered[recovered["Country/Region"] == country].iloc[:, -1].sum()

        st.subheader(country)
        st.write(f"Total Confirmed Cases: {confirmed_count}")
        st.write(f"Total Deaths: {deaths_count}")
        st.write(f"Total Recovered: {recovered_count}")
        if deaths_count > 0:
            mortality_rate = (deaths_count / confirmed_count) * 100
            st.write(f"Mortality Rate: {mortality_rate:.2f}%")
        if recovered_count > 0:
            recovery_rate = (recovered_count / confirmed_count) * 100
            st.write(f"Recovery Rate: {recovery_rate:.2f}%")

def plot_new_cases_analysis(data, selected_countries):
    for country in selected_countries:
        country_data = data[data["Country/Region"] == country].copy()
        country_data['New Cases'] = country_data['Count'].diff().fillna(0)
        st.subheader(country)
        fig, ax = plt.subplots(figsize=(14, 3))
        ax.bar(country_data["Date"], country_data["New Cases"], color='orange', alpha=0.6)
        ax.set_title("Daily New Cases")
        ax.set_xlabel("Date")
        ax.set_ylabel("Number of New Cases")
    return fig
