from random import randint

key_ = randint(3, 20)
print('n - ', key_)
result = []

for x in range(1, 21):
    for y in range(x + 1, 21):
        c = x + y
        if key_ % c == 0:
            result.append(x)
            result.append(y)
        
print('result - ', *result)
