import requests

useless_quote_url = "https://uselessfacts.jsph.pl/random.json?language=en"


def get_random_useless_quote():
    response = requests.get(useless_quote_url)
    res_map = response.json()
    return res_map['text']
