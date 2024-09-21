string_1 = list(input())
string_2 = input()

for index in range(len(string_1)):
    if not string_1[index] == string_2[index]:
        string_1[index] = string_2[index]
        print("".join(string_1))
