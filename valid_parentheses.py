s = list(input())

idx = []
stopped = None

for index_of_char in range(len(s)):
    if not idx and s[index_of_char] in ")]}":
        stopped = True
        break
    if s[index_of_char] in "({[":
        idx.append(s[index_of_char])
        continue
    if f"{idx[-1]}{s[index_of_char]}" in "(){}[]":
        idx.pop()
        continue
    else:
        stopped = True
        break

if not stopped and not idx:
    print(True)
else:
    print(False)
    