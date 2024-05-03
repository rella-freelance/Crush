import time
#not many libraries required 

def crush_name():
    girl_name = ['Ann', 'Anne', 'Brent', 'Brenda', 'Amelia', 'Annelisa', 'Damaris', 'Dinah', 'Esther', 'Ester', 'Emily',
                 'Susan', 'Leah', 'Mary', 'Hannah', 'Jennifer', 'Mercy', 'Maggie', 'Magrate', 'Melin', 'Stephanie', 'Steph', 'Zoe', 
                 'Rachael', 'Lucy', 'Lucia', 'Serah', 'Sarah', 'Mia', 'Kezziah', 'Keziah', 'Juliet', 'Miley']
    return girl_name

def isCrushAdorable(name):
    girl_names = crush_name()

    print('Checking if your crush is adorable.\n ***    ***   ***\n')
    for i in range(0, 3):
        print('**', end=" ")
    time.sleep(3)
    return name in girl_names

def wouldCrushWantMe(name):
    girl_names = crush_name()

    print("Checking if your crush would want  to have you. \n ***   ***  ***\n")
    time.sleep(3)

    if not name:
        return name in girl_names
    else:
        return 'Seems like your crush is a outta your range'

def enter():
    print("*All names start with a cpital letter followed by lower case*\n\n")
    name = input("Enter your crush's name: \n")
    return name

def main():
    name = enter()
    if isCrushAdorable(name):
        print("\nWhat are you doing with your life?\n\n")
        time.sleep(2)
    else:
        print("\nSeems like your crush is not your type!\n\n")
        time.sleep(2)

    print(wouldCrushWantMe(name))

if __name__ == '__main__':
    main()
