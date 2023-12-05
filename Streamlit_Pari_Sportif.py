import streamlit as st
import statsmodels.api as sm
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn import neighbors
from sklearn import datasets

from statsmodels.graphics.gofplots import qqplot
from sklearn.tree import plot_tree,  export_graphviz, DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split , GridSearchCV, learning_curve, cross_val_score
from sklearn.metrics import RocCurveDisplay,precision_score,mean_absolute_error, mean_squared_error,f1_score,confusion_matrix , accuracy_score,classification_report, roc_curve, auc
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import mannwhitneyu, chi2_contingency
from sklearn.preprocessing import StandardScaler

st.title("Est-il possible de battre les algorithmes des bookmakerssur l’estimation des probabilités d’un joueur gagnant un match de Tennis ? ")
st.image("Image_Couv.jpg")



st.sidebar.title("Sommaire")
pages = ["Introduction","Présentation du jeu de données", "Analyse graphique et premières hypothèses", "Description des choix de pré-processing", "Classification et modélisation", "Interprétation et limites","Conclusion"]
page = st.sidebar.radio("Aller vers la page :", pages)

if page == pages[0] : 
    st.write("### Introduction")
    st.write("En 2021, le marché des paris en ligne a passé un nouveau cap en dépassant les 2 milliards de dollars de PBJ. Ce marché en pleine croissance attire de plus en plus grâce à sa numérisation permettant un rajeunissement du bassin de consommateurs, mais aussi par cet espoir de devenir riche en suivant son sport favori. Mais s’agit-il vraiment d’un doux rêve ? ")
    st.write("De prime abord nous serions tentés de répondre oui : selon 60 Millions de Consommateurs, en 2021, sur les 4,5 millions d’utilisateurs, 27 500 ont réussi à dégager un bénéfice de 1000 euros, soit moins de 1% des utilisateurs. Pour autant, parmi ces parieurs un grand nombre semble inexpérimenté, peut faire ses choix par supportérisme, voire seulement pour s’amuser dans une consommation comparable au casino.")
    st.write("Mais en observant ces influenceurs et consultants en paris en ligne, florissant sur les réseaux sociaux, nous sommes tentés d’imaginer qu’il existe bel et bien des stratégies pour battre les bookmakers.A l’aide d’un jeu de données regroupant l’ensemble des matchs de tennis masculins entre 2000 et 2018. Nous allons tenter de créer une probabilité de confiance supérieure à celle des sites de paris en ligne. ")

elif page == pages[1] :
     st.write("### Présentation du jeu de données")
     st.write("Notre Dataset (disponible sur [Kaggle](https://www.kaggle.com/edouardthomas/atp-matches-dataset)) est constitué des résultats de tous les matchs de Tennis professionnels du cisrcuit ATP entre 2000 et 2018. Il composé de 44 708 lignes (= résultats de match) et de 23 variables. ")

elif page == pages[2] :
     st.write("### Analyse graphique et premières hypothèses")

elif page == pages[3] :
     st.write("### Description des choix de pré-processing")

elif page == pages[4] :
     st.write("### Classification et modélisation")

elif page == pages[5] :
     st.write("### Interprétation et limites")

elif page == pages[6] :
     st.write("### Conclusion")
