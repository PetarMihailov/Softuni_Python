version = input().split(".")

next_version = int("".join(version)) + 1
next_version = ".".join(str(next_version))


print(next_version)
