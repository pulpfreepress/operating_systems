"""Multi-Threaded Vacation

   Demonstrates how a multi-threaded application behaves.
"""

import threading
import time

_thirsty = True
_hungry = True

def fetch_drink():
    steps_to_the_bar = range(500)
    for i in steps_to_the_bar:
        if (i % 99) == 0:
            print()
            print(" Fetching Drinks  ", end="")
            time.sleep(.10)
        else:
            print(".",end="")
    global _thirsty
    _thirsty = False
    print()




def fetch_food():
    steps_to_the_grill = range(500)
    for i in steps_to_the_grill:
        if (i % 99) == 0: 
            print()
            print(" Fetching Food ", end="")
            time.sleep(.10)
        else:
            print(".", end="")
    global _hungry
    _hungry = False
    print()




def main():
    global _hungry
    global _thirsty
    threads = {}
    threads['drink_fetcher'] = threading.Thread(target=fetch_drink)
    threads['food_fetcher'] =  threading.Thread(target=fetch_food)
    for key in threads:
        threads[key].start()

    while _hungry or _thirsty:
        print("***** Relaxing *****\n")
        print('\a')
        time.sleep(.10)
        
       
        

if __name__ == "__main__":
    main()