import gdown
import joblib

def load_model():

    # 🔥 Paste your Google Drive link here
    url = "YOUR_GOOGLE_DRIVE_LINK"

    output = "house_price_model.pkl"

    gdown.download(url, output, quiet=False)

    model = joblib.load(output)

    return model