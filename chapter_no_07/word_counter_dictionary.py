# in dictionary there is not show same things..
#  it show just one

def word_counter(s):
    count = {}
    for i in s:
        count[i] = s.count(i)
    return count

print (word_counter('Rizwaan'))