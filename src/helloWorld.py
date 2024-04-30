print("Hello World")
print("How are you")
i=1
while i==1:
    userInput=input("Please enter the trend 1. Up Trending 2. Down Trending 3. Ranging 4. Exit?  ")
    if userInput=="1":
        userInput="Up Trending"
    elif userInput=="2":
        userInput="Down Trending"
    elif userInput=="3":
        userInput="Ranging"
    elif userInput=="4":
        userInput="Exiting the App"
        i=2
    else:
        userInput="Wrong Input"
    print(userInput)