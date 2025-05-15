import streamlit as st
import pickle
st.title("iris plant prediction")
sl=st.number_input("enter sepal lenght")
sw=st.number_input("enter sepal width")
pl=st.number_input("enter petal lenght")
pw=st.number_input("enter petal width")
button=st.button("predict")
if button:
    model=pickle.load(open("iris.pkl","rb"))
    res=model.predict([[sl,sw,pl,pw]])[0]
    st.markdown(f"Predict Iris Class :{res}")
