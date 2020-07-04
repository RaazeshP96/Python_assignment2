'''

Write a Python class to find validity of a string of parentheses, '(', ')', '{',
'}', '[' and ']'. These brackets must be close in the correct order, for example
"()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid


'''


def bra(string):
    dis = {'[': ']', '{': '}', '(': ')'}
    stack = []
    for i in string:
        if stack:
            tos = stack[-1]
            stack.pop() if i == dis[tos] else stack.append(i)
        else:
            stack.append(i)
    print("True") if len(stack) == 0 else print("False")


# test
if __name__ == '__main__':
    string = "()[{}]"
    bra(string)
