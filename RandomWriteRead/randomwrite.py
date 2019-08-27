#This program writes a series of user-inputted random
#integers to a file
import random

def main():
    
    #Ask user how many random numbers
    while True:
        try:
            SIZE = int(input('How many random numbers do you want? '))
            if SIZE <= 0:
                print('Numbers zero and below are not allowed.')
                continue
        except ValueError:
                print('The value you entered is invalid. ' +
                      'Only numerical values are valid.')
        else:
            break                

    #Get lowest number from user
    while True:
        try:
            low_num = int(input('What is the lowest the random ' +
                                'number should be: '))
            if low_num <= 0:
                print('Numbers zero and below are not allowed.')
                continue
        except ValueError:
                print('The value you entered is invalid. ' +
                      'Only numerical values are valid.')
        else:
            break   

    #Get highest number from user
    while True:
        try:
            high_num = int(input('What is the highest the random ' +
                                 'number should be: '))
            if high_num <= 0:
                print('Numbers zero and below are not allowed.')
                continue
            if high_num <= low_num:
                print('The highest random number cannot be ' +
                      'less than or equal to the lowest random number.')
                continue
        except ValueError:
                print('The value you entered is invalid. ' +
                      'Only numerical values are valid.')
        else:
            break

    #Call get_list function and assign it to
    #user_numbers variable
    user_numbers = get_list(SIZE, low_num, high_num)

    #Call write_file function 
    write_file(user_numbers)

#Create and return the user list
def get_list(LIST_SIZE, low, high):
    user_list = [] #Create empty list to hold numbers 
    index = 0 #Create variable to hold index

    while index < LIST_SIZE:
        number = random.randint(low, high) #Generate random number
        user_list.append(number) #add number to list
        index += 1

    return user_list

#Write a file to disk
def write_file(user_list):
    #Open a file for writing
    outfile = open('randomnum.txt', 'w')

    #Write the list to the file
    for number in user_list:
        outfile.write(str(number) + '\n')

    #Close the file
    outfile.close()

    print('The random numbers were written to randomnum.txt')

#Call main function
main()

    

















    
