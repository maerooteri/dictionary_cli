import os, requests, json
from dotenv import load_dotenv
import sys

load_dotenv()


def get_word_definition(word):
    try:
        url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
        response = requests.get(url)
        response_status = response.status_code
        # print(response_status)
        if response_status == 200:
            data = json.loads(response.text)
            # print(data)

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
                final_output = "This word definition doesn't exist in this dictionary"
            else:
                final_output = "This word definition doesn't exist in this dictionary"

        return final_output
    except Exception:
       return "An Exception occured!!" 


api_key = os.environ.get('API_KEY')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = input('Enter a word you want to search for: ')
    output = get_word_definition(word)
    print(output)

