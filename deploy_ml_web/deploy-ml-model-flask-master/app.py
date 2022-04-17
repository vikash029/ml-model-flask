from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def home():
    Nitrogen = request.form['a']
    phosphorous = request.form['b']
    potassium = request.form['c']
    temperature = request.form['d']
    humidity = request.form['e']
    ph = request.form['f']
    rainfall = request.form['g']
    predicition = model.predict((np.array([[Nitrogen,phosphorous , potassium, temperature , humidity , ph , rainfall]])))
    #print("the suggested crop for given climatic condition id of RandomForestClassifier:", predicition)
    output = predicition
    pu = [Nitrogen ,phosphorous , potassium, temperature , humidity , ph , rainfall]

   
    return render_template ("index.html" , pr_text = "the suggested crop for given climatic condition is: {}".format(output) )


if __name__ == "__main__":
    app.run(debug=True)




#Nitrogen=90,phosphorous=40,potassium=40,temperature=20,humidity=80,ph=7,rainfall=200










