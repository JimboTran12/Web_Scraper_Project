"""
FileReader class processes input files
"""

import requests
class FileReader:
    def __init__(self, input_file_name) -> None:
        self.pages = []
        try:
            with open(input_file_name) as file:
                urls = [line.rstrip() for line in file]
            for url in urls:
                self.pages.append(requests.get(url))
        except:
            print("Error reading file")
        

    def get_pages(self):
        return self.pages