"""
After pressing RUN, enter a name (ONLY FIRST NAME) or left it empty and let it choose a
random name. 😊
---------------| INPUT EXAMPLES |--------------
Matt
Xi
Gagan
Nazir
------------------| NOTE |---------------------
It mostly supports names that are used in United States of America (USA).
Names used by ethnic groups like Americans, 
Asians, Africans, Latinos, Indians etc.
-----------------------------------------------
Author: OR!ON
Version: 1.0-20200120 
-----------------------------------------------
All Rights Reserved (c) 2020 OR!ON

"""

import json
import random
from urllib import request
from urllib import error


url = "https://raw.githubusercontent.com/Or-i0n/gender_by_name/master/unique2.json"

try:
    raw = request.urlopen(url)
    dbs = json.loads(raw.read())
    
except error.HTTPError as database_err:
    print("Dataset Error! Unable to load dataset.")
else:
    dbs_names = tuple(dbs.keys())
    
    username = input().capitalize()
    if not username:
        username = random.choice(dbs_names)
        
    print(f"Name: {username}\n")

    print("Guessing 🤔 gender...", flush=True)

    if username in dbs:
        # Occurance of name as a male or female.
        m, f = dbs[username].values()
        total = m + f
        # Male and Female Possibility
        male_possib = round(m / total * 100)
        female_possib = round(f / total * 100)

        if m > f:
            print(f"I'm {male_possib}% sure. He's a MALE ♂️!")
        elif f > m:
            print(f"I'm {female_possib}% sure. She's a FEMALE ♀️!")
        else:
            print(f"I'm 50% sure. It's either MALE ♂️ or FEMALE ♀️!")
    else:
        print(f"Sorry 😔 don't know about '{username}'!")
        
    print("\n\n(Based on US Social Security records 1880-2018)")

