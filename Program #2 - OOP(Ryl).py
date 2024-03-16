import pyfiglet
from colorama import Fore

name = str(input("\033[92m Enter your name here: "))
dream_job = str(input("\033[91m Enter your dream job here: "))

styled_name = pyfiglet.figlet_format("Hi, I'm " + name + "!", font= "doom")
print(Fore.CYAN + styled_name)
styled_dream_job = pyfiglet.figlet_format("My dream job is to become a " + dream_job + "!", font= "doom")
print(Fore.GREEN + styled_dream_job)