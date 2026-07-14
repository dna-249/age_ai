from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from age import get_age_prediction

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'age' not in data:
        return jsonify({'error': 'Missing age'}), 400
    
    try:
        age = int(data['age'])
    except ValueError:
        return jsonify({'error': 'Age must be an integer'}), 400
    
    result = get_age_prediction(age)
    
    if result is None: 
        return jsonify({'error': 'Invalid age (0-120)'}), 400
        
    return jsonify({'age': age, 'behaviors': result})

if __name__ == '__main__':
    app.run(port=5000, debug=True)