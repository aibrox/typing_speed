import time
from random import randrange

random_int = randrange(0,2)
text_example =""

with open("typethis.txt", "r") as f:
    lines = f.readlines()
    text_example = lines[random_int].strip()
word_count = len(text_example.split())
print(text_example)
start = time.time()
user_input = input()
end = time.time()
if text_example == user_input:
    print("true")
else:
    print("false")
print(word_count/((end - start)/60))
