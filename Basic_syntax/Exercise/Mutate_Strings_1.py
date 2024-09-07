str1 = input()
str2 = input()
m_str = ''
for i in range(len(str1)):
    f_string = str1[i+1:]
    m_str = str2[:i+1]+f_string
    if str1[i] != str2[i]:
        print(m_str)

first = input()
second = input()
new = ""
add = ""

for i in range(0, len(first)):
    if first[i] == second[i]:
        add = first[i]
        new += add
    else:
        add = second[i]
        new += add
        new1 = new
        for j in range(i + 1, len(first)):
            new1 += first[j]
        print(new1)

s1 = input()

s2 = input()



for i in range(len(s1)):

   if s1[i] != s2[i]:

       s1 = s1[:i] + s1[i:i + 1].replace(s1[i], s2[i], 1) + s1[i + 1:]

       print(s1)

