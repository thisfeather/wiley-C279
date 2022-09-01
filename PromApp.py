import logging
from prometheus_client import start_http_server
import prometheus_client as prom  ## Added for Prometheus

import time
from random import seed
from random import randint


logging.basicConfig(filename="record.log", level=logging.DEBUG)

# Try prometheus metric here:
counter = prom.Counter("user_served", "already responded to user ID")


# @c.inc()
def number_stream():

    userID = 0

    while userID != 500000:

        userID = randint(0, 1000001)
        userInput = randint(0, 1001)
        sleepLength = randint(0, 11)

        if userID % 17 == 0 or userID % 23 == 0: # Set some jackpot just in case
            print("Jackpot hit! User ID is:", userID)

            # Allow any error actions here, e.g. loop breaking

        print("\n\nUser ID is:", userID)

        # implement cases of logging:
        if userID % 5 == 0:
            print("Info: UserID is a multiple of 5:", userID)
            logging.info("Info log information - multiple of 5")

        if userID % 16 == 0:
            print("Warning: UserID is a multiple of 16:", userID)
            logging.warning("Warning log info - multiple of 16")

        if userID % 100 == 0:
            print("Debug: UserID is a multiple of 100:", userID)
            logging.debug("Debug log info - multiple of 100")

        if userID % 1000 == 0:
            print("Critical: UserID ends with 000:", userID)
            logging.critical("Critical log info - multiple of 1,000")

        if userID % 10000 == 0:
            print("Error: UserID ends with 0000:", userID)
            logging.error("Error log info - multiple of 10,000")


        printString = ""
        repeat = userID if userID < 100 else int(userID/10000)
        for i in range(repeat):
            printString += str(userID)

        seconds = sleepLength

        print("Will sleep for", seconds, "second after printing this:")
        print(printString)

        # Premetheus counter
        counter.inc()

        time.sleep(seconds)


    return 0



if __name__ == '__main__':
    prom.start_http_server(8001)   ## Start server with Prometheus client itself to post results
    number_stream()


