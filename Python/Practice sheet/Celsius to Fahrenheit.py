def convert(c):
    return(c*9/5)+32

c = int(input("Enter the temperature: "))

conversion = convert(c)

print(f"{c} degree Celsius is {conversion} degree fahrenheit")