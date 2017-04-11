#reverse 
def reverse(text):
    new = []
    length = len(text)
    while length > 0:
        length -= 1
        new.append(text[length])
    return "".join(new)
print(reverse('hello'))

# Letter play
def reverse(text):
    new = []
    length = len(text)
    for letter in text:
        length -= 1
        new.append(text[length])
    return "".join(new)
print(reverse('awesome'))

# Scrabble game

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word = word.lower()
    total = 0
    for letter in word:
        total = total + score[letter]
    return total
print(scrabble_score('Kindness'))

# Sum
def digit_sum(n):
    result = 0
    while n > 0:
        right = n%10 # this gonna show the number on the most right place
        result = result + right
        n = n // 10 # this gonna replace our number with the number witout the last right number
    return result
print(digit_sum(127594))

# Factorial
def factorial(x):
    result = 1
    while x > 1:
        result = result * x
        x = x - 1
    return result
print(factorial(7))
print('******')
# reccurence 
def fib(n):
    if n==0:
        return 0
    elif n== 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))
for i in range(5):
    print('fib({}) = {}'.format(i, fib(i)))

# dictionary



