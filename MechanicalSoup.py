import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=en"

browser.open(url)
#print(browser.get_url())


#get HTML
browser.get_current_page()

#target the search input
browser.select_form()
browser.get_current_form().print_summary()

#search for a term
search_term = 'dog'
browser["q"] = search_term

#submit/"click" search
browser.launch_browser()
response = browser.submit_selected()

print('new url:', browser.get_url())
print('my response:\n', response.text[:500])
