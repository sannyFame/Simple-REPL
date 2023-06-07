from colorama import Fore, Back, Style
import random

def create_random_variable():
    seed = random.randint(0, 10)
    ALPHA = "abcdefghijklmnopqrstuvwxyz"
    ALPHA = ALPHA
    variable = ''
    for i in range(seed):
        variable += random.choice(ALPHA)
    return variable
varname = create_random_variable()
run = True
print(Fore.GREEN + Style.BRIGHT + 'Welcome to the Python REPL!' + Style.RESET_ALL)
print("Using pseudo-variable name: " + varname)
print(Fore.GREEN + Style.BRIGHT + 'Type "exit" to exit the REPL.' + Style.RESET_ALL)
while run:
    
    
    # Set input color = Yellow bold
    print()
    __PROMPT_VARIABLE__ = input(Fore.YELLOW + Style.BRIGHT + 'Prompt >>' + Style.RESET_ALL).strip()
    if __PROMPT_VARIABLE__ == 'exit':
        choice = input(Fore.RED + Style.BRIGHT + 'Are you sure you want to exit? (y/n) >>' + Style.RESET_ALL).strip()
        if choice == 'y':
            run = False
        else:
            print('Continuing...')
        
    else:
        try:
            exec(__PROMPT_VARIABLE__) # Execute the input
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + 'Error:' + Style.RESET_ALL)
            print(Fore.RED + str(e) + Style.RESET_ALL)