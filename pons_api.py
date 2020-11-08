import configparser
import requests


DICTIONARY = "https://api.pons.com/v1/dictionary"
config = configparser.ConfigParser()
env = config.read('.env')
secret = config.get('all', 'secret')
HEADERS = {'X-Secret': secret}


def build_query_params(first_lang, second_lang, search_term):
    query_params = {
                    'q': search_term,
                    'l': first_lang+second_lang,
                    'language': 'en'  # display results in English
                    }
    return query_params


def get_translations(first_lang, second_lang, search_term):
    params = build_query_params(first_lang, second_lang, search_term)

    response = requests.get(url=DICTIONARY, params=params, headers=HEADERS)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()

    json = response.json()

    return json
