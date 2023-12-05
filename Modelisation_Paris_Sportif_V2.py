import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from imblearn.over_sampling import RandomOverSampler


atp_clean=pd.read_csv("atp_clean2.csv")
atp_pred=pd.read_csv("atp_pred_clean.csv")
atp_pred2=pd.read_csv("atp_pred2.csv")

st.title("Random Forest Classifier App")

choix_joueur = ['Federer', 'Del Potro','Raonic','Coric']
option_joueur = st.selectbox('Sélectionnez votre joueur', choix_joueur)
df = atp_pred2

liste_joueurs =[]
nom_joueur = 0

for nom_joueur in df['Joueur_1']:
    joueur = df['Joueur_1']



if option_joueur == "Del Potro" :
    df_DelPotro = df.loc[(df["id_1"] == 24) | (df["id_2"] == 24)]
    choix_match =[]
    for i in range(0, len(df_DelPotro)) :
        string = f"{df_DelPotro.iloc[i, 5]} - {df_DelPotro.iloc[i, 7]} vs {df_DelPotro.iloc[i, 11]}"
        choix_match.append(string)
    option_match = st.selectbox("Sélectionnez votre match", choix_match)
    option_match_index = choix_match.index(option_match)
    index_selected_row = df_DelPotro.index[option_match_index]
    forecast = df_DelPotro.iloc[option_match_index]
    forecast = forecast[['PS_1','PS_2','elo_1','elo_2','id_1','id_2','Rank_1','Rank_2']]
    joueur_1 = df_DelPotro.iloc[option_match_index]['Joueur_1']
    joueur_2 = df_DelPotro.iloc[option_match_index]['Joueur_2'] 
    resultat = df_DelPotro.iloc[option_match_index]['Victoire_J1'] 

elif option_joueur == "Federer" :
    df_Federer = df.loc[(df["id_1"] == 0) | (df["id_2"] == 0)]
    choix_match = []
    for i in range(0, len(df_Federer)) :
        string = f"{df_Federer.iloc[i, 5]} - {df_Federer.iloc[i, 7]} vs {df_Federer.iloc[i, 11]}"
        choix_match.append(string)
    option_match = st.selectbox("Sélectionnez votre match", choix_match)
    option_match_index = choix_match.index(option_match)
    index_selected_row = df_Federer.index[option_match_index]
    forecast = df_Federer.iloc[option_match_index]
    forecast = forecast[['PS_1','PS_2','elo_1','elo_2','id_1','id_2','Rank_1','Rank_2']]
    joueur_1 = df_Federer.iloc[option_match_index]['Joueur_1']
    joueur_2 = df_Federer.iloc[option_match_index]['Joueur_2']  
    resultat = df_Federer.iloc[option_match_index]['Victoire_J1'] 


elif option_joueur == "Raonic" :
    df_Raonic = df.loc[(df["id_1"] == 51) | (df["id_2"] == 51)]
    choix_match = []
    for i in range(0, len(df_Raonic)) :
        string = f"{df_Raonic.iloc[i, 5]} - {df_Raonic.iloc[i, 7]} vs {df_Raonic.iloc[i, 11]}"
        choix_match.append(string)
    option_match = st.selectbox("Sélectionnez votre match", choix_match)
    option_match_index = choix_match.index(option_match)
    index_selected_row = df_Raonic.index[option_match_index]
    forecast = df_Raonic.iloc[option_match_index]
    forecast = forecast[['PS_1','PS_2','elo_1','elo_2','id_1','id_2','Rank_1','Rank_2']]
    joueur_1 = df_Raonic.iloc[option_match_index]['Joueur_1']
    joueur_2 = df_Raonic.iloc[option_match_index]['Joueur_2']
    resultat = df_Raonic.iloc[option_match_index]['Victoire_J1'] 


elif option_joueur == "Coric" :
    df_Coric = df.loc[(df["id_1"] == 177) | (df["id_2"] == 177)]
    choix_match = []
    for i in range(0, len(df_Coric)) :
        string = f"{df_Coric.iloc[i, 5]} - {df_Coric.iloc[i, 7]} vs {df_Coric.iloc[i, 11]}"
        choix_match.append(string)
    option_match = st.selectbox("Sélectionnez votre match", choix_match)
    option_match_index = choix_match.index(option_match)
    index_selected_row = df_Coric.index[option_match_index]
    forecast = df_Coric.iloc[option_match_index]
    forecast = forecast[['PS_1','PS_2','elo_1','elo_2','id_1','id_2','Rank_1','Rank_2']]
    joueur_1 = df_Coric.iloc[option_match_index]['Joueur_1']
    joueur_2 = df_Coric.iloc[option_match_index]['Joueur_2']
    resultat = df_Coric.iloc[option_match_index]['Victoire_J1']           


# Spération de la variable cible et des Dataset d'entrainement et de test
X_train = atp_clean.drop(['Victoire_J1'] , axis=1)
X_test = atp_pred.drop(['Victoire_J1'] , axis=1)
y_train = atp_clean['Victoire_J1']
y_test = atp_pred['Victoire_J1']


# RandomForestClassifier
X_train = atp_clean[(['PS_1','PS_2','elo_1','elo_2','id_1','id_2','Rank_1','Rank_2'])]
X_test = atp_pred[(['PS_1','PS_2','elo_1','elo_2','id_1','id_2','Rank_1','Rank_2'])]

ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

model_RF3 = RandomForestClassifier(n_estimators=30, max_depth=4, random_state = 42)
model_RF3.fit(X_resampled, y_resampled)


input_data = pd.DataFrame({
    'id_1': [forecast['id_1']],
    'Rank_1': [forecast['Rank_1']],
    'elo_1': [forecast['elo_1']],
    'id_2': [forecast['id_2']],
    'Rank_2': [forecast['Rank_2']],
    'elo_2': [forecast['elo_2']],
    'PS_1': [forecast['PS_1']],
    'PS_2': [forecast['PS_2']]
})


prediction = model_RF3.predict(input_data)

st.subheader("Prediction:")
if prediction[0] == 1:
    st.write(f"Je prédis que le joueur gagnant est {joueur_1} ")
elif prediction[0] == 0:
    st.write(f"Je prédis que le joueur gagnant est {joueur_2}")

if st.checkbox("Afficher le résultat réel"):
    if resultat == 1:
        st.write(f"Le joueur qui a réellement gagné est {joueur_1} ")
    elif resultat == 0:
        st.write(f"Le joueur qui a réellement gagné est {joueur_2} ")