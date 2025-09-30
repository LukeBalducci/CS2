"""
Luke Balducci
9/30/2025

This project takes your name and runs a through a multitude of differnt functions that do differnt things. Enjoy!

bugs: missing middle name function
get first name can not detect title names
get first and last name can not detect names if user does not use a space when typing their name
while true loop does not work and code breaks after each use 


"""

import random

def vowel_count(name):                                          #Function that will count the vowels of the name
    vowels= 'aeiouAEIOU'                                        # all of the possible present vowels in entered name
    return sum(1 for char in name if char in vowels)            # counts and returns the amount of 



def consonant_count(name):                                      #Function that will count the vowels of the name
    consonants= 'qQwWrRtTyYpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM'    # all of the possible present vowels in entered name
    return sum(1 for char in name if char in consonants)        # counts and returns the amount of



def reverse_name(name):                                         #function to reverse name
    return name[::-1]                                           # it take the name and starts no where, ends no where and counts bakcwards so it returns reverse



def print_first_name(name):                                   
    output = ""                                                 # storage place where the letter goes once it goes through the function
    for letter in name:                                         # goes through the letters in the name
        if letter == ' ':                                       # checks if character is a space    
            break                                               # breaks code if characters ia a space
        else:                                                   # if characted isnt a space
            output += letter                                    # sends letter to the output 
    return output                                               # returns all letters sent to output once fucntion finds a space 

def print_last_name(name):
    output = ""
    for letter in reversed(name):
        if letter == " ":
            break
        else:
            output = letter + output
    return output

def contain_hyphen(name):
    return '-'in name

def convert_lower(name):

    output = ""
    for letter in name:
        num = ord (letter)
        if num >= 65 and  num <=90:
            num = num+32
            letter = chr(num)
            output= output +letter
        else:
            output = output + letter
    return output

def detect_palindrome(name):
    return name == reverse_name(name)

def convert_upper(name):
    output = ""
    for letter in name:
        num = ord (letter)
        if num >= 97 and  num <=122:
            num = num-32
            letter = chr(num)
            output= output +letter
        else:
            output = output + letter
    return output

def get_initials(name):
    parts = name.split()
    initials =""
    for word in parts:
        initials += word[0]
    return initials




def main(): 
    
    while True:
        name = input ("enter your full name or text:")
        choice = input( ''' 
                   1. Count vowels 
                   2. Count consonants
                   3. Reverse name
                   4. Print first name 
                   5. Print last name
                   6. Convert your name to lower case
                   7. Convert your name to upper case
                   8. Is your name a palindrome? 
                   9. Get your Initials
                   10. check name for hyphen(-)
                   
                   Please enter a number:''')
        if choice == "1":
            print ( vowel_count(name),'vowels')
        elif choice == "2":
            print ( consonant_count(name),'consonants')
        elif choice == "3":
            print(reverse_name(name))
        elif choice == "4":
            print(print_first_name(name))
        elif choice == "5":
            print(print_last_name(name))
        elif choice == "6":
            print(convert_lower(name))
        elif choice == "7":
            print(convert_upper(name))
        elif choice == "8":
            print(detect_palindrome(name))
        elif choice == "9":
            print(get_initials(name))
        elif choice == "10":
            print(contain_hyphen(name))
        break
        print("you entered an invalid answer please enter a number 1-10")

main()