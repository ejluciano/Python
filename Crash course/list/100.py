numbers = list(range(1,101))
odds = list(range(1,101, 2))
multiples = list(range(3,31,3))
print(numbers, "\n")

print(min(numbers))
print(max(numbers))
print(sum(numbers))
for odd in odds:
    print(odd,"\n")

for multiple in multiples:
    print(multiple,"\n")

for value in range(1, 11):
    cube = value ** value
    print(cube)
    