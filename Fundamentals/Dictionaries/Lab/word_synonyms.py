lines = int(input())

words = {}

for _ in range(lines):
    word = input()
    synonym = input()

    if word not in words:
        words[word] = []
    words[word].append(synonym)

for word in words:
    print(f"{word} - {', '.join(words[word])}")
