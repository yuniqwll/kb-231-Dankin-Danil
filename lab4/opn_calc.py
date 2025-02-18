import operator

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token in precedence:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    
    while stack:
        output.append(stack.pop())
    
    return output

def evaluate_postfix(postfix):
    stack = []
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
    5
    for token in postfix:
        if token.isnumeric():
            stack.append(float(token))
        elif token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
    
    return stack[0]

def calculate(expression):
    postfix = infix_to_postfix(expression)
    print("Зворотня польска нотація:", " ".join(postfix))
    return evaluate_postfix(postfix)

if __name__ == "__main__":
    expr = input("введіть матиматичний вираз (з проблемами між числами і операторами): ")
    try:
        result = calculate(expr)
        print("Результат:", result)
    except Exception as e:
        print("Помилка в обчисленні:", e)
