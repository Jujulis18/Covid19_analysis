import streamlit as st
from scripts.data_loader import load_data
from scripts.data_processor import melt_data, process_data, plot_temporal_trends, plot_geographical_distribution, plot_comparison, display_summary_statistics, plot_new_cases_analysis

# Charger les données
confirmed, deaths, recovered = load_data()

# Transformer les données pour l'analyse temporelle
confirmed_melted, deaths_melted, recovered_melted = melt_data(confirmed, deaths, recovered)

# Interface Streamlit
st.title("COVID-19 Data Analysis")

# Sélection des pays
countries = confirmed["Country/Region"].unique()
selected_countries = st.multiselect("Select Countries", countries, default=["France", "Italy", "Germany"])

# Filtrer et traiter les données pour les pays sélectionnés
confirmed_filtered, deaths_filtered, recovered_filtered = process_data(
    confirmed_melted, deaths_melted, recovered_melted, selected_countries
)

# Graphique des tendances temporelles
st.header("Temporal Trends of Confirmed Cases")
fig_trends = plot_temporal_trends(confirmed_filtered, selected_countries)
st.pyplot(fig_trends)

# Carte choroplèthe interactive
st.header("Geographical Distribution of Confirmed Cases")
fig_map = plot_geographical_distribution(confirmed)
st.plotly_chart(fig_map)

# Comparaison des données
st.header("Data Comparison")
fig_comparison = plot_comparison(confirmed, deaths, recovered, selected_countries)
st.plotly_chart(fig_comparison)

# Statistiques résumées
st.header("Summary Statistics")
confirmed_count, deaths_count, recovered_count = display_summary_statistics(confirmed, deaths, recovered, selected_countries)
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

# Analyse des nouveaux cas
st.header("New Cases Analysis")
fig_new_cases = plot_new_cases_analysis(confirmed_filtered, selected_countries)
st.pyplot(fig_new_cases)
