from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('template.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input values from the form
        type = request.form['type']
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])

        # Make prediction
        features = np.array([[type, amount, oldbalanceOrg, newbalanceOrig]])
        prediction = model.predict(features)

        # Display the prediction result
        if prediction == 'No Fraud':
            result = 'No Fraud'
        else:
            result = 'Fraud'

        return render_template('template.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
