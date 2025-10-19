# expr_evaluator.py
# Shunting-yard to convert infix to postfix, then evaluate.
import operator
ops = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv),
    '^': (3, operator.pow)
}

def infix_to_postfix(tokens):
    out = []
    stack = []
    for tok in tokens:
        if tok.isnumeric():
            out.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack and stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and ops[tok][0] <= ops.get(stack[-1], (0,))[0]:
                out.append(stack.pop())
            stack.append(tok)
    while stack:
        out.append(stack.pop())
    return out

def eval_postfix(postfix):
    stack = []
    for tok in postfix:
        if tok.isnumeric():
            stack.append(float(tok))
        else:
            b = stack.pop(); a = stack.pop()
            stack.append(ops[tok][1](a,b))
    return stack[0]

def tokenize(expr):
    tokens=[]
    num=''
    for ch in expr:
        if ch.isdigit():
            num+=ch
        else:
            if num:
                tokens.append(num); num=''
            if ch.strip():
                tokens.append(ch)
    if num: tokens.append(num)
    return tokens

if __name__ == "__main__":
    expr = input("Enter infix expression (e.g., 3+(4*5)-2): ").strip()
    toks = tokenize(expr)
    postfix = infix_to_postfix(toks)
    print("Postfix:", ' '.join(postfix))
    print("Evaluated:", eval_postfix(postfix))
