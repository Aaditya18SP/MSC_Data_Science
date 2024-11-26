inputs = [-1, 0, 1, 2, 3, -1]
ans = []
seen = set()
for idx, i in enumerate(inputs[:-2]):
    for j in inputs[idx+1:-1]:
        j_idx = idx + 1
        for k in inputs[j_idx+1:]:
            print(i, j, k)
            if i + j + k == 0 and not (i in seen and j in seen and k in seen):
                ans.append([i, j, k])
                seen.add(i)
                seen.add(j)
                seen.add(k)

print(ans)
