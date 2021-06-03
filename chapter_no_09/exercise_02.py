l = [True, False, [1,2,3],1,1.0,3]
# filtered_list = []
# for i in l:
#     if type(i) == int or type(i) == float:
#         filtered_list.append(str(i))
# print(filtered_list)

def filtered_list(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float)]
print (filtered_list(l))