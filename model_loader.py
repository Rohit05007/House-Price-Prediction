import os
import joblib
import gdown

def load_model():

    url = "https://drive.google.com/uc?export=download&id=1XHAIlEX25dWUKT25-aMkTRn-XnH_ZFfJ"
    output = "house_price_model.pkl"

    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)

    # Load model
    model = joblib.load(output)

    return model
