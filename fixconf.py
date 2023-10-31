import re

def fix_conf():
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
