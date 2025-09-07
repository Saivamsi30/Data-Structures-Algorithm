# 1.first define a function
# 2.Create an empty set with a variable name freq
# 3.Using for loop,set a range to input_list
# 4.now freq[i] = freq.get(i,0)+1 , which means freq will go to every element in the list from 0th index
#   and it will get output as 1 if it is not repeated or it will get ouput as 2 if it is repeated.
# 5.now print the i and freq
# 6.return freq
# 7.call the function. 

def counter(input_list):
    freq = {}
    for i in input_list:
        freq[i] = freq.get(i,0)+1
        print(i,freq[i])
    return freq

print(counter([2,1,3,2,2,1,3,0]))
