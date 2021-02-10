from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def init():
    global model
    model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods =['GET'])
def predict():
    if request.methof
    prediction = ""
    return render_template('index.html', prediction=prediction)

@app.route('/', methods =['POST'])
def predict():
    # model = pickle.load(open('model.pkl', 'rb'))
    if request.method == 'POST':
        user_input = request.form.get('query')
        user_input =  str(user_input)
        prediction = model.predict(user_input)
    else:
        prediction = ""

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    init()
    app.run(debug=True)

