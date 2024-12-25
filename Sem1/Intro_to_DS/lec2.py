weights = [70,80,45,50]
print(weights)
max_weight = max(weights)
weights[weights.index(45)] = 48
print(weights)
print("Sum:", sum(weights))
print("Mean:", sum(weights)/len(weights))
