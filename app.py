import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
  with open('model.pkl', 'rb') as file:
      data = pickle.load(file)
  return data

data = load_model()

model = data["model"]

columns = ['city', 'date', 'time', 'year', 'month', 'day', 'hour', 'minute', 'weather', 'temp', 'wind', 'humidity', 'barometer', 'visibility']

def show_predict_page():
    st.title("Weather Prediction ")
    
    st.write("""### We need some information for prediction""")

    hour = (
        24,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10
    )

    temp = (
        5,
        10,
        15,
        20,
        25,
        30,
        35,
        40,
        45,
        50,
        55,
        60,
        65,
        70,
    )

    hours = st.selectbox("Hour", hour)
    temps = st.selectbox("Temperature", temp)

    ok = st.button("Predict")

    if ok:
        st.write("""### Prediction""")
        st.write("""### The predicted weather is: """)
        # st.write(model.predict(np.array([hours])))


show_predict_page()

