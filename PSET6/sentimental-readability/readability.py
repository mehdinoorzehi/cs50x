# TODO
from cs50 import get_string
import string

matn = get_string("Text: ")
harf = 0
for i in matn:
    if(i.isalpha()):
        harf += 1

kalame = len(matn.split())

jomle = 0
for j in matn:
    if(j == "?" or j == "." or j == "!"):
        jomle += 1


jomlekalame = kalame / 100

L = harf / jomlekalame

S = jomle / jomlekalame

index = round(0.0588 * L - 0.296 * S - 15.8)


if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
