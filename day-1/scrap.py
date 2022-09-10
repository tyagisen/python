from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read() #Reads the opened file
    soup = BeautifulSoup(content, "lxml") #By default it takes or uses python's integrated html parser in the html. So, i order to take lxml as parser we explicitly put it there as second parameter.
    # print(soup.prettify())
    # tags = soup.find("h1") #It finds the first h1 tags and store in tags variable.
    all_tags = soup.find_all("h1") #It takes all values contained in h1 tags.
    # print(all_tags)
    for tag in all_tags:
        print(tag.text)

"""This is just the example but in real projects it is not as easy as it is seen."""