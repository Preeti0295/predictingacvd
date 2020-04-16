import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'male':0, 'age':46, 'cigsPerDay':0, 'BPMeds':0, 'prevalentStroke':0, 'prevalentHyp':0, 'diabetes':0, 'totChol':250, 'sysBP':121, , 'diaBP':80, 'BMI':25, 'heartRate':75, 'glucose':121})

print(r.json())