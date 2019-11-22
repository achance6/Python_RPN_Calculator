from RPN_calculator.Stack import Stack


def do_operation(i, stack):
    if i == '+':
        stack.push(stack.pop() + stack.pop())
    elif i == '-':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.push(num2 - num1)
    elif i == '*':
        stack.push(stack.pop() * stack.pop())
    elif i == '/':
        num1 = stack.pop()
        num2 = stack.pop()
        if num1 == 0:
            print("Divide by zero error")
            stack.push(num2)
            stack.push(num1)
        else:
            stack.push(num2 / num1)
    elif i == '%':
        num1 = stack.pop()
        num2 = stack.pop()
        if num1 == 0:
            print("Divide by zero error")
            stack.push(num2)
            stack.push(num1)
        else:
            stack.push(num2 % num1)
    elif i == '^':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.push(num2 ** num1)
    elif i == '!':
        exit(0)
    elif i == '?':
        if not stack.empty():
            print(stack.peek())
        else:
            print("Empty")
    else:
        return False


def is_operator(i):
    operators = ('+', '-', '*', '/', '%', '^', '!', '?')
    return operators.__contains__(i)


def main():
    stack = Stack()
    print("Enter a post-fix expression")
    print("! to exit, ? to show current result")
    print("Example Input: 3 4.5 + ? 5 * ? 0 / ? 4 + ? ^ ? !")
    print(">", end=' ')
    while True:
        user_input = input().split()
        for i in user_input:
            try:
                float(i)
                stack.push(float(i))
                continue
            except ValueError:
                pass
            if is_operator(i):
                if not stack.size() > 1 and i != '!' and i != '?':
                    print("Not enough numbers")
                    break
                do_operation(i, stack)
            else:
                print("Invalid argument")
        print(">", end=' ')


if __name__ == main():
    main()
