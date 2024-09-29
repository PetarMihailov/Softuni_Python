path = input()

search_1 = path.rindex("\\")
search_2 = path.rindex(".")
file = path[search_1+1:search_2]
extension = path[search_2+1:]

print(f"File name: {file}")
print(f"File extension: {extension}")
