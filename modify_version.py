import sys

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # APP_VERSION
    content = content.replace("APP_VERSION='v29'", "APP_VERSION='v30'")

    # Changelog
    # Let's see how the changelog looks. Where is the changelog in the file?
    pass

update_file("index.html")
