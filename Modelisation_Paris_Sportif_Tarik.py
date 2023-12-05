import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

#atp=pd.read_csv("atp_data.csv")

st.title("Est-il possible de battre les algorithmes des bookmakers sur l’estimation des probabilités d’un joueur gagnant un match de Tennis ? ")
#st.image("Image_Couv.jpg")


# with open('rf_model', 'rb') as pickle_out:
    # model = pickle.load(pickle_out)
	
picklefile = open("rf_model_Tarik0.pkl", "rb")
model = pickle.load(picklefile)

st.title("Random Forest Classifier App")

WRank = st.slider("WRank", min_value=0, max_value=1890)
elo_loser = st.slider("elo_loser", min_value=1333.9214021861708, max_value=2392.595566601127)
elo_winner = st.slider("elo_winner", min_value=1323.9014800728364, max_value=2392.40892268678)
LRank = st.slider("LRank", min_value=0, max_value=1890)

input_data = pd.DataFrame({
    'WRank': [WRank],
    'elo_loser': [elo_loser],
    'elo_winner': [elo_winner],
    'LRank': [LRank]
})

prediction = model.predict(input_data)

st.subheader("Prediction:")
st.write(prediction[0])