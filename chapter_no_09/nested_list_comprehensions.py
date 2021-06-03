example = [[1,2,3],[1,2,3],[1,2,3]]
# simple list
new_list = []
for i in example:
    new_list.append(i)

print (new_list)

# list coprehensions
# new_example = [[i for i in range(1,4)] for j in range(3)]
new_example = [i for i in example]
print(new_example)