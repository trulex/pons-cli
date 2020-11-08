from enum import Enum


# the languages are defined in pons api docs pdf
# we could call /dictionaries to get the list, but it probably won't change so often
class Language(Enum):
    DE = 'de'
    EL = 'el'
    EN = 'en'
    ES = 'es'
    FR = 'fr'
    IT = 'it'
    PL = 'pl'
    PT = 'pt'
    RU = 'ru'
    SL = 'sl'
    TR = 'tr'
    ZH = 'zh'
