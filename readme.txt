# My-Zootopia

This project fetches animal information from an external API and generates a simple HTML page to display it.

## Overview

My-Zootopia allows users to input an animal name, retrieves corresponding data from the API Ninjas Animals API, and then displays the animal's details (diet, location, type) in an HTML format.

## Features

* Fetches animal data from the API Ninjas Animals API.
* Generates an HTML page displaying animal information.
* Uses a template HTML file for consistent output.
* Handles API errors and provides user-friendly messages.
* Loads API keys from a `.env` file for security.

## Prerequisites

* Python 3.x
* `pip` (Python package installer)
* An API key from [API Ninjas Animals API](https://api-ninjas.com/api/animals)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/D-G-B/My-Zootopia.git
    cd My-Zootopia
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    * In the root directory of the project, create a file named `.env`.
    * Add your API key to the `.env` file:

        ```
        API_KEY=your_api_key_here
        ```

    * **Note:** Ensure that `.env` is in your `.gitignore` file to prevent committing your API key.

## Usage

1.  **Run the script:**

    ```bash
    python animals_web_generator.py
    ```

2.  **Enter the animal name** when prompted.

3.  The script will generate an `animals.html` file in the project directory, which you can open in your web browser.

## Project Structure

My-Zootopia/
├── .venv/                # Virtual environment (ignored by Git)
├── animals.html         # Generated HTML output
├── animals_template.html  # HTML template
├── animals_web_generator.py # Main Python script
├── data_fetcher.py       # API fetching logic
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md             # Project documentation

## Dependencies

* `requests`: For making HTTP requests.
* `python-dotenv`: For loading environment variables.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License. See https://opensource.org/licenses/MIT for details.