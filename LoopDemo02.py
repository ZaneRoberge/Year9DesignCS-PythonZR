# loop demo structure is a structure that allows us to run a section of code a number of times. It is great for when we need to repeat a process it is 
#also great when we need to run a pattern

print("0")
print("1")
print("2")
print("3")
print("4")
print("5")

print("*************************************")
for i in range(0, 6, 1):
    print(i)

# i = 0, 0 < 6, True RUN LOOP
# i = 1, 1 < 6, True RUN LOOP
# i = 2, 2 < 6, True RUN LOOP
# i = 3, 3 < 6, True RUN LOOP
# i = 4, 4 < 6, True RUN LOOP
# i = 5, 5 < 6, True RUN LOOP
# i = 6, 6 < 6, False EXIT LOOP AND MOVE ON

print("**************************************")
print("Write a Loop that will print out 7 to 104 inclusive")
for i in range(7, 105, 1):
	print(i)

print("*****************************************")
print("Print out all numbers from 101 to 0 inclusive")
for i in range(101, -1, -1):
	print(i)

s = "Fish food"

for i in range(0, 9, 1):
	print(s[i])


#len(s) finds the length of the string s
for i in range(8, -1, -1):
    print(i[s])