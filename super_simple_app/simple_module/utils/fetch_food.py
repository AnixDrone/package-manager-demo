import requests
import os


def fetch_food_generic(params, endpoint):
    """
    Fetches food data from the USDA Food Composition Databases API
    :param params: the parameters to send to the API
    :param endpoint: the endpoint to send the request to
    :return: the response from the API
    """
    api_key = os.environ.get('TOKEN')
    base_url = 'https://api.nal.usda.gov/fdc'

    params['api_key'] = api_key

    response = requests.get(os.path.join(base_url, endpoint), params=params)

    if response.status_code != 200:
        raise Exception(
            'The request to the USDA Food Composition Databases API failed.')

    # Return the response
    return response.json()
