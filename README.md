# Web Scraper for SIUE's The Alestle URLs in Text File 
**IMPORTANT: Only works for https://www.alestlelive.com**

This Python program is designed to visit each URL for The Alestle's web pages listed in a text file and scrape or download the content from those URLs. It serves as a versatile tool for extracting information from various web resources efficiently.

## Features

- **URL Extraction**: The program parses a text file containing a list of URLs and extracts each URL for further processing.
- **Headline Extraction**:  It visits each URL and extracts the headline from the web page.
- **Content Extraction**: It visits each URL and extracts the content from the web page.



## Usage

1. **Input File**: Prepare a text file containing a list of URLs, with each URL on a separate line.
2. **Python Environment**: Ensure that you have Python installed on your system.
3. **Install Dependencies**: Install the required Python packages by running `conda install [package_name]`.
4. **Run the Program**: Execute the main Python script `main.py`.
5. **Output**: The program will process each URL, extract the content, and save it to an external `.txt` file.

## Configuration

- **URL File Path**: Specify the path to the text file containing the list of URLs.
- **Content Extraction Method**: Choose the desired method for extracting content from the web pages (e.g., using BeautifulSoup, etc.).
- **Download Options**: Enable or disable the downloading of resources linked within the web pages.
- **Output Directory**: Set the directory where the scraped content will be saved.

## Example

Suppose you have a text file named `input.txt` with the following content:

https://example.com/page1
https://example.com/page2
https://example.com/page3


You can run the program with the default configuration to visit each URL, extract the content, and save it in the specified output directory.

## Dependencies

- **Python 3.12.1**: The program is compatible with Python 3.x versions.
- **Requests**: Used for making HTTP requests to retrieve web pages.
- **BeautifulSoup**: A Python library for pulling data out of HTML and XML files.


## Acknowledgments

- The development of this program was inspired by the need to efficiently scrape web content for various applications.
- Special thanks to the developers of Requests and BeautifulSoup for providing powerful tools for web scraping in Python.


