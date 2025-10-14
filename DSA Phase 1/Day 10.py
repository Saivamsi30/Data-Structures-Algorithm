# Remove duplicates from String

def removeduplicates(s):
    seen = set()
    res = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            res.append(ch)
    return ''.join(res)

s = "geEksforGEeks"
print(removeduplicates(s))