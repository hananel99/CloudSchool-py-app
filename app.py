from flask import Flask, render_template, request
import boto3
import requests
import urllib.request
import logging
import logging.config
import hvac
import re
from description import get_description

AWS_REGION_NAME = 'us-east-1'

boto3_logs_client = boto3.client("logs", region_name=AWS_REGION_NAME)

log_level = {
  'CRITICAL' : 50,
  'ERROR'	   : 40,
  'WARN'  	 : 30,
  'INFO'	   : 20,
  'DEBUG'	   : 10
}
logger = logging.getLogger("werkzeug")


app = Flask(__name__)

# Specify the path to your app.conf file
file_path = "/home/bob/myapp/app.conf"


# Read the file
with open(file_path, 'r') as file:
    content = file.read()

# Use a regular expression to remove newlines followed by a double quote
cleaned_content = re.sub(r'\n"', '"', content)

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(cleaned_content)

# Load the configuration from app.conf file
app.config.from_pyfile("app.conf", silent=False)

MYSQL_ENDPOINT = (app.config.get("MYSQL_ENDPOINT")).split(":")[0]
LOG_LEVEL = app.config.get("LOG_LEVEL")
VAULT_ENDPOINT = app.config.get("VAULT_ENDPOINT")
VAULT_TOKEN = app.config.get("VAULT_TOKEN")
VAULT_PATH_TO_CREDS = app.config.get("VAULT_PATH_TO_CREDS")
APPLICATION_VERSION = app.config.get("APPLICATION_VERSION")
VAULT_CLIENT = hvac.Client(url=VAULT_ENDPOINT, token=VAULT_TOKEN)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route('/checkhealth', methods=['GET'])
def check_health():
    return "Server is healthy"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Make a request to the API
        response = requests.get(url="https://www.sefaria.org/api/calendars").json()

        # Retrieve the data from the API
        title = response["calendar_items"][0]["title"]["en"]
        title_info = response["calendar_items"][0]["displayValue"]["en"]
        description = get_description()
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
    app.run() #host= "0.0.0.0", port = 8080, debug=True
