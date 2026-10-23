def longest_increasing_subsequence(s: str) -> list[str]:
    n = len(s)
    if n == 0:
        return []
    length = [1] * n
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if s[j] < s[i] and length[j] + 1 > length[i]:
                length[i] = length[j] + 1
                prev[i] = j
    end = max(range(n), key=lambda i: length[i])
    result = []
    while end != -1:
        result.append(s[end])
        end = prev[end]
    result.reverse()
    return result

print(longest_increasing_subsequence("Welcome"))
