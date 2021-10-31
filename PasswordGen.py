import random
import array

MAX_LENGTH_OF_PASSWORD=12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']


Combined_list=DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS
def make_password():
    temp_pass=""
    for character in range(MAX_LENGTH_OF_PASSWORD):
        #having temp password as a string and adding the choices of the combined list
        temp_pass+=random.choice(Combined_list)
        
        #having the temp pass as an array and later shuffling it
        
        temp_list=array.array('u',temp_pass)
        random.shuffle(temp_list)
    return temp_list

password=""

if __name__=="__main__":
    for pass_char in make_password():
        #gets a array the list from the function and adds it
        password+=pass_char
    print(password)