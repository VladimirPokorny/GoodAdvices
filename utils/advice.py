import requests
from utils.translator import Translator


class Advice:
  def __init__(self) -> None:
    self.advice_url = "https://api.adviceslip.com/advice"

  def get_random_advice(self):
    response = requests.get(self.advice_url)
    if response.status_code == 200:
        advice = response.json()['slip']['advice']
        return advice
    else:
        print("Failed to retrieve advice")