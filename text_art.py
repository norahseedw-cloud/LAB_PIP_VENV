from art import *
from colorama import *


welcome = text2art("Welcome ", font="block")

print(Fore.WHITE + welcome)


believe = text2art("BELIEVE AND ACHEIVE", font="block")
hello = text2art("HELLO", font="sub-zero")

print(Fore.CYAN + believe)
print(Fore.YELLOW + hello)


name = text2art("Norah", font="slant")
age = text2art("25", font="random")
face = text2art(":)", font="mini")



print(Fore.MAGENTA + name)
print(Fore.GREEN + age)
print(Fore.MAGENTA  + face)





