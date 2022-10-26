from collections import deque
words = deque(input().split())

first_word = words.popleft()

longest_prefix = first_word[0]
if all([x.startswith(longest_prefix) for x in words]):
    for ch in first_word[1::]:
        if all([x.startswith(longest_prefix + ch) for x in words]):
            longest_prefix += ch
        else:
            break
else:
    longest_prefix = ""

print(longest_prefix)