array = []
result = []
sorted = []
size = 0

# Input the size of incoming input
while True:
    try:
        size = int(input("Enter an input: "))
    except ValueError:
        print("Error converting to int. Please Try again.")
    else:
        break

# Input the string that need to do acronyms
for i in range(size):
    text = input()
    array.append(text)

# Create acronyms out of text 
for item in array:
    if item != None:
        arrayStringSplit = item.split(" ")
        acronyms = ""
        for splitstr in arrayStringSplit:
            if splitstr[0].isupper():
                acronyms += splitstr[0]
        if acronyms == "":
            result.append("A")
        else:
            result.append(acronyms)
    else:
        result.append("A")

# Sorting
sorted.append(result[0])
for i in range(1, len(result)):
    length = len(sorted)
    for j in range(length):
        if len(result[i]) > len(sorted[j]):
            sorted.insert(j, result[i])
            break
        elif len(result[i]) == len(sorted[j]):
            if result[i] < sorted[j]:
                sorted.insert(j, result[i])
                break

        if j == length - 1:
            sorted.append(result[i])
            
# Print result
for item in sorted:
    print(item)