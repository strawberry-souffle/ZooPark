n = int(input())
answer = 11 + (n-6)
if answer < 0:
    answer += 24
elif answer >= 24:
    answer -= 24
if answer <= 9:
    print("0" + str(answer) +":00")
else:
    print(str(answer) + ":00")