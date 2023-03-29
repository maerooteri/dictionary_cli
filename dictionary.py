import os, requests, json
from dotenv import load_dotenv
import sys

load_dotenv()

word = input('Enter a word you want to search for: ')
api_key = os.environ.get('API_KEY')

url = f"https://www.dictionaryapi\
    .com/api/v3/references/collegiate/json/{word}?key={api_key}"

response = requests.get(url)
response_status = response.status_code

data = json.loads(response.text)

if data and type(data[0]) is dict:
    try:
        pronunciation = data[0].get('hwi').get('prs')[0].get('mw')
        pronunciation = pronunciation.strip("ˈ").strip("ˌ").strip(",")
    except Exception:
        pronunciation = ''
    try:
        part_of_speech = data[0].get('fl')
    except Exception:
        part_of_speech = ''
    meaning = data[0].get('shortdef')[0]
    meaning = meaning.split(':')[0].strip()

    final_output = f"{pronunciation} ({part_of_speech}): {meaning}"
elif type(data) is list:
    """This gives Homonyms (similar words in the dictionary),
      if the word we searched for doesnt exist"""
    final_output = f"This word definition doesn't exist in\
          this dictionary, did you mean any of these ? \n {data}"
else:
    final_output = f"Word definition doesn't exist in this dictionary"
