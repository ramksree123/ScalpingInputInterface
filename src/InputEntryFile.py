import requests
print("Hello World")
print("How are you")
i=1
while i==1:
    userInput=input("Please enter the trend 1. Up Trending 2. Down Trending 3. Ranging 4. Exit 5. Fetch Status?  ")
    if userInput=="1":
        r = requests.get("http://127.0.0.1:8000/apis/updateTrendStatus?updateTrendStatus=true&trendStatus=1")
        print(r.status_code)
        userInput="Up Trending"
    elif userInput=="2":
        r = requests.get("http://127.0.0.1:8000/apis/updateTrendStatus?updateTrendStatus=true&trendStatus=2")
        print(r.status_code)
        userInput="Down Trending"
    elif userInput=="3":
        r = requests.get("http://127.0.0.1:8000/apis/updateTrendStatus?updateTrendStatus=true&trendStatus=3")
        print(r.status_code)
        userInput="Ranging"
    elif userInput=="4":
        r = requests.get("http://127.0.0.1:8000/apis/updateTrendStatus?updateTrendStatus=true&trendStatus=4")
        print(r.status_code)
        userInput="Exiting the App"
        i=2
    elif userInput=="5":
        r = requests.get("http://127.0.0.1:8000/apis/fetchTrendStatus?fetchTrendStatus=true")
        print(r.status_code)
        print(r.headers)
        print(r.content)
        print(r.text)
        userInput="Ranging"
    else:
        userInput="Wrong Input"
    print(userInput)