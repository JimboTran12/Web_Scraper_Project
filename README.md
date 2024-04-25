# Web Scraper for SIUE's The Alestle URLs in Text File 
**IMPORTANT: Only works for https://www.alestlelive.com**

This Python program is designed to visit each URL for The Alestle's web pages listed in a text file and scrape or download the content from those URLs. It serves as a versatile tool for extracting information from various web resources efficiently.

## Features

- **URL Extraction**: The program parses a text file containing a list of URLs and extracts each URL for further processing.
- **Headline Extraction**:  It visits each URL and extracts the headline from the web page.
- **Content Extraction**: It visits each URL and extracts the content from the web page.

# Web Scraper for SIUE's The Alestle URLs in Text File

## Description

This Python program is designed to visit each URL for The Alestle's web pages listed in a text file and scrape or download the content from those URLs. It serves as a versatile tool for extracting information from various web resources efficiently.

## Features

- **URL Extraction**: The program parses a text file containing a list of URLs and extracts each URL for further processing.
- **Headline Extraction**:  It visits each URL and extracts the headline from the web page.
- **Content Extraction**: It visits each URL and extracts the content from the web page.

## Running Tests

To run the tests for this project, you will need to use pytest. If you haven't installed pytest yet, you can do so by running the following command:

```bash
conda install pytest
```
Once pytest is installed, navigate to the project directory and run the following command:
```bash
pytest test.py
```

### What is being tested?
The tests in this project cover the following functionalities:

1. **URL Extraction**: Tests if the FileReader class correctly parses a text file containing a list of URLs and extracts each URL for further processing.
2. **HTML Page Retrieval:** Tests if the FileReader class correctly retrieves the HTML pages from the URLs.
3. **Content Extraction:**  Tests if the HtmlProcessor class correctly processes the HTML pages and extracts the content from the web pages.
4. **Output File Creation**: Tests if the HtmlProcessor class correctly creates output files with the extracted content.
5. **HtmlProcessor get_output_filenames method**: Tests if the HtmlProcessor class correctly returns the filenames of the output files.
6. **FileReader Initialization**: Tests if the FileReader class is correctly initialized with the given input file name.
7. **HtmlProcessor Initialization**: Tests if the HtmlProcessor class is correctly initialized with the given pages and output directory.
8. **AI Initialization:Tests if the AI class is correctly initialized with the given files and output directory.

   Each of these tests is designed to ensure that the individual components of the project are working as expected, and that they correctly interact with each other to produce the expected output.

## Usage

1. **Input File**: Prepare a text file containing a list of URLs, with each URL on a separate line.
2. **Python Environment**: Ensure that you have Python installed on your system.
3. **Install Dependencies**: Install the required Python packages by running `conda install [package_name]`.
4. **Run the Program**: Execute the main Python script `main.py`.
5. **Output**: The program will process each URL, extract the content, and save it to an external `.txt` file.

## OpenAI API Demo

This repository contains a simple demonstration of how to use the OpenAI API to interact with powerful GPT models.

### Creating an OpenAI API Account and Generating API Key

To access OpenAI's powerful GPT models and utilize its API, you'll need to create an account on the OpenAI platform and generate an API key. Here's a step-by-step guide:

1. **Sign Up for an Account**:
   - Go to the [OpenAI website](https://openai.com/) and sign up for an account if you haven't already. Follow the instructions to complete the registration process.

2. **Navigate to API Settings**:
   - After signing in, navigate to your account settings. You can find this by clicking on your profile icon or by directly visiting the account settings page.

3. **Generate an API Key**:
   - Once you're in the account settings, find the section related to API access or API keys. Click on the option to generate a new API key. You might be asked to provide additional information or agree to terms of service.

4. **Copy the API Key**:
   - After generating the API key, it will be displayed on the screen. Copy this key and store it securely. Treat your API key like a password, as it grants access to your OpenAI account and can incur charges based on usage.

5. **Add API key to .bash_profile**:
    - Open Terminal: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
    - Edit Bash Profile: Use the command nano ~/.bash_profile or nano ~/.zshrc (for newer MacOS versions) to open the profile file in a text editor.
    - Add Environment Variable: In the editor, add the line below, replacing your-api-key-here with your actual API key:
    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```
    - Save and Exit: Press Ctrl+O to write the changes, followed by Ctrl+X to close the editor.
    - Load Your Profile: Use the command source ~/.bash_profile or source ~/.zshrc to load the updated profile.
    - Verification: Verify the setup by typing echo $OPENAI_API_KEY in the terminal. It should display your API key. 

### Making a Simple API Call in macOS using Python

Here's how you can use the generated API key to make a simple API call in macOS using Python:

1. **Install the OpenAI Python Library:**
   - Before making API calls, ensure you have the OpenAI Python library installed. You can install it via conda:

   ```bash
   conda install openai
   ```
2. **Write Python Script:**
   - Before making API calls, ensure you have the OpenAI Python library installed. You can install it via conda:

   ```python
   import openai
   ```
3. **Make API Call:**
   - Use the library functions to make API calls. For example, to use the completion endpoint of the API:

   ```python
   client = OpenAI()
   completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role": "assistant", "content":  "~Article content~"},
                    {"role": "user", "content": "Please make the article concise, up to 50 words"}
                    ]
                    )
   ```
4. **Print or Use Response:**
   - Once you receive the response, you can print it or utilize it as required. For example:

   ```python
   print(completion.choices[0].message.content)
   ```

5. **Write Python Script:**
   - Execute the Python script in your terminal:

   ```bash
   python run.py
   ```
   Ensure that you are in the directory containing your Python script.

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


