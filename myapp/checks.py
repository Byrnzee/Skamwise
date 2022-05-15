import json

def urlCompare(url):
    file = open('myapp/static/fakeSitesList.json')
    data = json.load(file)

   # print(data["urls"])

    if url in data['urls']:
        return True

        # print("%s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" % url)
        # print("The value of", url, "is", data["urls"].index(url))
    else:
        return False

        # Print the message if the value does not exist
        # print("%s is not found in JSON data" % url)

    file.close()