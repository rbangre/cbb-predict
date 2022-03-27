import streamlit as st
import pickle
import numpy as np
import pandas as pd
from teams import cbb_teams

data_2021 = pd.read_csv("../data/ncaab-data/cbb21.csv")

def load_model(): 
    with open('saved_steps.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

data = load_model()

postseason_model = data["postseason_model"]
seed_model = data["seed_model"]
postseason_label_encoder = data["postseason_label_encoder"]

def show_predict_page(): 
    st.title("NCAA Basketball Model Predictions")

    st.write("""Please Select a Team you'd like to learn about for the 2021 Season !""")

    team = st.selectbox("Team", cbb_teams)

    button = st.button("Determine Seeding Predictions")
    if button: 
        team_data = data_2021[data_2021["TEAM"] == team]
        team_data = team_data[["WP", "ADJOE", "ADJDE", "BARTHAG", "EFG_O", "EFG_D", 
        "TOR", "TORD", "ORB", "DRB", "FTR", "FTRD", "2P_O", 
        "2P_D", "3P_O", "3P_D", "ADJ_T", "WAB"]]

        seed = seed_model.predict(team_data)[0]

        if seed == 0: 
            st.write("""The data suggests """ + str(team) + """ will not be in the tournament.""")
        #postseason = postseason_model.predict(team_data)[0]
        # postseason = postseason_label_encoder.inverse_transform([postseason])[0]
        else: 
            st.write("""The data suggests """ + str(team) + """ will be a """ + str(seed) + """ seed in the tournament.""")

    
