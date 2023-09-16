from flask import Flask,request,render_template
import numpy as np
import pandas
import sklearn
import pickle

model = pickle.load(open('RandomForest.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
def pre():
    N = int(request.form['Nitrogen'])
    P = int(request.form['Phosporus'])
    K = int(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])
    data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(data)
    print(prediction)
    op = str(prediction)
    op = op[1:-1]
    op = op[1:-1]
    s = op.capitalize()
    result = "{} is the best crop to be cultivated there".format(s)
    return render_template('index.html',result = result,name = op)
    
#     print(result)

# python main
if __name__ == "__main__":
    app.run(debug=True)