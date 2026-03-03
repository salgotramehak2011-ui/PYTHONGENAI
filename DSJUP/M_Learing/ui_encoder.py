import joblib

encoder = joblib.load('encoder.pkl')

value = input('Enter(man,women,child)')
print(encoder.transform([[value]]).toarray())