import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title('Loan Eligibility Solution')
st.image('loan.jpg')

Credit_History = st.number_input('Credit History', min_value=0, max_value=1, step=1)
ApplicantIncome = st.number_input('Applicant Income', min_value=0)
LoanAmount = st.number_input('Loan Amount', min_value=0)
Education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
Gender = st.selectbox('Gender', ['Male', 'Female'])

if st.button('Predict'):
    if Education == 'Graduate':
        Education_num = 1
    else:
        Education_num = 0

    if Gender == 'Male':
        Gender_num = 1
    else:
        Gender_num = 0

    makeprediction = model.predict([[Credit_History, ApplicantIncome, LoanAmount, Education_num, Gender_num]])
    output = makeprediction[0]

    if output == 1:
        result = 'Eligible'
    else:
        result = 'Not Eligible'

    st.success(f'Loan Eligibility: {result}')
