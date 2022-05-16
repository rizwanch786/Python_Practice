# in dictionary there is not show same things..
#  it show just one

def word_counter(s):
    return {i: s.count(i) for i in s}

print (word_counter('Rizwaan'))