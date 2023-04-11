import csv
import pandas as pd
import streamlit as st
    
# membaca file csv kamus bahasa Indonesia-Inggris
df = pd.read_csv('Kamus2.csv', delimiter=',')
# menampilkan kata-kata dalam bahasa Indonesia dan Inggris
for index, row in df.iterrows():
 kata_indonesia = row['inggris']
 kata_inggris = row['indonesia']
 print(kata_indonesia, kata_inggris)

# Load the English-Indonesian dictionary
dictionary = pd.read_csv("Kamus2.csv")

def translate(word):
    translation = dictionary[dictionary["indonesia"] == word]["inggris"]
    if len(translation) > 0:
        return translation.values[0]
    else:
        return "Kata tidak ditemukan di dalam kamus."

# Set up the Streamlit app
st.title("Kamus Bahasa Indonesia-Inggris")
word = st.text_input("Masukkan kata dalam bahasa Inggris:")
if st.button("Terjemahkan"):
    translation = translate(word)
    st.write("Arti kata dalam bahasa Indonesia:")
    st.write(translation)
    