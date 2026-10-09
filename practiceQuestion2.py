#create a hetereogenous list of numbers and names .split the ist from highest number
a = [12, "Alisha", 45, "Rahul", 89, 23]

n = []

for i in a:
    if type(i) == int:
        n.append(i)

n.sort(reverse=True)
print(n)