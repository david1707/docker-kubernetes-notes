from random import randint as ri

def print_options():
    global option
    # Use a proper menu with visuals

    while True:
        user_input = input('What do you want to roll?\n1. 6 rolls, roll 4d6 drop lower.\n2. 6 rolls, roll 3d6.\n'  
                    + '3. X rolls, roll 4d6 drop lower.\n4. X rolls, roll 3d6.\n0. Exit.\n')
        if int(user_input) not in [1,2,3,4,0]:
            print('Please, use one of the options in the menu.')
        elif user_input.isdigit():
            option = int(user_input)
            break
        else:
            print("Please, enter a valid integer.")   


def check_option():
    rolls = []
    match option:
        case 1:
            print('You selected: 6 rolls, roll 4d6 drop lower.')
            rolls = calculate_4d6_drop(6)

        case 2:
            print('You selected: 6 rolls, roll 3d6.')
            rolls = calculate_3d6(6)

        case 3:
            print('You selected: X rolls, roll 4d6 drop lower.')
            # Sanitise this input
            rolls_n_times = int(input('How many rolls do you want to have?\n'))
            rolls = calculate_4d6_drop(rolls_n_times)

        case 4:
            print('You selected: X rolls, roll 3d6.')
            # Sanitise this input
            rolls_n_times = int(input('How many rolls do you want to have?\n'))
            rolls = calculate_3d6(rolls_n_times)

        case 0:
            print('Bye :)')
            exit()


    if(rolls):
        print_rolls(rolls)
    

## Roll helper functions
def calculate_4d6_drop(roll_n_times):
    rolled_values = []
    for _ in range(roll_n_times):
        rolled_values.append(roll4d6_drop())
        
    return rolled_values


def calculate_3d6(roll_n_times):
    rolled_values = []
    for _ in range(roll_n_times):
        rolled_values.append(roll3d6())
        
    return rolled_values     


def roll4d6_drop():
    roll_value = []
    for _ in range(4):
        roll_value.append(ri(1,6))

    roll_value.remove(min(roll_value))
    return roll_value


def roll3d6():
    roll_value = []
    for _ in range(3):
        roll_value.append(ri(1,6))

    return roll_value


## Print helper functions
def print_rolls(rolls):
    for roll in rolls:
        print(f'{str(sum(roll)).rjust(2, "0")} = {roll}')
    total = sum( sum(x) if isinstance(x, list) else x for x in rolls)
    print(f'Total: {total}\n')