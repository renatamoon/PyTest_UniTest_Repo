
with open("potato.txt", 'w') as file:
    file.write("""
    I gotta tell you what I'm feeling inside
    I could lie to myself, but it's true
    There's no denying when I look in your eyes
    Girl I'm out of my head over you
    And I lived so long believing all love is blind
    But everything about you is telling me this time
    """)

tab = open("potato.txt")

print(tab) # <_io.TextIOWrapper name='potato.txt' mode='r' encoding='UTF-8'>

print(next(tab))

g = open("potato.txt").read()
print(g)

g = open("potato.txt").readlines

print("-="*20)

map(lambda x: x, [1,2,3])

m = map(lambda x: x, [1,2,3])

print("this is the generator: ", next(m))
print("this is the generator: ", next(m))
print("this is the generator: ", next(m))
print("this is the generator: ", next(m))