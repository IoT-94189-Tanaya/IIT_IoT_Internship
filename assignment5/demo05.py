# Arithmetic functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# String functions
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# Main program execution
num1 = 5
num2 = 3

print("Addition:", add(num1, num2))
print("Multiplication:", multiply(num1, num2))

text = "Python Programming"
print("Reversed String:", reverse_string(text))
print("Vowel Count:", count_vowels(text))