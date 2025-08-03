#Balanced Parentheses Check

def is_balanced(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return "NO"
            top = stack.pop()
            if matching[char] != top:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

S = input().strip()
print(is_balanced(S))
