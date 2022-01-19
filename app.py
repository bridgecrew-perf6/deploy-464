import streamlit as st

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
    date = st.date_input('Date')

    ok = st.button("Predict")

    if ok:
        st.write("""### Prediction""")
        st.write("""### The predicted weather is: """)


show_predict_page()

