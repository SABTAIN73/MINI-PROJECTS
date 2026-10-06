import time
import random

print("Typing Speed Test")

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Practice makes perfect when learning how to code.",
    "Keep calm and code on."
]

sentence = random.choice(sentences)

print("\nType this sentence:")
print(sentence)

input("\nPress Enter when you are ready...")

start_time = time.time()

print("\nType it again:")
user_input = input("> ")

end_time = time.time()

time_taken = end_time - start_time

correct = 0

for i in range(min(len(sentence), len(user_input))):
    if sentence[i] == user_input[i]:
        correct += 1

accuracy = (correct / len(sentence)) * 100

print("\nResult")
print(f"Time: {time_taken:.2f} seconds")
print(f"Accuracy: {accuracy:.2f}%")

if user_input == sentence:
    print("Perfect!")
else:
    print("There were some mistakes.")