import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=en"

browser.open(url)
print(browser.get_url())

