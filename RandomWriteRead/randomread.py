#This program reads numbers from a file
import sys

def main():
    try:
        #Open a file for reading
        infile = open('randomnum.txt', 'r')   

        #Read the contents of the file into a list
        numbers_list = infile.readlines()

        #Close the file()
        infile.close()       
        
        print('List of random numbers in randomnum.txt:')
        
        #Convert each element to an int 
        index = 0
        while index < len(numbers_list):
            numbers_list[index] = int(numbers_list[index])
            print(numbers_list[index])
            index += 1

        print('Random number count:', len(numbers_list))
        
    except IOError:
        print('An error occurred when trying to read')
        print('the file randomnum.txt')
    except FileNotFoundError:
        print('The file randomnum.txt was not found')   
    
#Call main function
main()
    
    
        
