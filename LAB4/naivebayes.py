import csv



def calConditional(key, values, outputs, output_frequency):
    print(key)
    print(values)
    print(outputs)
    print(output_frequency)
    
    value_frequency = {}
    
    for k in values:
        if k not in value_frequency:
            value_frequency[k] = 1
        else:
            value_frequency[k] += 1
    
    print(value_frequency)
    
    conProbBox = {}
    
    i = 0
    
    
    for k in values:
        if k not in conProbBox.keys():
            conProbBox[k] = {out: 0 for out in output_frequency.keys()}
    
   
    for i in range(len(values)):
       conProbBox[values[i]][outputs[i]] += 1
       
       
    print(conProbBox)

    for k in conProbBox.keys():
        # print(conProbBox[k].keys())
        for q in conProbBox[k].keys():
            conProbBox[k][q] = round(conProbBox[k][q] / output_frequency[q], 4)
    
    
    return {key: conProbBox}


file = open('dataset.csv')

listOfInstances = list(file)

# print(listOfInstances)

print("Total number of examples are ", len(listOfInstances) - 1)

listOfListOfInstances = [l.split(',') for l in listOfInstances]

# print(listOfListOfInstances)

print("The given attributes are: ")

attributes = listOfListOfInstances[0]


print(attributes)

print("Given values for the data set are: ")

for l in listOfListOfInstances[1:]:
    print(l)
    
print("\nCalculating the prior probability\n")

list_of_outputs = [l[len(l) - 1] for l in listOfListOfInstances[1:]]

print("We have the list of outputs as: ")

list_of_outputs = [l.replace('\n', '') for l in list_of_outputs]

for output in list_of_outputs:
    print(output)

print("\nDifferent types of outputs are: \n")

output_frequency = dict()

for key in list_of_outputs:
    if key not in output_frequency:
        output_frequency[key] = 1
    else:
        output_frequency[key] += 1
    
print(output_frequency)

priorProbabilityDict = {}

for key in output_frequency:
    priorProbabilityDict[key] = round(output_frequency[key] / len(list_of_outputs), 4)
    
print("Prior probailites are: ")

print(priorProbabilityDict) 

print("Making separate columns for each attributes")

i = 0

attributeValueDict = {}

for keys in attributes[:len(attributes) - 1]:
    attributeValueDict[keys] = [row[i] for row in listOfListOfInstances[1:]]
    i += 1
    
print(attributeValueDict)
    
print("Calculating conditional probabilities for the attributes")

model = {}

for key in attributeValueDict.keys():
    model.update(calConditional(key, attributeValueDict[key], list_of_outputs, output_frequency))
    
    
print("Final ML Model built is")


print(model)


print("Enter new instance: ")

newInstance = input().split()

print(newInstance)

print("Output for yes")

VnbYes = 1

i = 0
for k in model.keys():
    VnbYes *= model[k][newInstance[i]]['yes']
    i += 1

VnbYes *= output_frequency['yes']
VnbYes /= len(list_of_outputs)
print(round(VnbYes, 4))





    
