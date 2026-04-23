import random

results = []

for i in range(100):
    throw = random.choice(["head", "tail"])
    results.append(throw)

heads = results.count("head")
tails = results.count("tail")

print("Percentage heads:", heads / 100)
print("Percentage tails:", tails / 100)
