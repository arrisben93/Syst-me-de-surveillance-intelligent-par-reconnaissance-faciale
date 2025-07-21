import streamlit as st
import pandas as pd
from base_donnees import recuperer_detections

def authentification():
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type='password')
    if username == 'Ariss' and password == '2000':
        return True
    else:
        st.warning("Identifiants invalides.")
        return False

def dashboard():
    st.title("Dashboard Surveillance IA2")
    data = recuperer_detections()
    df = pd.DataFrame(data, columns=["Nom", "Date/Heure"])
    st.subheader("Historique des détections")
    st.dataframe(df)
    st.subheader("Statistiques")
    stats = df['Nom'].value_counts().rename_axis('Nom').reset_index(name='Nombre de passages')
    st.bar_chart(stats.set_index('Nom'))

if __name__ == "__main__":
    if authentification():
        dashboard()
