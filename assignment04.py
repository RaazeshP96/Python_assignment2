'''
Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?

'''
colleagues = list()
while True:
    colleague = input("Enter the name of  colleague:")
    colleagues.append(colleague)
    qns = input("Do you want to add more friend? Press Y/N :").upper()
    if qns != 'Y':
        break
print(colleagues)  # list before sorting
print('===============================')
beforeSort = id(colleagues)  # id of list before sorting
colleagues.sort()  # sorting the list
print(colleagues)  # list after sorting
print('===============================')
afterSort = id(colleagues)  # id of list after sorting
print('The id of the list is not changed') if beforeSort == afterSort else print(
    'The id of the list is changed')
print(f"first item => {colleagues[0]}")
print(f"second item => {colleagues[1]}")
