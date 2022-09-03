import os
import json


def load_dev_config():
    with open('dev.json') as json_file:
        return json.load(json_file)


def load_config():
    if os.getenv('IS_DOCKER_ENVIRONMENT') is not None:
        if os.getenv('IS_DOCKER_ENVIRONMENT') == 'true':
            config = {}

            if os.getenv('TFC_TOKEN') is None:
                print('Variable TFC_TOKEN has not been set')
                exit(1)
            else:
                config['tfc_token'] = os.getenv('TFC_TOKEN')

            if os.getenv('TFC_ORGANIZATION') is None:
                print('Variable TFC_ORGANIZATION has not been set')
                exit(1)
            else:
                config['tfc_organization'] = os.getenv('TFC_ORGANIZATION')

            if os.getenv('TFC_CLIENT_NAME') is None:
                print('Variable TFC_CLIENT_NAME has not been set')
                exit(1)
            else:
                config['tfc_client_name'] = os.getenv('TFC_CLIENT_NAME')

            if os.getenv('GH_ORGANIZATION') is None:
                print('Variable GH_ORGANIZATION has not been set')
                exit(1)
            else:
                config['gh_organization'] = os.getenv('GH_ORGANIZATION')

            if os.getenv('GH_REPOSITORY') is None:
                print('Variable GH_REPOSITORY has not been set')
                exit(1)
            else:
                config['gh_repository'] = os.getenv('GH_REPOSITORY')

            return config
    else:
        return load_dev_config()
