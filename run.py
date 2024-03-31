"""
Main function that first process the input file 
using FileReader class to get HTML pages. It then 
uses HtmlProcessor class to process each html pages
then output each output into a desginated folder
"""

"""
SOLID Principle used:
(S)ingle responsibility principle
For each of the two classes FileReader and HtmlProcessor,
each serves one single function to scrape the data off the
article. FileReader class processes each URL in an input file
to produce a html page using one library Requests. HtmlProcessor
class filter out each html pages to produce the only core content
of each page on separate files using one singular library BeautifulSoup.

"""

import requests
from bs4 import BeautifulSoup
from module_1.page_reader import FileReader
from module_2.article_processor import HtmlProcessor
from module_3.open_ai_api import AI


def main():
    htmls = FileReader("Data/raw/input.txt")
    pages = htmls.get_pages()
    html_processor = HtmlProcessor( pages, "Data/processed")
    html_processor.process()
    ai = AI(html_processor.get_output_filenames(), "Data/generated")
    ai.generate()


if __name__ == "__main__":
    main()