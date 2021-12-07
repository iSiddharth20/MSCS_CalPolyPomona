'''
Importing Necessary Libraries
'''
# For Web Rendering
from flask import Flask, render_template, request
# To Load ML Model
import joblib


'''
Importing Accuracy Value of 
Importing Data Formatting Functions from 'text_formatting.py'
'''
from text_formatting import format_data , distributed_format


'''
Initialising Flask Dependencies
'''
app = Flask(__name__)


'''
Importing the Trained Model
'''
mul_reg = open("trained_model.pkl", "rb")
ml_model = joblib.load(mul_reg)


'''
Declaring Outputs based on Prediction
'''
def calstr(num):
    if num == 'Negative' or num == 'negative':
        return 'Movie Likelihood : Low'
    elif num == 'Positive' or num == 'positive':
        return 'Movie Likelihood : High'
    else:
        return 'Error!'


'''
Rendering Input/Home Page
'''
@app.route("/")
def home():
    return render_template('home.html')


'''
Rendering Output Page
'''
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.form.get('NewYork'))
        try:
            # Getting Movie Review as User Input
            review = str(request.form['Review'])
            # Formatting the Movie Review Text
            review = format_data(review)
            review = distributed_format(review)
            # Predicting Movie Likelihood
            model_prediction = calstr(ml_model.classify(review))
        except ValueError:
            return "Value Error!"
    # Rendering Output Page
    return render_template('predict.html', prediction = model_prediction)


'''
Defining Main Function
'''
if __name__ == "__main__":
    app.run()
