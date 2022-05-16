l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
def avrg(l1,l2,l3):
    l = list(zip(l1,l2,l3))
    return [sum(numbers)/len(numbers) for numbers in l]

print(avrg(l1,l2,l3))
 
# Lambda Expression
avrage = lambda l1,l2,l3 : [(sum(numbers)/len(numbers)) for numbers in list(zip(l1,l2,l3))]
print(avrage(l1,l2,l3))

# List Coprehension
print([(sum(pairs)/len(pairs)) for pairs in list(zip(l1,l2,l3))])
