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
from openai import OpenAI
from module_1.page_reader import FileReader
from module_2.article_processor import HtmlProcessor
from module_3.open_ai_api import AI


def main():
    htmls = FileReader("Data/raw/input.txt") #Retrieve full html page from all links in input.txt
    pages = htmls.get_pages() #store all html pages in pages
    html_processor = HtmlProcessor( pages, "Data/processed")
    html_processor.process() #Extracts the content from the html pages then save them in text files in the Data/processed directory
    ai = AI(html_processor.get_output_filenames(), "Data/generated")
    ai.generate() #Use openAI API to write concise version of each rticle and save them in text files in the Data/generated directory


if __name__ == "__main__":
    main()