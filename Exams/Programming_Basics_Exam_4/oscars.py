actor_name = input()  
academy_points = float(input())  
n = int(input())  

for _ in range(n):
    judge_name = input() 
    judge_points = float(input())  

    academy_points += (len(judge_name) * judge_points) / 2

    if academy_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
else:
    needed_points = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
