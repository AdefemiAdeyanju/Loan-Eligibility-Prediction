from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

model = pickle.load(open('model.pkl', 'rb'))

class LoanInput(BaseModel):
    Credit_History: int
    ApplicantIncome: int 
    LoanAmount:int
    Education: str
    Gender: str

class LoanOutput(BaseModel):
    eligible: bool

@app.post('/predict/')
def predict_loan_eligibility(input_data: LoanInput):
    # Convert Education and Gender to numerical format
    if input_data.Education == 'Graduate':
        Education = 1
    else:
        Education = 0

    if input_data.Gender == 'Male':
        Gender = 1
    else:
        Gender = 0

    # Make the prediction
    makeprediction = model.predict([[input_data.Credit_History, input_data.ApplicantIncome, input_data.LoanAmount, Education, Gender]])
    output = makeprediction[0]

    # Create response object
    response = LoanOutput(eligible=bool(output))

    return response
