a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x< 5: print(x)             #displaying the values

# making as new list
print([ element for element in a if element<5 ])
print([y for y in a if y>5])
print([z for z in a if z==5])