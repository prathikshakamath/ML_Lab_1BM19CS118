import csv
file = open('data.csv')

print(file)

listOfInstances = [l.replace('\n','') for l in list(file)]

print(listOfInstances)


attributes = listOfInstances[0].split(',')

print("The attributes are: ")

print(attributes)

values = [[int(i.split(',')[0]), int(i.split(',')[1])] for i in listOfInstances[1:]]

print("The values of the given attributes: ")
for i in values:
    print(i)

# here summation is represented by sum

sumx = 0
sumy = 0
sumxsq = 0
sumxy = 0
n = len(values)

for row in values:
    sumx += row[0]
    sumy += row[1]
    sumxsq += row[0] * row[0]
    sumxy += row[0] * row[1]
    
b0 = (sumy * sumxsq - sumx * sumxy) / (n * sumxsq - sumx ** 2)
b1 = (n* sumxy - sumx * sumy) / (n * sumxsq - sumx ** 2)

print("sumx =", sumx)
print("sumy =", sumy)
print("sumxsq =", sumxsq)
print("sumxy =", sumxy)
print("")
print("b0 =", b0)
print("b1 =", b1)



print("Enter the value of x")

x = int(input())
y = b0 + b1 * x

print("y =", y)

