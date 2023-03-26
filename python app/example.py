
def parasha():

    if button == "info":
        collection = "calendars"
        response = requests.get(str(url + collection)).json()
        html_code = response



parasha()