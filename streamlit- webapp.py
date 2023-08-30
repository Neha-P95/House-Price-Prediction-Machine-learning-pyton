import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('houseprice.pkl', 'rb'))

st.title('USA House Price Prediction')
st.sidebar.header('USA')
st.sidebar.subheader('House Data')
# image = Image.open('pexels-binyamin-mellish-1396122.jp')
st.image("pexels-binyamin-mellish-1396122.jpg",'')

# FUNCTION
def user_report():
  bedrooms = st.sidebar.slider('Bedrooms', 0,8, 1 )
  bathrooms = st.sidebar.slider('Bathrooms', 0,9, 1 )
  sqft_living = st.sidebar.slider('Sqft Living', 370,13540, 370 )
  sqft_lot = st.sidebar.slider('Sqft lot', 638,1074218, 1 )
  floors = st.sidebar.slider('Floors', 1,4, 1 )
  waterfront = st.sidebar.slider('Waterfront', 0,1, 1)
  view = st.sidebar.slider('View', 0,4, 1)
  condition = st.sidebar.slider('Condition', 1,5, 1)
  sqft_above = st.sidebar.slider('Sqft Above', 370,9410, 1)
  sqft_basement = st.sidebar.slider('Sqft Basement', 0,4820, 1)
  year_built = st.sidebar.slider('Year Built', 1900,2014, 1900)
  year_renovated = st.sidebar.slider('Year Renovated', 0,2014, 1)
  street = st.sidebar.slider('Street', 0,4524, 1)
  city = st.sidebar.slider('City', 0,43, 1)
  statezip = st.sidebar.slider('Statezip', 0,76, 1)
  country = st.sidebar.slider('Country', 0,0, 1)








  user_report_data = {
      'bedrooms':bedrooms,
      'bathrooms':bathrooms,
      'sqft_living':sqft_living,
      'sqft_lot':sqft_lot,
      'floors':floors,
      'waterfront':waterfront,
      'view':view,
      'condition':condition,
      'sqft_above':sqft_above,
      'sqft_basement':sqft_basement,
      'yr_built':year_built,
      'yr_renovated':year_renovated,
      'street':street,
      'city':city,
      'statezip':statezip,
      'country':country

  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('House Data')
st.write(user_data)

salary = model.predict(user_data)
st.subheader('House Price')
st.subheader('$'+str(np.round(salary[0], 2)))
