import requests
from bs4 import BeautifulSoup

def get_description():
    # URL of the web page
    url = "https://www.hebcal.com/sedrot/lech-lecha-20231028?utm_source=js&utm_medium=api"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the container with class "container"
        container = soup.find("div", class_="container")

        # Find the row with class "row" within the container
        row = container.find("div", class_="row")

        # Find the column with class "col" within the row
        col = row.find("div", class_="col")

        # Find all <p> elements within the column
        paragraphs = col.find_all("p")

        # Print the text in each <p> element
        description = []
        for paragraph in paragraphs:
            description.append(paragraph.get_text())
        return "".join(description)
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)