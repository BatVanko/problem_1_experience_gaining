needed_experience = int(input())
count_of_battles = int(input())
sum_of_experience = 0
counter = 0
for num in range (1,count_of_battles+1):
    experience = int(input())
    counter +=1
    if num % 3 == 0:
        experience *= 1.15
    if num % 5 == 0:
        experience *= 0.9
    if num % 15 == 0:
        experience *= 1.05
    sum_of_experience += experience
    if sum_of_experience >= needed_experience:
        break

if sum_of_experience >= needed_experience:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    print(f"Player was not able to collect the needed experience, {(needed_experience - sum_of_experience):.2f} more needed.")







