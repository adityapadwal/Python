movies = ["Pathaan", "Kesari", "Drishyam", "Pushpa"]
stars = ["SRK", "AK", "AD", "AA"]

for i, j in list(zip(movies, stars)):
    # print(f'{j} star in {i} movie')
    print(list(zip(movies, stars)))

# ans = {}
# user = input("Enter something: ")
# for i in user:
#     ans[i] = user.count(i)
# print(ans)
