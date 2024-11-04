pool = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

pipe_1 *= hours
pipe_2 *= hours
total_liters = pipe_1 + pipe_2
percentage_pipe_1 = pipe_1 / total_liters * 100
percentage_pipe_2 = pipe_2 / total_liters * 100
percentage_pool = total_liters / pool * 100



if total_liters > pool:
    print(f"For {hours} hours the pool overflows with {total_liters - pool:.2f} liters.")
else:
    print(f"The pool is {percentage_pool:.2f}% full. Pipe 1: {percentage_pipe_1:.2f}%. Pipe 2: {percentage_pipe_2:.2f}%.")
