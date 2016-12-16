#Cesar Neri
#December 16, 2016

#Exercise 11-2 From Murach's Python programming Book



#!/usr/bin/env python3

from datetime import timedelta
from datetime import datetime

def main():
    print("The Timer Program\n")
    
    #Create current time object (start)
    input("Press Enter to start...")
    start = datetime.now()
    print("Start time: " + str(start))
    
    print()

    #Create current time object (finish)
    input("Press Enter to stop...")
    end = datetime.now()
    print("End time: " + str(end))
    
    interval = end - start

    #calculate data
    minutes = interval.seconds // 60
    seconds = interval.seconds % 60

    hours = minutes // 60
    minutes = minutes % 60

    print("ELAPSED TIME")
    print("Hours/Minutes:\t" + str(hours) + ":" + str(minutes))
    print("Seconds:\t" + str(seconds))


if __name__ == "__main__":
    main()
    
