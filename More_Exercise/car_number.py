start= int(input())
end = int(input())

special_numbers = []
for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        for num3 in range(start, end + 1):
            for num4 in range(start, end + 1):
                if ((num1 % 2 == 0 and num4 % 2 != 0) or (num1 % 2 != 0 and num4 % 2 == 0)) \
                        and (num1 > num4) \
                        and ((num2 + num3) % 2 == 0):

                    special_number = f"{num1}{num2}{num3}{num4}"
                    special_numbers.append(special_number)

print(" ".join(special_numbers))
