# A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

# Examples
# The following are examples of balanced delimiter strings:

# ()[]{}
# ([{}])
# ([]{})
# The following are examples of invalid strings:
# ([)]
# ([]
# [])
# ([})
# Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

# Input:
# ([{}])
# Output:
# True

def brackets_balance(str1):
    stack = []
    for i in str1:
        if (i == '(') or (i == '[') or (i == '{'):
            stack.append(i)
        else:
            if (stack[-1] =='(' and i == ')') or (stack[-1] == '{'and i == '}') or (stack[-1] =='[' and i == ']'):
                stack.pop()
            
            else:
                return False
        
    return not stack

str1 = "([{}])"

# print(brackets_balance(str1))

if brackets_balance(str1):
    print("Balanced")

else:
    print("Not balanced")

