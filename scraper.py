import mechanicalsoup
import pandas as pd
import sqlite3

# create browser object & open URL
browser = mechanicalsoup.StatefulBrowser()
browser.open("https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions")


th = browser.page.find_all("th", attrs={"class": "table-rh"})
distribution = [value.text.replace("\n", " " ) for value in th]
distribution = distribution[:98]
#finding the table end tablw header index value
print(distribution.index("Zorin OS "))

#storing td tags text
td= browser.page.find_all("td")
columns = [value.text.replace("\n", " " ) for value in td]
columns = columns[6:1084]    #spitling list by using following/
#print(columns.index("AlmaLinux Foundation "))
#print(columns.index("Binary blobs "))


print(columns)

column_names = ["Founder", 
                "Maintainer", 
                "Initial_Release_Year", 
                "Current_Stable_Version", 
                "Security_Updates", 
                "Release_Date", 
                "System_Distribution_Commitment", 
                "Forked_From", 
                "Target_Audience", 
                "Cost", 
                "Status"]

dictionary = {"Distribution": distribution}

for idx, key in enumerate(column_names):        #qs
    dictionary[key] = columns[idx:][::11]

df = pd.DataFrame(data = dictionary)
print(df)


connection = sqlite3.connect("linux_distro.db")
cursor = connection.cursor()

cursor.execute("create table linux (Distribution, " + ",".join(column_names)+ ")") 

for i in range(len(df)):
    cursor.execute("insert into linux values (?,?,?,?,?,?,?,?,?,?,?,?)", df.iloc[i])


connection.commit()

connection.close()


