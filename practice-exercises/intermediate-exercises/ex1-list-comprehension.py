words = ["apple", "bat", "cherry", "dog", "elderberry"]

filtered_words = [w.upper() for w in words if len(w) >= 4]

print(f"Original: {words}")
print(f"Result: {filtered_words}")