name = "Jessy"
print(name)

sent = "%s is my friend"
print(sent%name)


sent2 = "Let's practice %s"
thing = "Python"

print(sent2%thing)

sent3 = "I need to borrow %d amount "
amount = 3000

print(sent3%amount)

# array

shopList = ["bread", "coffee", "butter", "milk"]

print(shopList)
print(shopList[0])
print(shopList[0:2])
del shopList[0]
print(shopList)

print(len(shopList))

shopList2 = ["shampoo", "cream"]

print(shopList + shopList2)
print(shopList * 2 )

listNum = [1,4,232,43,-999]

print(max(listNum))
print(min(listNum))




