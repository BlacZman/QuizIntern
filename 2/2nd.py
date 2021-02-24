import math as m

result = []
array = []
text = ""

# Input
while True:
    while text != "0.0":
        text = input()
        try:
            check = float(text)
            if text != "0.0" and (check <= 1.0 or check >= 10.0):
                raise ValueError
        except ValueError:
            break
        array.append(text)

    if len(array) > 0 and array[len(array) - 1] == "0.0":
        break
    else:
        print("Try again. Please continue from where you made a mistake.")

# Clear the "0.0"
array.pop()

# Trial Division for finding Primality of n
# ref: https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/trial-division
for item in array:
    floatN = item[0]
    for i in range(2, len(item)):
        floatN += item[i]
        number = int(floatN)

        # Find primality of the floatN number
        P = round(m.sqrt(number))
        answer = True
        for n in range(2, P):
            divide = number/n
            divideint = round(divide)
            if divide - divideint == 0:
                answer = False
                break

        if answer:
            break
    result.append(answer)

# Print result
for item in result:
    print(item)