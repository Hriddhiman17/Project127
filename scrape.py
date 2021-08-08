import csv
import time
import random
webLink = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# time.sleep(10)

def scrape():
    headers = ["name", "distance", "mass", "radius"]
    data = []
    for i in random.randint(99, 999):
        print(i)

scrape()
