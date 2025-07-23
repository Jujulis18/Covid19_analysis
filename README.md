# Dashboard d'Analyse COVID-19

## Contexte

Dans un monde où la pandémie de COVID-19 a eu un impact significatif sur la santé publique, il est crucial de visualiser et de comprendre les données pour prendre des décisions éclairées. Ce projet vise à fournir une plateforme interactive pour explorer les données de COVID-19 de manière intuitive et informative.

**Le défi ?** Présenter des données complexes de manière accessible et interactive pour le grand public.

## Objectifs

L'idée est de créer un outil qui permet de comparer les tendances de COVID-19 entre différents pays et de visualiser la distribution géographique des cas.

Objectifs principaux :
- Visualiser les tendances temporelles des cas confirmés
- Comparer les statistiques entre différents pays
- Afficher la distribution géographique des cas

Objectifs secondaires :
- Fournir une interface utilisateur simple et intuitive
- Permettre une exploration interactive des données

## Méthodologie

Pour réaliser ce projet, j'ai suivi les étapes suivantes :
1. Collecte des données COVID-19 depuis Kaggle
2. Nettoyage et préparation des données pour l'analyse
3. Création de visualisations interactives avec Plotly et Matplotlib
4. Développement d'une interface utilisateur avec Streamlit

**Outils et technologies utilisés** :
- Pandas : Manipulation et analyse des données
- Plotly, Matplotlib : Visualisation des données
- Streamlit : Interface utilisateur web [Streamlit Dashboard](https://hzrhzpkmdekqmy32ygbi4v.streamlit.app/)


## Analyse et Résultats

- **Analyse des données COVID-19** :
  - Statistiques descriptives : Distribution des cas confirmés, décès et guérisons
  - Visualisations : Graphiques temporels, cartes choroplèthes

- **Résultats obtenus** :
  - Visualisation interactive des tendances temporelles
  - Comparaison des statistiques entre pays sélectionnés
  - Carte géographique interactive des cas confirmés

## Impact Business

- **Valeur ajoutée** :
  - Amélioration de la compréhension des tendances de COVID-19

- **Prochaines pistes** :
  - Intégration de données de vaccination
  - Amélioration des visualisations avec des graphiques plus avancés

## Conclusion

Ce projet m'a permis de combiner mes compétences en analyse de données et en visualisation pour créer un outil utile dans le contexte de la pandémie de COVID-19. Il m'a aussi rappelé l'importance de la visualisation des données pour rendre l'information accessible et compréhensible.

- **Leçons apprises** :
  - Importance de la visualisation interactive pour l'exploration des données
  - Utilité des outils comme Streamlit pour créer des applications web rapidement
  - Nécessité de nettoyer et préparer les données avant l'analyse

## 🚀 Comment démarrer

1. Clonez le dépôt
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```
3. Lancez le dashboard :
```bash
streamlit run app.py
```

## Références et Liens

- **Sources de données** :
  - [COVID-19 Dataset raw]("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")