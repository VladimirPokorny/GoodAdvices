import requests
from dotenv import load_dotenv
import os

load_dotenv()


class Translator:
    def __init__(self):
        self.translator_API_url = "https://api-free.deepl.com/v2/translate"

    def translate_text(self, text, target_lang):
        
        # Request parameters
        params = {
            "auth_key": os.getenv("DEEPL_API_KEY"),
            "text": text,
            "target_lang": target_lang
        }
        
        # Send POST request to DeepL API
        response = requests.post(self.translator_API_url, data=params)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response
            translation_data = response.json()
            # Extract and return translated text
            translated_text = translation_data['translations'][0]['text']
            return translated_text
        else:
            # If request was not successful, print error message
            print("Error:", response.text)
            return None