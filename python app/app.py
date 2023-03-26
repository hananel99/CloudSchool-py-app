from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Make a request to the API
        response = requests.get(url="https://www.sefaria.org/api/calendars").json()

        # Retrieve the data from the API
        title = response["calendar_items"][0]["title"]["en"]
        title_info = response["calendar_items"][0]["displayValue"]["en"]
        description = response["calendar_items"][0]["description"]["en"]

        # Check if the API request was successful
        try:
            # Retrieve the data from the API
            en_data = {
                "name": title,
                "info": title_info,
                "description": description
            }

            # Render the data on a template
            return render_template("index.html", data=en_data)
        except:
            # Return an error message if the API request was not successful
            return "Could not retrieve data from API"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=3000)
