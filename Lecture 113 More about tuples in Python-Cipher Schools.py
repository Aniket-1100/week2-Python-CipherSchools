mixed = (1,2,3,4,0)
for i in mixed:
    print(i)


num = (1,)
print(type(num))

guitarists = ('Maneli Jamal','Eddie Van Der Meer','Andrew Foy')
guitarist1,guitarist2,guitarist3 = (guitarists)
print(guitarist1)

fav = ('southern magnolia',['Tokya Ghoul','landscape'])
fav[1].pop()
fav[1].append('we made it')
print(fav)