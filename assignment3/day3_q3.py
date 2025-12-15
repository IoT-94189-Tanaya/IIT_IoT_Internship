def count_vowels(s):
    v = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            v += 1
    return v

def count_consonants(s):
    c = 0
    for ch in s:
        if ch.isalpha() and ch not in "aeiouAEIOU":
            c += 1
    return c

s = input("Enter string: ")

v = count_vowels(s)
c = count_consonants(s)

print("Vowels:", v)
print("Consonants:", c)

if c != 0:
    print("Ratio:", v / c)
else:
    print("Cannot find ratio")
