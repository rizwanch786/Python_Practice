# Squares
# simple dictionary
Squares = {f"Sequare of {num} : {num**2}" for num in range(1,11)}
print(Squares)

# # word counter
# # simple dictionary
string = 'Rizwan'
# for i in string:
#     print (f"{i} : {string.count(i)}")
# dictionary comprihension
new_list = {i:string.count(i) for i in string}
print  (new_list)

for key, value in new_list.items():
    print(f"{key} : {value}")

# if_else
# d = {1:'odd', 2:'even'}
d = {i:('even' if i%2 == 0 else 'odd') for i in range (1,11)}
print(d)
d1 = {}
for i in range (1,11):
    if i%2 == 0:
        d1[i] = 'even'
    else:
        d1[i] = 'odd' 
print (d1)

for key,value in d1.items():
    print(f"{key} : {value}")