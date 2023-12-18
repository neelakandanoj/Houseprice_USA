# import necessary librairies
import streamlit as st
import numpy as np
import string
import pickle
# st.set_option('deprecation.showfileUploaderEncoding',False)
model = pickle.load(open('model.pkl','rb'))


def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>House Price Predictor</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Drop in The required Inputs and we will do  the rest.</h3>", unsafe_allow_html=True)
  st.sidebar.header("What is this Project about?")
  st.sidebar.text("It a Web app that would help the user in determining the price of a house .")
  st.sidebar.header("What tools where used to make this?")
  st.sidebar.text("The Model was made using a dataset from Kaggle along with using Kaggle notebooks to train the model. We made use of Sci-Kit learn in order to make our Linear Regression Model.")



  Per_Capita_GDP = st.slider(" Per Capita GDP",45000.00,70000.00)
  UNRATE = st.slider("Input the Unemployment rate",4.0,15.0)
  Cons_Materials = st.slider("Enter the Construction_Price",500.00,2500.00)
  FEDFUNDS = st.slider("Enter the Intrest-rate",0,10)

  inputs = [[Per_Capita_GDP, UNRATE, Cons_Materials, FEDFUNDS]]

  if st.button('Predict'):
    result = model.predict(inputs)
    st.success('The Estimated price of the house is {} per unit area'.format(result))


if __name__ =='__main__':
  main()
