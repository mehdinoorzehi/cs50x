# TODO
from cs50 import get_float

while True:
    a = get_float("Change owed: ")
    if a > 0:
        break
    else:
        continue
c = round(a * 100)

sekke = 0
while c > 0:
    if c >= 25:
        c -= 25
    elif c >= 10:
        c -= 10
    elif c >= 5:
        c -= 5
    else:
        c -= 1
    sekke += 1
print(sekke)
