#!/usr/bin/env python3


#====#^#====#
# Imports
import random
import json
import os


#====#^#====#
# Colors
cyan = '\033[1;96m'       # Cyan
reset = '\033[0m'         # Reset


#====#^#====#
# Clear Terminal
os.system("cls" if os.name == "nt" else "clear")
print(f"{cyan}Hi! Let's talk...")


#====#^#====#
# Brain
with open('brain.json', 'r+') as _brain:
    brain = dict(json.load(_brain))

    learned = len(brain)
 
    print(f"{cyan}Learned words:{reset} {learned}")

    while True:
        user_input = input(f"\n{cyan}>>>{reset} ") .lower().strip()

        if user_input[-1] == "?":
            user_input = user_input.split("?")[0].strip()


        try:        
            print(f"{cyan}" + brain[user_input])

        except KeyError:
            learn = input(f"{cyan}{user_input}{reset}\n\n{cyan}>>>{reset} ")
            brain[user_input] = learn
            json.dump(brain, open("brain.json", 'w'), indent=4 )