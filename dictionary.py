import os, requests, json
from dotenv import load_dotenv
import sys

load_dotenv()

word = input('Enter a word you want to search for: ')
api_key = os.environ.get('API_KEY')

url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
response = requests.get(url)
response_status = response.status_code

data = json.loads(response.text)
