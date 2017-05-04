import config
import requests
from bs4 import BeautifulSoup


def get_new_series():
    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
        # Sign in ororo.tv to be able to see all series
        json = 'https://ororo.tv/en/users/sign_in.json'
        p = s.post(json, data=config.ororo_payload, proxies=config.proxies, headers=config.headers)
        # TODO check if status is 200, handle error
        # print(p.text)

        # Load series page
        r = s.get('https://ororo.tv/en',  proxies=config.proxies, headers=config.headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        fav_series_list = soup.find_all('div', class_='favorites-item movie')
        new_series = []

        for series in fav_series_list:
            series_name = series.find("p", class_="movie-title").contents[0]
            new_episodes_count = series.find("div", class_="movie-badge full")
            if new_episodes_count is not None:
                new_series.append({"name": series_name, "amount": new_episodes_count.contents[0]})
        return new_series

# TODO what if update_data is None?
def format_message(update_data):
    response = ""
    for series in update_data:
        response += "There is {0} new episode on {1}\n".format(series["amount"], series["name"])
    return response