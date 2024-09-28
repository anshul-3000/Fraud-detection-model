# Transaction Guardian
## Fraud Detection System Using Decision Tree Classifier
## Overview
This project implements a fraud detection system using a Decision Tree Classifier with Gini Impurity. The model is designed to identify fraudulent transactions based on historical transaction data. The project includes data preprocessing, model training, and a simple web interface for real-time fraud detection.

## Project Details
#### Dataset: Contains transactional data with features relevant to fraud detection (e.g., transaction amount, transaction type).
#### Tools & Libraries: Python, scikit-learn, Flask, Pandas, NumPy
#### Objective: To build and deploy a machine learning model that can accurately classify transactions as fraudulent or non-fraudulent.\

## Features
#### Data Preprocessing: Data cleaning, feature selection, and splitting into training and test sets.
#### Model Training: Utilizes a Decision Tree Classifier with Gini Impurity to train the model.
#### Web Interface: A simple Flask application to input transaction details and get fraud predictions.

## Installation
#### Navigate to the project directory:
cd fraud-detection-model

#### Install the required dependencies:
pip install -r requirements.txt

## Usage
Start the Flask application:
python app.py

#### Open your web browser and go to https://fraud-detection-model.onrender.com/ to access the fraud detection interface.

Enter the transaction details in the form and submit to get a prediction on whether the transaction is fraudulent or not.

## Project Structure
#### app.py: Main Flask application for the web interface.
#### model.py: Contains the code for model training and prediction.
#### data/: Directory for storing raw and processed data.
#### static/: Directory for static files (e.g., CSS, JavaScript).
#### templates/: Directory for HTML templates used in the Flask application.
#### requirements.txt: List of dependencies for the project.

## Results
#### Model Accuracy: Evaluated on test data to determine performance metrics (e.g., accuracy, precision, recall).
#### Web Interface: Allows users to input transaction data and receive fraud predictions in real-time.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue if you have suggestions or find bugs.
