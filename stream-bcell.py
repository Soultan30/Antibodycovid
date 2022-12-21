import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('bcell.sav', 'rb'))

st.title('Prediksi Antibody Terhadap Penyakit COVID-19')

col1, col2 = st.columns(2)

with col1:
    start_position = st.text_input('Start Position')

with col2:
    end_position = st.text_input('End Position')

with col1:
    chou_fasman = st.text_input('Chou Fasman')

with col2:
    emini = st.text_input('Emini')

with col1:
    kolaskar_tongaonkar = st.text_input('Kolaskar Tongaonkar')

with col2:
    parker = st.text_input('Parker')

with col1:
    isoelectric_point = st.text_input('Isoelectric Point')

with col2:
    aromaticity = st.text_input('Aromaticity')

with col1:
    hydrophobicity = st.text_input('Hydrophobicity')

with col2:
    stability = st.text_input('Stability')

bcell_diagnosis = ''

if st.button('Prediksi Antibody Terhadap Penyakit COVID-19'):
    bcell_prediction = model.predict([[start_position, end_position, chou_fasman, emini, kolaskar_tongaonkar, parker, isoelectric_point, aromaticity, hydrophobicity, stability]])

    if(bcell_prediction[0]==0):
        bcell_diagnosis = 'Lemah'
    else:
        bcell_diagnosis = 'Kuat'

st.success(bcell_diagnosis)