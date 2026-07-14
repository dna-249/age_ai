import pandas as pd
import joblib
import os

# Load these once globally when the server starts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'model.pkl'))
mlb = joblib.load(os.path.join(BASE_DIR, 'mlb.pkl'))

def get_age_prediction(age):
    try:
        input_age = int(age)
        if not (0 <= input_age <= 120):
            return None
            
        input_df = pd.DataFrame([[input_age]], columns=['Age'])
        pred_array = model.predict(input_df)

        # Convert binary result back into readable behavior names
        predicted_behaviors = mlb.inverse_transform(pred_array)
        return list(predicted_behaviors[0]) if predicted_behaviors else []
    except Exception:
        return None