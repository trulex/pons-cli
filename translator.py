import json
from bs4 import BeautifulSoup
import pons_api


def translate(first_lang, second_lang, search_term):
    response = pons_api.get_translations(first_lang, second_lang, search_term)

    roms = response[0]['hits'][0]['roms']
    headwords = []
    for rom in roms:
        stripped = BeautifulSoup(rom['headword_full'], features="html.parser").get_text()
        headwords.append(stripped)

    return headwords
