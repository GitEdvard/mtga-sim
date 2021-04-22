import pytest
import requests
import json


RANDOM_URL = 'https://api.scryfall.com/cards/random'


class TestApi:
    def test_export_random_card_to_file(self):
        session = requests.session()
        response = session.get(RANDOM_URL, headers={"Content-Type": "application/json"})
        # print(json.dumps(response.json(), indent=4))
        # with open(r'/home/edvard/sources/mtga-sim/resources/random_card.json', 'w') as f:
        #     f.write(json.dumps(response.json(), indent=4))
        assert False
