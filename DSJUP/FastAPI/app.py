# pip install uvicorn fastapi
import uvicorn 
from fastapi import FastAPI
from input import getData 

app = FastAPI()
# get, post, update, delete
@app.get('/')
def index():
    return{'message':'Hello Students, how are you!!'}
@app.get('/name')
def printNaam():
    return{'message':'Hello Mehak'}
@app.post('/getname')
def getName(data:getData):
    dict_data = data.model_dump() #Export the model instance to a dictionary
    print(dict_data)

    return dict_data