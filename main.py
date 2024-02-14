import requests
from bs4 import BeautifulSoup

def main():
    with open("input.txt") as file:
        urls = [line.rstrip() for line in file]
    pages = []
    for url in urls:
        pages.append(requests.get(url))

    URLnum = 1
    for page in pages:
        string = ""
        soup = BeautifulSoup(page.text, "html.parser")

        headline = soup.find_all(class_ = "asset-header")[0].find_all(class_ = "headline")[0].find_all("span")[0]
        string += headline.string.upper() + "\n\n"

        divs = soup.find_all(id = "article-body")
        for div in divs:
            ps = div.find_all("p")
            for p in ps:
                string += p.string + "\n"
        
        with open("url" + str(URLnum) + ".txt","w") as out_file:
            out_file.write(string)
        URLnum += 1

if __name__ == "__main__":
    main()
