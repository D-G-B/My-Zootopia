import json
import requests


def load_data(file_path):
    """
    Loads a JSON file and returns its contents as a Python object.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict or list: The parsed JSON data.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def make_animals_html(data, animal_name):
    """
    Generates an HTML list of animal information from the provided data.

    Args:
        data (list of dict): A list of dictionaries, each representing an animal with its attributes.
        animal_name (str): The name of the animal that was searched.

    Returns:
        str: A string containing HTML markup for the animals.
    """
    if not data:
        return f'<h2> ): The animal "{animal_name}" does not exist in the API. :( </h2>'

    output = ""

    for animal in data:
        list_html = '<li class="cards__item">'

        if name := animal.get("name"):
            list_html += f'<div class="card__title">{name}</div>'

        list_html += '<div class="card__text">'
        list_html += '<ul class="card__details">'

        if diet := animal.get("characteristics", {}).get("diet"):
            list_html += f'<li class="card__detail-item"><strong>Diet:</strong> {diet}</li>'

        if location := animal.get("locations", [None])[0]:
            list_html += f'<li class="card__detail-item"><strong>Location:</strong> {location}</li>'

        if ani_type := animal.get("characteristics", {}).get("type"):
            list_html += f'<li class="card__detail-item"><strong>Type:</strong> {ani_type}</li>'

        list_html += '</ul></div></li>'
        output += list_html

    return output


def read_template(html_path):
    """
    Reads an HTML template file and returns its contents as a string.

    Args:
        html_path (str): The path to the HTML template file.

    Returns:
        str: The contents of the HTML file.
    """
    with open(html_path, "r") as file:
        file_data = file.read()
    return file_data


def write_html_file(html_content):
    """
    Writes the generated HTML content to a file.

    Args:
        html_content (str): The HTML content to write into the file.

    Returns:
        None
    """
    with open("animals.html", "w") as file:
        file.write(html_content)

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


def main():
    """
    Orchestrates the process of loading animal data, generating HTML content,
    and writing the final HTML output to a file.

    Returns:
        None
    """
    # Ask user for animal
    animal = input("Enter the animal name you would like to add: ")

    # Get animal from api
    name = animal
    animals_data = get_animal_json(name)

    # Read the HTML template
    template = read_template('animals_template.html')

    # Generate the string of animal information
    animals_string = make_animals_html(animals_data, name)

    # Replace the placeholder in the template
    output_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_string)

    # Write the new HTML file
    write_html_file(output_html)


if __name__ == "__main__":
    main()
