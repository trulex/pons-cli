import json
from bs4 import BeautifulSoup


def translate(first_lang, second_lang, search_term):
    # call api


    # parse response
    with open('test/response.json') as f:
        read_data = f.read()

    response = json.loads(read_data)
    roms = response[0]['hits'][0]['roms']
    headwords = []
    for rom in roms:
        stripped = BeautifulSoup(rom['headword_full'], features="html.parser").get_text()
        headwords.append(stripped)

    return headwords
