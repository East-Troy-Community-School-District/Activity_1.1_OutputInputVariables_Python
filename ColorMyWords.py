'''
Color My Words
Pawelski
3/9/2023
Python II
'''

import colorama

print(colorama.Fore.RED + "red ", end="")
print(colorama.Fore.GREEN + "green ", end="")
print(colorama.Fore.BLUE + "blue")
print("Still blue...")
print(colorama.Fore.CYAN + "cyan "
      + colorama.Fore.MAGENTA + "magenta "
      + colorama.Fore.YELLOW + "yellow")
print(colorama.Back.WHITE + colorama.Fore.BLACK + "Inverted colors?")
print(colorama.Back.RESET + colorama.Fore.RESET + "Back to normal!")

# Add some code to display "Cookie, Cookie, Cookie!" in yellow text
# with a cyan background.
