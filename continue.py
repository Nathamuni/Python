# Continue is used to just skip for that specific conditions __ only inside the loop or condition

# Here I want to skip the values that are dividible by 2(even n.os) using _continue_
for i in range (1,101):
    if i% 2 == 0:
        continue

    print(i)

