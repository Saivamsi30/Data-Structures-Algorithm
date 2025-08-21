def recursive_sort_stack(stack):
    if len(stack) <= 1:
        return stack
    
    top = stack.pop()
    recursive_sort_stack(stack)
    insert_in_sorted(stack,top)
    return stack

def insert_in_sorted(stack,value):
    if len(stack) == 0 or stack[-1] <= value:
        stack.append(value)
        return stack
    
    top = stack.pop()
    insert_in_sorted(stack,value)
    stack.append(top)
    return stack

stack = [2,5,3,1,6]
print(stack)
sorted_stack = recursive_sort_stack(stack)
print(sorted_stack)


