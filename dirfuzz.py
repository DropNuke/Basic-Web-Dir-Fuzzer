#!/usr/bin/env python3
from colorama import init, Fore
import requests 

#Colors stuffs --------------------------------------------------------------
init()
class color:
        red = Fore.RED
        blue = Fore.BLUE
        green = Fore.GREEN
        yellow = Fore.YELLOW
        cyan = Fore.CYAN
        error = Fore.RED+"["+Fore.RESET+"-"+Fore.RED+"]"+Fore.RESET+" "
        adv = Fore.YELLOW+"["+Fore.RESET+"!"+Fore.YELLOW+"]"+Fore.RESET+" "
        ble = Fore.BLUE+"["+Fore.RESET+"*"+Fore.BLUE+"]"+Fore.RESET+" "
        reset = Fore.RESET 
#----------------------------------------------------------------------------

header = {'User-Agent':'Mozilla/5.0'}	#Set UserAgent for Requests
file = "rockyou.txt"	#Wordlist Here
#file = "wordlist.txt"	#Wordlist Here
fuzz_url = "https://underc0de.org/"	#url Here

#----------------------------------------------------------------------------

#FUNCTION MAIN---------------------------------------------------------------

def fuzzing(url, my_wordlist):

	words = []

	with open(my_wordlist, 'r', encoding="latin1") as f: #Open wordlist and read all lines
	
		for line in f:
			words.append(line.rstrip('\n')) #append all words to a List (words)

	for word in words:

		if word == "": #in case there is an empty line

			pass

		else:

			fuzzing_url = url + word #Append the word to our url
			response = requests.get(fuzzing_url,headers=header) #Make the requests
			status = response.status_code #Get the response status code

			if status in range(200, 299): #Verify that the client's request was received successfully
				print(fuzzing_url + color.green+" ---- Found"+color.reset) 
			else:
				print(fuzzing_url + color.red+" ---- Not Found"+color.reset)

#----------------------------------------------------------------------------

#fuzzing(url,wordlist)
if __name__ == "__main__":
	fuzzing(fuzz_url, file)

