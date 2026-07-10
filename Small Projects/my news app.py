import requests

apikeyAPI_KEY = '093dfd99e7b14de892b7ab73e0187ab5'
url = 'https://newsapi.org/v2/top-headlines'
Trump = "https://newsapi.org/v2/top-headlines?q=trump&apiKey=093dfd99e7b14de892b7ab73e0187ab5"

forai = "https://newsapi.org/v2/everything?q=artificial intelligence&from=2025-8-1&sortBy=popularity&apiKey=093dfd99e7b14de892b7ab73e0187ab5"

forbitcoin = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=093dfd99e7b14de892b7ab73e0187ab5"

forapple = "https://newsapi.org/v2/everything?q=apple&from=2025-08-31&to=2025-08-31&sortBy=popularity&apiKey=093dfd99e7b14de892b7ab73e0187ab5"

nextweb = "https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey=093dfd99e7b14de892b7ab73e0187ab5"

a1 = input("Which headline do you want to read?: ")

try:

    if a1.lower() == "trump":
        e1 = requests.get(Trump)
        data = e1.json() # Get the JSON data from the response
        print(f"Here is your news about Trump:")
        for article in data['articles']: # Loop through the articles
            print(" -", article['title']) # Print each title

    elif a1.lower() == "ai":
        e2 = requests.get(forai)
        data = e2.json()
        print(f"Here is your news about AI:")
        for article in data['articles']:
            print(" -", article['title'])


    elif a1.lower() == "bitcoin":
        e3 = requests.get(forbitcoin)
        data = e3.json()
        print(f"Here is your news about Bitcoin:")
        for article in data['articles']:
            print(" -", article['title'])


    elif a1.lower() == "apple":
        e4 = requests.get(forapple)
        data = e4.json()
        print(f"Here is your news about Apple:")
        for article in data['articles']:
            print(" -", article['title'])


    elif a1.lower() == "nextweb":
        e5 = requests.get(nextweb)
        data = e5.json()
        print(f"Here is your news from TechCrunch and The Next Web:")
        for article in data['articles']:
            print(" -", article['title'])
    else:
        print("We dont have this news")

except ValueError as py:
    print("Failed to give you the funcking news, you niggardly ducker")
    
    
