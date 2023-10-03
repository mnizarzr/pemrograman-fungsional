def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))

def add(a,b):
    return a+b

def minus(a, b):
    return a - b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

expression_tree = ((2, '+', 3), '*', (5, '-', 1))

result = tree(expression_tree)

print("Result: ", result)
