severity_dictionary = {}

severity_names = ["Critical", "High", "Medium", "Low", "Info"]
severity_scores = [4, 3, 2, 1, 0]

# Name -> Score
severity_map = {severity_names[i]: severity_scores[i] for i in range(len(severity_names))}
print(severity_map)

# Score -> Name (reverse mapping)
reverse_map = {score: name for name, score in severity_map.items()}
print(reverse_map)