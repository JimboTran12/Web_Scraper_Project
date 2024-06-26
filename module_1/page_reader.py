"""
FileReader class processes input files from its file
name and produces html pages from the urls in the input
file.
"""

import requests
class FileReader:
    def __init__(self, input_file_name) -> None:
        self.pages = []
        self.input_file_name = input_file_name
        try:
            with open(self.input_file_name) as file:
                urls = [line.rstrip() for line in file]
            for url in urls:
                self.pages.append(requests.get(url)) #get html pages from url
        except:
            print("Error reading file")
        

    def get_pages(self):
        return self.pages