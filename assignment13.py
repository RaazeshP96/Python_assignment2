'''

Write a function to write a comma-separated value (CSV) file. 
It should accept a filename and a list of tuples as parameters. 
The tuples should have a name, address, and age. The file should 
create a header row followed by a row for each tuple. 
If the following list of tuples was passed in: [('George', '4312 Abbey Road', 22), 
('John', '54 Love Ave', 21)] it should write the following in the file:

name,address,age 
George,4312 Abbey Road,22
John,54 Love Ave,21

'''


def Csvfiles(filename, lis1):
    with open(f'{filename}.csv', 'w') as file:
        str1 = "name, address, age \n"
        file.writelines(str1)
        for i in lis1:
            name, address, age = i
            str2 = f'{name}, {address}, {age} \n'
            file.writelines(str2)
    print('csv file is created')


# filename='comma'
filename = input("Enter the filename:")
lis1 = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
Csvfiles(filename, lis1)
