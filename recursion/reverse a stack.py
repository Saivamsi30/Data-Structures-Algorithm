def insert_at_bottom(stack,value):
    if not stack:
        stack.append(value)
        return
    
    top = stack.pop()
    insert_at_bottom(stack,value)
    stack.append(top)

def reversed_stack(stack):
    if not stack:
        return stack
    
    top = stack.pop()
    reversed_stack(stack)
    insert_at_bottom(stack,top)
    return stack

stack = [1,2,3,4,5]
print(stack)
print(reversed_stack(stack))