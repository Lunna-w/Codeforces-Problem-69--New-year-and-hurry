
n,k=map(int, input() .split())

max_time=240 # 4 hours=240 minutes

remaining_time = max_time - k


total_time = 0
problems_solved=0

for i in range(1, n + 1):
    time_to_solve = 5 * i
    if total_time + time_to_solve <= remaining_time:
        total_time += time_to_solve
        problems_solved += 1
    else:
        break

print(problems_solved)
