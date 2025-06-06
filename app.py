import streamlit as st
from scripts.load_data import load_data
from scripts.data_processor import melt_data, plot_temporal_trends, plot_geographical_distribution, plot_summary_metrics

# Charger les données
confirmed, deaths, recovered = load_data()

# Transformer les données pour l'analyse temporelle
confirmed_melted, deaths_melted, recovered_melted = melt_data(confirmed, deaths, recovered)

# Interface Streamlit
st.title("COVID-19 Data Analysis")

# Sélection des pays
countries = confirmed["Country/Region"].unique()
selected_countries = st.multiselect("Select Countries", countries, default=["France", "Italy", "Germany"])

# Filtrer les données pour les pays sélectionnés
confirmed_filtered = confirmed_melted[confirmed_melted["Country/Region"].isin(selected_countries)]

# Mise en page avec colonnes
col1, col2 = st.columns(2)

with col1:
    # Carte choroplèthe interactive
    st.header("Geographical Distribution")
    fig_choropleth = plot_geographical_distribution(confirmed)
    st.plotly_chart(fig_choropleth, use_container_width=True)

with col2:
    # Graphique des tendances temporelles
    st.header("Temporal Trends of Confirmed Cases")
    fig_trends = plot_temporal_trends(confirmed_filtered, selected_countries)
    st.pyplot(fig_trends)

# Statistiques résumées sous forme de métriques ou de jauges
st.header("Summary Statistics")
plot_summary_metrics(confirmed, deaths, recovered, selected_countries)
