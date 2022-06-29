import time

text_example = "Adam jest szefem vima."
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

