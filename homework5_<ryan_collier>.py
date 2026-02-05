#This is the start of exercise 1: List Exercise
cheeses = ['brie','american','cheddar','colby-jack', 'gouda', 'mozarella']
for cheese in cheeses:
    print(cheese)
print(f"The first two items in the list are: {cheeses[0:2]}")
print(f"The middle two items in the list are: {cheeses[2:4]}")
print(f"The first and last items in the list are {cheeses[0]}, {cheeses[-1]}")

#This is the beginning of the second exercise: Resturaunt / Tuple
#Line breaks added for readability of professor when reviewing output
print('\n')
foods = ('patty', 'buns', 'fries', 'lettuce', 'tomato')
for food in foods:
    print (food)
#Updated Menu with Tuple modified - last two items updated. Printed with loop
print('\n')
foods = ('patty','buns', 'fries', 'ketchup', 'mustard')
for food in foods:
    print (food)