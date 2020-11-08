import click
import language
import translator


def print_languages():
    print(', '.join([e.value for e in language.Language]))


def print_translations(translations):
    for translation in translations:
        print(translation)


def translate(first_lang, second_lang, search_term):
    translation = translator.translate(first_lang, second_lang, search_term)
    print_translations((translation))


def print_help():
    ctx = click.get_current_context()
    print(ctx.get_help())


@click.command()
@click.option('--languages', is_flag=True, help='Get a list of all available languages.')
@click.argument('first_lang', default='')
@click.argument('second_lang', default='')
@click.argument('search_term', default='')
def pons(languages, first_lang, second_lang, search_term):
    if languages:
        print_languages()
    elif first_lang and second_lang and search_term:
        translate(first_lang, second_lang, search_term)
    else:
        print_help()


if __name__ == '__main__':
    pons()
