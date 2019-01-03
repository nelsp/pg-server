import requests
import random
import json

from constants import SERVER_HOST, SERVER_PORT
server_url = SERVER_HOST + SERVER_PORT


def main(player, my_info, player_token):
    my_info = requests.get(server_url + "/my_info",cookies=player_token).json()
    print(json.dumps(my_info, indent=4))
    response = choose_power(my_info['info']['name'], player_token)
    #print(json.dumps(player_info, indent=4))


def choose_power(player_name, player_token):
    my_info = requests.get(server_url + "/my_info", cookies=player_token).json()
    #print('xxxxx', my_info['info']['powerplants']['market_cost'])
    payload = dict(player_name=player_name)
    payload['powerplants']= [my_info['info']['powerplants'][0]['market_cost']]

    print('payload', payload)
    response = requests.post(server_url + "/power", json=payload, cookies=player_token).json()
    print(response.text)
    return response