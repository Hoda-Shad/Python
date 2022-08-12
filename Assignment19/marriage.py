from random import choice
marriage = []
boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aydin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
for i in range (len(boys)):
    a = choice(boys)
    b = choice(girls)
    marriage.append((a,b))
    boys.remove(a)
    girls.remove(b)
print(marriage)