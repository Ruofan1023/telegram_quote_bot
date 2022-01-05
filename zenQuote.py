import requests

zen_quote_url = "https://zenquotes.io/api/random"

def get_random_zen_quote():
    response = requests.get(zen_quote_url)
    list = response.json()
    text = list[0]['q'];
    author = list[0]['a']
    return text + " - " + author
