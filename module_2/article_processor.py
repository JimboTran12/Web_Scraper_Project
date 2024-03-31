"""
HtmlProcessor class process each of its html
pages and output filtered articles into a desfinated
directory
"""

from bs4 import BeautifulSoup

class HtmlProcessor:
    def __init__(self, pages, output_dir) -> None:
        self.output_dir = output_dir
        self.pages = pages

    def process(self):    

        for count, page in enumerate(self.pages, start=1):
            string = ""
            soup = BeautifulSoup(page.text, "html.parser")

            headline = soup.find_all(class_ = "asset-header")[0].find_all(class_ = "headline")[0].find_all("span")[0]
            string += headline.string.upper() + "\n\n"

            divs = soup.find_all(id = "article-body")
            for div in divs:
                ps = div.find_all("p")
                for p in ps:
                    string += p.string + "\n"
            
            with open(self.output_dir + "/url" + str(count) + ".txt","w") as out_file:
                out_file.write(string)


    def get_output_filenames(self):
        file_names = []
        URLnum = 1
        for page in self.pages:
            name = self.output_dir + "/url" + str(URLnum) + ".txt"
            file_names.append(name)
            URLnum += 1
        return file_names
