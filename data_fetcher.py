import requests

def get_animal_json(name):
    """
    Fetches animal data from the API based on provided name.

    Args: name (str): The name of the animal to search for provided by usr input

    Returns:
        list or None: A list of animal data in JSON format if successful, otherwise None.
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'e4kugb+adSUD+i3UPMNCKQ==hETJEYy9dgplQWPV'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None
