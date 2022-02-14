from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__, template_folder='templates')

model = pickle.load(open('model_random.pkl', 'rb'))

@app.route('/')
def start():
    
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'GET':
        return (render_template('main.html'))

    if request.method == 'POST':
        ex = -1
        
        bedrooms = request.form['bedrooms']
        if bedrooms == '':
            bedrooms = int(ex)
            
        bathrooms = request.form['bathrooms']
        if bathrooms == '':
            bathrooms = int(ex)
        
        sqft_living = request.form['sqft_living']
        if sqft_living == '':
            sqft_living = int(ex)
            
        sqft_lot = request.form['sqft_lot']
        if sqft_lot == '':
            sqft_lot = int(ex)
            
        zipcode = request.form['zipcode']
        if zipcode == '':
            zipcode = int(ex)
            
        yr_built = request.form['yr_built']
        if yr_built == '':
            yr_built = int(ex)
            
        sqft_above = request.form['sqft_above']
        if sqft_above == '':
            sqft_above = int(ex)
        
        design = str(request.form['grade'])
        if (design == "Low"):
            grade = 3
        elif (design == "Medium"):
            grade = 7
        else:
            grade = 11
            
        sqft_living15 = int(sqft_living) + 1800
        
        sqft_lot15 = int(sqft_lot) + 7533
        
        if (bathrooms == -1) | (sqft_living == -1) | (sqft_lot == -1) | (sqft_above == -1) | (yr_built == -1) | (zipcode == -1):
            return render_template("index.html", pred="Complete the information below:")
        
        values = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, grade, sqft_above, yr_built, zipcode, sqft_living15, sqft_lot15]])
        
        output = int(model.predict(values))
    
    return render_template("index.html", pred="The price of your house is: US${}".format(output))

if __name__ == "__main__":
    app.run(debug=True)