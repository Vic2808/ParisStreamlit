import streamlit as st
import pandas as pd
import pickle
from lib2to3.pgen2.pgen import DFAState
import numpy as np
from PIL import Image


atp_clean=pd.read_csv("atp_clean2.csv")
atp_pred=pd.read_csv("atp_pred_clean.csv")
atp_pred2=pd.read_csv("atp_pred2.csv")

st.sidebar.title("Sommaire")
pages = ["Accueil","Modelisation","Conclusion"]
page = st.sidebar.radio("Aller vers la page :", pages)

if page == pages[0] : 
    st.title("Est-il possible de battre les algorithmes des bookmakers sur l'estimation des probabilités d'un joueur gagnant un match de Tennis ? ")
    st.image("Image_Couv.jpg")

if page == pages[1] :    
    st.title("Quelle sont les prédiction de vainqueur de nos modèles ?")
    st.write("Nous avons décidé de tester nos modèles de prédiction sur le tournoi BNP Paribas OPEN 2018 d'Indian Wells, qui suit chronologiquement le dernier tournoi de notre Dataset d'entrainement.")
    st.image("sddefault.jpg")
    st.subheader("Choix d'un joueur, d'un match et d'un modèle de prédiction")
 
    df = atp_pred2

    picklefile = open('rf_model_RF2.pkl', 'rb')
    model = pickle.load(picklefile)
    picklefile1 = open('DTC_model.pkl', 'rb')
    model1 = pickle.load(picklefile1)
    picklefile2 = open('KNN1_model.pkl', 'rb')
    model2 = pickle.load(picklefile2)
    picklefile3 = open('LR_model.pkl', 'rb')
    model3 = pickle.load(picklefile3)

    choix_model = [model, model1, model2, model3]
  
    liste_joueurs =[]
    nom_joueur = 0

    for i in range(0, len(df)):
        joueur = df.iloc[i, 7]
        if joueur not in liste_joueurs :
            liste_joueurs.append(joueur)
        joueurb = df.iloc[i, 11]
        if joueurb not in liste_joueurs :
            liste_joueurs.append(joueurb)
  
    liste_joueurs.sort()

    option_joueur = st.selectbox('Sélectionnez votre joueur', liste_joueurs)

    if option_joueur != "" :
        df_joueur = df.loc[(df["Joueur_1"] == option_joueur) | (df["Joueur_2"] == option_joueur)]
        choix_match =[]
        for i in range(0, len(df_joueur)) :
            string = f"{df_joueur.iloc[i, 5]} - {df_joueur.iloc[i, 7]} vs {df_joueur.iloc[i, 11]}"
            choix_match.append(string)
        option_match = st.selectbox("Sélectionnez votre match", choix_match)
        option_match_index = choix_match.index(option_match)
        index_selected_row = df_joueur.index[option_match_index]
        forecast = df_joueur.iloc[option_match_index]
        forecast = forecast[['PS_1','PS_2','elo_1','elo_2','id_1','id_2','Rank_1','Rank_2']]
        joueur_1 = df_joueur.iloc[option_match_index]['Joueur_1']
        joueur_2 = df_joueur.iloc[option_match_index]['Joueur_2'] 
        resultat = df_joueur.iloc[option_match_index]['Victoire_J1']            

    modelf=st.selectbox("Sélectionnez le modèle de prédiction", choix_model)
    forecast = atp_pred.iloc[index_selected_row,:]

    input_data = pd.DataFrame({
        'id_1': [forecast['id_1']],
        'Rank_1': [forecast['Rank_1']],
        'elo_1': [forecast['elo_1']],
        'id_2': [forecast['id_2']],
        'Rank_2': [forecast['Rank_2']],
        'elo_2': [forecast['elo_2']],
        'PS_1': [forecast['PS_1']],
        'PS_2': [forecast['PS_2']],
        'Year': [forecast['Year']],
        'Month': [forecast['id_1']],
        'Series_ATP500': [forecast['Series_ATP500']],
        'Series_Grand_Slam': [forecast['Series_Grand_Slam']],
        'Series_Masters_1000': [forecast['Series_Masters_1000']],
        'Series_Masters_Cup': [forecast['Series_Masters_Cup']],
        'Surface_Clay': [forecast['Surface_Clay']],
        'Surface_Grass': [forecast['Surface_Grass']],
        'Surface_Hard': [forecast['Surface_Hard']],
        'Round_2nd_Round': [forecast['Round_2nd_Round']],
        'Round_3rd_Round': [forecast['Round_3rd_Round']],
        'Round_4th_Round': [forecast['Round_4th_Round']],
        'Round_Quarterfinals': [forecast['Round_Quarterfinals']],
        'Round_Round_Robin': [forecast['Round_Round_Robin']],
        'Round_Semifinals': [forecast['Round_Semifinals']],
        'Round_The_Final': [forecast['Round_The_Final']]
    })

    prediction = modelf.predict(input_data)

    st.subheader("Prediction:")
    if prediction[0] == 1:
        st.write(f"Je prédis que le joueur gagnant est {joueur_1} ")
    elif prediction[0] == 0:
        st.write(f"Je prédis que le joueur gagnant est {joueur_2}")

    if st.checkbox("Afficher le résultat réel"):
        if resultat == 1 and resultat == prediction:
            st.write(f"Le joueur qui a réellement gagné est {joueur_1} :white_check_mark:")
        if resultat == 1 and resultat != prediction:
            st.write(f"Le joueur qui a réellement gagné est {joueur_1} :x:") 
        if resultat == 0 and resultat == prediction:
            st.write(f"Le joueur qui a réellement gagné est {joueur_2}:white_check_mark: ")
        elif resultat == 0 and resultat != prediction:
            st.write(f"Le joueur qui a réellement gagné est {joueur_2} :x: ")
    
    
elif page == pages[2] :
    st.title('Conclusion :')
    st.write("Calculons notre ROI si nous parions 1€ sur le vainqueur de chacun des 93 matchs du BNP Paribas OPEN 2018 d'Indian Wells selon 4 stratégies différentes :")
    tableau = Image.open('tab_concu.png')
    st.image(tableau)
    st.subheader("Analyse des résultats")
    st.markdown(
    """
    - **64** matchs sur 93 prédits correctement (69%)
    - Un ROI de **16%** en pariant 1€ sur chaque match
    - Le Random Forest, modèle le **plus efficace**
    """  
    )

    st.markdown(
    """
    - Un tournoi particulier : 
        - Absence de Nadal (#1 Elo) et Murray (#5 Elo)
        - Djokovic revenant de blessure, sort au premier tour (#2 Elo)
    - Le favori selon les cotes des bookmakers ne tient pas compte des stratégies commerciales eventuelles (bonus, surcotes, etc..)
    """
    )
    



    st.subheader('Comment améliorer encore le modèle ?')
    st.markdown(
    """
    Apport de données concernant : 
    - le **jeu d'un joueur** (aces, fautes directes, pourcentage de victoires...)
    - le **contexte du match** (face à face, météo, blessure...)
    """
    )
    st.markdown(
    """
    Appliquer une **randomisation** à :
    - La définition du 'Joueur 1' et du 'Joueur 2'
    - L'attribution des 'Id_joueur'
    """
    )
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.subheader(
    """
    :blue[**Dans ce contexte nous pouvons dire que nous avons battu les bookmakers sur l'estimation des probabilités d'un joueur gagnant un match de tennis !**]
    """)