candies = [2,3,5,1,3]
extraCandies = 3

maxCandy = max(candies)
print(maxCandy)
for i in range(len(candies)):
    if candies[i] + extraCandies >= maxCandy:
                candies[i] = True
                print(i)
    else:
        candies[i] = False

print(candies)

