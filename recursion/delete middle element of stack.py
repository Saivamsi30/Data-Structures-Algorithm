def delete_middle_element(stack):
    if not stack:
        return stack
    
    middle = len(stack) // 2
    delete_middle(stack,0,middle)
    return stack

def delete_middle(stack,current,middle):
    if current == middle:
        stack.pop()
        return
    
    top = stack.pop()
    delete_middle(stack,current+1,middle)
    stack.append(top)

stack = [1,2,3,4,5]
print(stack)
print(delete_middle_element(stack))
