import webbrowser, requests, bs4

"""#webbrowser.open('https://automatetheboringstuff.com/') # Open the given webpage
resp = requests.get('https://www.uleth.ca/future-student/sites/default/files/to-do-list.pdf') # returns the response from the targeted websited
resp.raise_for_status() # checking the response status is ok or 404
playFile = open('RomeoAndJuliet.pdf', 'wb')  # creates a file with given file name in current folder in not exists
for chunk in resp.iter_content(100000):  # iter_content is a response function to iterate the chunks(100000 is a good number)
    playFile.write(chunk)           # Writing to file in series of chunks downloaded
playFile.close()"""

corona_file_india = requests.get('https://www.worldometers.info/coronavirus/')
corona_file_soup = bs4.BeautifulSoup(corona_file_india.text, 'html.parser')
elem_soup = corona_file_soup.select('.maincounter-number')
print(elem_soup)