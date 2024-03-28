import requests
from utils.translator import Translator


class Advice:
  def __init__(self) -> None:
    self.advice_url = "https://api.adviceslip.com/advice"

  def get_random_advice(self):
    response = requests.get(f"{self.advice_url}/{id}")
    if response.status_code == 200 and self.is_advice_exist(id):
        advice = response.json()['slip']['advice']
        return advice
    elif response.status_code == 200 and not self.is_advice_exist(id):
        message = response.json()['message']['text']
        return message
    else:
        print("Failed to retrieve advice")
  
  def get_advice_by_id(self, id):
    response = requests.get(f"{self.advice_url}/{id}")
    if response.status_code == 200 and self.is_advice_exist(id):
        advice = response.json()['slip']['advice']
        return advice
    elif response.status_code == 200 and not self.is_advice_exist(id):
        message = response.json()['message']['text']
        return message
    else:
        print("Failed to retrieve advice")

  def is_advice_exist(self, id):
    response = requests.get(f"{self.advice_url}/{id}")
    if response.status_code == 200 and response.json()['message']['type'] != 'error':
        return True
    else:
        return False