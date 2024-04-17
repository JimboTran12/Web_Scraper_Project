import pytest
import requests
from bs4 import BeautifulSoup
from module_1.page_reader import FileReader
from module_2.article_processor import HtmlProcessor
from module_3.open_ai_api import AI

from run import main

def test_url_extraction(): #Test if the urls are extracted from the input file
    reader = FileReader('Data/raw/input.txt')
    pages = reader.get_pages()
    assert isinstance(pages[0], requests.models.Response) #The type of the object should be a response object

def test_html_page_retrieval(): #Test if the html pages are retrieved from the urls
    reader = FileReader('Data/raw/input.txt')
    pages = reader.get_pages()
    assert len(pages) == 10  #10 pages should be loaded because of the 10 urls in the input file

def test_content_extraction(): #Test if the content is extracted from the html pages
    reader = FileReader('Data/raw/input.txt')
    pages = reader.get_pages()
    processor = HtmlProcessor(pages, "Data/processed")
    with open('Data/processed/url1.txt', 'r') as f:
        content = f.read()

    assert isinstance(content, str) and len(content) > 0#The content should be a string and should not be empty

def  test_html_processor_get_headline(): #Test if the headline is extracted from the html pages
    reader = FileReader('Data/raw/input.txt')
    pages = reader.get_pages()
    processor = HtmlProcessor(pages, "Data/processed")
    processor.process()
    with open('Data/processed/url1.txt', 'r') as f:
        content = f.readline()
    assert content == 'COST-FRIENDLY COLLEGE DATES FOR VALENTINE’S DAY\n'
