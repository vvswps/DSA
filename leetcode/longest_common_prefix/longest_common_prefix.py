# 14. Longest Common Prefix

# strs = ["flower", "flow", "flight"]
strs = ["c", "acc", "ccc"]
# strs = ["dog","racecar","car"]

prefixes = [strs[0][0:i+1] for i in range(len(min(strs)))]

sequences = []
for i in prefixes:
    if all(map(lambda x: x.startswith(i), strs)):
        sequences.append(i)
print("" if len(sequences) == 0 else max(sequences))
