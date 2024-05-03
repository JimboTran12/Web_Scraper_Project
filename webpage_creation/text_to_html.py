from xml.etree import ElementTree as ET

def txt_to_html(txt_file, html_file):
  """
  Converts a text file with header and paragraph to an HTML file.
  Make necessary changes for multiple news articles. This script is
  only for one news article.

  Args:
      txt_file (str): Path to the text file.
      html_file (str): Path to the output HTML file.
  """
  # Read text file content
  with open(txt_file, 'r') as f:
    contentALL = f.read()
  contentALL = contentALL.split("\n\n\n")
  root = ET.Element("html")
  head = ET.SubElement(root, "head")
  title = ET.SubElement(head, "title")
  title.text = "My News Aggregation Site"
  body = ET.SubElement(root, "body")


  for article in contentALL:
  # Extract header and paragraph, since you will be having multiple articles the logic will
  # change for the code given below. 
    content = article.split("\n")

    header = content[0].strip()
    paragraph = "".join(content[1:]).strip()

    h1 = ET.SubElement(body, "h1")
    h1.text = header
    p = ET.SubElement(body, "p")
    p.text = paragraph

  # Write HTML tree to file
  with open(html_file, 'wb') as f:
    tree = ET.ElementTree(root)
    tree.write(f, encoding='utf-8')




def congregrate(dir_path, output_file):
    string = ""
    for i in range(1, 11):
        with open(f"{dir_path}/url{i}.txt", 'r') as f:
            string += f.read() + "\n\n\n"
    with open(output_file, 'w') as f:
        f.write(string)

txt_file = "webpage_creation/input.txt"
html_file = "webpage_creation/all_news_articles.html"
congregrate("Data/generated", "webpage_creation/input.txt")
txt_to_html(txt_file, html_file)
print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")
