# WebScraping_Python
# Web Scraping Script

This Python script is designed to scrape links and images from a given URL using the BeautifulSoup library. The scraped data is then saved to a CSV file.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:

## Usage

1. Open the `webscarping.py` file in a text editor.
2. Modify the `url` variable to the URL you want to scrape.
3. Save the changes and run the script.

The script will scrape the links and images from the specified URL and save the data to a CSV file named `scraped_data.csv` in the same directory as the script.

## Script Breakdown

Here's a breakdown of the script's functionality:

1. The script imports the necessary libraries: `BeautifulSoup` from `bs4` and `requests` for making HTTP requests.
2. The `requests.get()` function is used to fetch the HTML content of the specified URL.
3. The `BeautifulSoup` object is created from the fetched HTML content.
4. The `find_all()` method is used to find all `<a>` (link) and `<img>` (image) tags in the HTML.
5. The script iterates through the found links and images, extracting the `href` (for links) and `src` (for images) attributes, as well as the link text and image alt text.
6. The extracted data is stored in a list of dictionaries.
7. The `csv` module is used to create a CSV file and write the scraped data to it.
8. The script prints a message indicating that the web scraping process is complete and the data has been saved to the CSV file.

## Note

Please note that web scraping can be against the terms of service of some websites. Always check the website's policies before scraping and use this script responsibly.
