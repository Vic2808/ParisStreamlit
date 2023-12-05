import streamlit as st
import pandas as pd
import pickle

# Charger les données d'entraînement (à adapter selon tes données)
atp_clean = pd.read_csv("atp_clean2.csv")
atp_pred = pd.read_csv("atp_pred_clean.csv")

# Charger les modèles depuis les fichiers pickle
picklefile1 = open('DTC_model.pkl', 'rb')
model1 = pickle.load(picklefile1)
picklefile2 = open('KNN1_model.pkl', 'rb')
model2 = pickle.load(picklefile2)
picklefile3 = open('LR_model.pkl', 'rb')
model3 = pickle.load(picklefile3)

# Sidebar avec les options
st.sidebar.title("Sommaire")
pages = ["Titre", "Modelisation", "Conclusion"]
page = st.sidebar.radio("Aller vers la page :", pages)

if page == pages[0]:
    st.title("Est-il possible de battre les algorithmes des bookmakers sur l’estimation des probabilités d’un joueur gagnant un match de Tennis ?")
    st.image("Image_Couv.jpg")

elif page == pages[1]:
    st.title("Quelles sont les prédictions de vainqueur de notre modèle ?")
    st.write("Nous avons décidé de tester notre modèle de prédiction sur le tournoi BNP Paribas OPEN 2018 d'Indian Wells, qui suit chronologiquement le dernier tournoi de notre Dataset d'entraînement.")
    st.image("sddefault.jpg")
    st.subheader("Random Forest Classifier App")

    # Charger les données pour les prédictions
    df_pred = atp_pred  # Adapter si nécessaire selon la structure du fichier atp_pred_clean.csv

    # Affichage des prédictions pour chaque match
    for index, row in df_pred.iterrows():
        selected_match_data = row[['id_1', 'Rank_1', 'elo_1', 'id_2', 'Rank_2', 'elo_2']]  # Adapter aux caractéristiques utilisées par les modèles

        # Utilisation des modèles pour la prédiction
        prediction1 = model1.predict(selected_match_data.values.reshape(1, -1))
        prediction2 = model2.predict(selected_match_data.values.reshape(1, -1))
        prediction3 = model3.predict(selected_match_data.values.reshape(1, -1))

        # Affichage des prédictions en fonction des modèles
        st.subheader("Prediction:")
        st.write(f"Prédiction du modèle 1 : {prediction1}")
        st.write(f"Prédiction du modèle 2 : {prediction2}")
        st.write(f"Prédiction du modèle 3 : {prediction3}")

elif page == pages[2]:
    st.title('Conclusion :')
    st.subheader("Analyse des résultats")
    st.markdown(
        """
        - **64** matchs sur 93 prédits correctement
        - Un ROI de **16%**
        - Le Random Forest, modèle le **plus efficace**
        """
    )
    tableau = Image.open('tab_concu.png')
    st.image(tableau)
    st.subheader('Comment améliorer encore le modèle ?')
    st.markdown(
        """
        Apport de données concernant : 
        - le **jeu d'un joueur** (aces, fautes directes, pourcentage de victoires...)
        - le **contexte du match** (face à face, météo, blessure...)
        """
    )
    st.write('Appliquer une **randomisation** à Joueur 1 et Joueur 2 pour éviter un biais.')
