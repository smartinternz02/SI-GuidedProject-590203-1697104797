from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the pickled model
with open('fraud_detection_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
 
@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict(): 
        if request.method =='POST':
            type = int(request.form.get('type'))
            amount = float(request.form.get('amount'))
            oldbalanceOrg = float(request.form.get('oldbalanceOrg'))
            newbalanceOrig = float(request.form.get('newbalanceOrig'))
        
   
        prediction = model.predict([[type,amount,oldbalanceOrg,newbalanceOrig]])

        # Return the prediction result
        
        return render_template('predict.html', is_fraud=prediction[0])

   
if __name__ == '__main__':
    app.run(debug=True)