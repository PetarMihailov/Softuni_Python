def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

start_1 = int(input())  
start_2 = int(input())  
diff_1 = int(input())   
diff_2 = int(input())   

for first_pair in range(start_1, start_1 + diff_1 + 1):
    for second_pair in range(start_2, start_2 + diff_2 + 1):
        if is_prime(first_pair) and is_prime(second_pair):
            print(f"{first_pair}{second_pair}")
