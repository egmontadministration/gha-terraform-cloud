import requests
import json


def get_oauth_clients(organization, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/vnd.api+json',
    }

    url = f'https://app.terraform.io/api/v2/organizations/{organization}/oauth-clients'

    response = requests.get(url=url, headers=headers)
    return response.json()['data']


def get_oauth_client_token_id(organization, token, client_name):
    clients = get_oauth_clients(organization,token)

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/vnd.api+json',
    }

    for client in clients:
        if client['attributes']['name'] == client_name:
            url = 'https://app.terraform.io/api/v2/oauth-clients/{}/oauth-tokens'.format(client['id'])

            response = requests.get(url=url, headers=headers)

            return response.json()['data'][0]['id']


def register_module(organization, token, oauth_client_name, github_organization, repository_name):
    oauth_client_token_id = get_oauth_client_token_id(organization, token, oauth_client_name)

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/vnd.api+json',
    }

    body = {
        'data': {
            'attributes': {
                'vcs-repo': {
                    'identifier': f'{github_organization}/{repository_name}',
                    'oauth-token-id': oauth_client_token_id,
                    'display_identifier': f'{github_organization}/{repository_name}'
                }
            },
            'type': 'registry-modules'
        },
    }

    url = f'https://app.terraform.io/api/v2/organizations/{organization}/registry-modules/vcs'

    response = requests.post(url=url, headers=headers, json=body)

    if 299 < response.status_code < 200:
        raise Exception(f'Module registration failed: {response.json()}')


def get_modules(organization, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/vnd.api+json',
    }

    url = f'https://app.terraform.io/api/v2/organizations/{organization}/registry-modules?page[size]=100'

    modules = []

    while url is not None:
        response = requests.get(url=url, headers=headers)
        url = response.json()['links']['next']

        for module in response.json()['data']:
            modules.append(module)

    return modules


def check_module_exists(organization, token, github_organization, repository_name):
    modules = get_modules(organization, token)

    for module in modules:
        if module['attributes']['vcs-repo']['identifier'] == f'{github_organization}/{repository_name}':
            return True

    return False
