import json
from functools import reduce


JSON = {"a":{"b":{"c":"d"}},"x":{"y":{"z":"a"}}}

path = input("Enter your key: ")
# Enter path/key as "x/y/z" or "a/b/c during runtime

value = reduce(lambda array,i: array[i], path.split('/'), JSON)
print ("value: ",value)
