strings = input().split()
searched_palindrome = input()

palindromes = [word for word in strings if word == word[::-1]]

print(f"{palindromes}\nFound palindrome {palindromes.count(searched_palindrome)} times")
