import json

file = open('PycharmProjects/pythonProject/fakeSitesList.json')
data = json.load(file)

search = input("\nEnter the url:")

if search in data['urls']:
    print("%s !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" %search)
    print("The value of", search, "is", data[search])
else:
    # Print the message if the value does not exist
    print("%s is not found in JSON data" %search)

file.close()