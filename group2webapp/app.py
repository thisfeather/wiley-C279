from flask import Flask, 

import time
from random import seed
from random import randint

app = Flask(__name_)

@app.route('/')
def number_stream():
    
    userID = 0

    while userID != 500000:

        userID = randint(0, 1000001)
        userInput = randint(0, 1001)
        sleepLength = randint(0, 10001)

        if userID % 17 == 0 or userID % 23 == 0: # Set some jackpot just in case
            print("Jackpot hit! User ID is:", userID)

            # Allow any error actions here, e.g. loop breaking

        print("\n\nUser ID is:", userID)
        
        printString = ""
        for i in range(userID):
            printString += str(userID)

        milliseconds = int(sleepLength / 1000)

        print("Will sleep for", milliseconds, "after printing this:")
        print(printString)

        time.sleep(milliseconds)


if __name__ == '__main__':
    app.run()


