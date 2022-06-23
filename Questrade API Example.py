#!/usr/bin/env python
# coding: utf-8

# Questrade API Example

import pprint
import requests
from requests_oauthlib import OAuth2Session
from urllib.parse import urljoin

## Get Questrade API Data

### Set up OAuth2 session

token = {
    "access_token": "AQe1fAItV2E5BsmnHMN6M9HG6CCEgckG0",
    "api_server": "https://api01.iq.questrade.com/",
    "expires_in": 1800,
    "refresh_token": "cz-tuua7D98nGpqVuwhXF_QCz2a0gT_o0",
    "token_type": "Bearer"
}
refresh_url = 'https://login.questrade.com/oauth2/token'


def token_saver(new_token):
    token = new_token

client = OAuth2Session(token=token, auto_refresh_url=refresh_url, token_updater=token_saver)


### Get account

questrade_api = 'https://api01.iq.questrade.com/'
accounts_route = 'v1/accounts'
questrade_accounts_endpoint = urljoin(questrade_api, accounts_route)
print(f'Questrade Accounts Endpoint: {questrade_accounts_endpoint}')


def get_questrade_data(endpoint, params=None):
    """
    Gets data from the Questrade API given an endpoint and parameters.
    
    Parameters:
        endpoint (string): A Questrade API URI
        params (dictionary): A map of parameters to values for building the query string
        
    Returns:
        data (dictionary): The Questrade API response
    """
    response = client.get(endpoint, params=params)
    response.raise_for_status()
    data = response.json()
    
    return data

account_data = get_questrade_data(questrade_accounts_endpoint)
pp = pprint.PrettyPrinter()
pp.pprint(account_data)


### Get account positions

account_number = account_data['accounts'][0]['number']
print(account_number)

account_positions_route = f'accounts/{account_number}/positions'
account_positions_endpoint = urljoin(questrade_accounts_endpoint, account_positions_route)
print(f'Questrade Accounts Positions Endpoint: {account_positions_endpoint}')

account_positions_data = get_questrade_data(account_positions_endpoint)
pp.pprint(account_positions_data)


### Get market symbol

symbols_search_route = 'v1/symbols/search'
questrade_symbols_search_endpoint = urljoin(questrade_api, symbols_search_route)
print(f'Questrade Symbols Search Endpoint: {questrade_symbols_search_endpoint}')

symbol = 'AAPL'
symbols_data = get_questrade_data(questrade_symbols_search_endpoint, params={'prefix': symbol})
pp.pprint(symbols_data)

id = 8049
symbols_id_route = f'v1/symbols/{id}'
questrade_symbols_id_endpoint = urljoin(questrade_api, symbols_id_route)
print(f'Questrade Symbols Endpoint: {questrade_symbols_id_endpoint}')

symbol_id_data = get_questrade_data(questrade_symbols_id_endpoint)
pp.pprint(symbol_id_data)
