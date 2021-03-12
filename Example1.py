string1 = "Archit Tickoo"
print(string1)
print(string1[3])
string1_length =len(string1)
print(string1_length)
for i in range(string1_length):
    print(string1[i])
    # print index as well
    print(i)

parrot = "Norwegian Blue"
print(parrot[3])
print(parrot[4])
print()
print(parrot[3]);print(parrot[6]);print(parrot[8])

# indexing with negative number
# left to right goes 0 to n
# right to left naturally goes n to 0
# therefore it is either n to 0 or you can use -1
# n = -1
# this means in Norwegian Blue
#               01234567890123
# in negative   43210987654321
# 13 poition is same as -1, 12 position is same  as -2 which means 0 is -0
# zero minues zero doesnt make sense but you get teh pickture
# lets print the same as above we win using negative or backwards

print(parrot)
print(parrot[-1])
print(parrot[-2])
print(parrot[-3])
print(parrot[-4])
print(parrot[-5])
print(parrot[-6])
print(parrot[-7])
print(parrot[-8])
print(parrot[-9])
print(parrot[-10])
print(parrot[-11])
print(parrot[-12])
print(parrot[-13])
print(parrot[-14])
print("we are here at the beginning", parrot[-14])
# lets now print we win
print(parrot)
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# start stop and step
# lets learn slicing

parrot = "norwegion nlue"
print(parrot[0:6])
# from 0 to 5 i.e. 6-1
print(parrot[3:5])
print(parrot[:9])
print(parrot[0:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[:])

test = "surbhi tukra;wife;daughter:heroime"
print(test[:])
print(test[:12])
print(test[0:])
print(test[-5:12])
print(test[::3])
test1 = "123:456:777:999;098,111,123"
print(test1[3::4])