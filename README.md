# Google News Web Scraper

This project is a Python application that utilizes Beautiful Soup for web scraping and PySimpleGUI for a simple graphical user interface (GUI) to scrape Google News headlines and links and save them to a text file.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The application provides a user interface where the user can enter a URL (Google News link) and specify the name of the file to save the scraped data. Upon clicking the "Scrap!" button, the program fetches the news articles and their links, and then writes this information to a text file.

## Requirements

- Python 3.x
- Libraries:
  - PySimpleGUI
  - BeautifulSoup4
  - requests

You can install the necessary libraries via pip:

  ```bash
  pip install PySimpleGUI beautifulsoup4 requests


## Usage

Clone or download the repository.
Install the required dependencies.
Run the Python script scraping_gui.py.
Enter a Google News URL and specify the file name for the output.
Click the "Scrap!" button to start the scraping process.
The scraped headlines and links will be saved to a text file with the provided name.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the MIT License.


