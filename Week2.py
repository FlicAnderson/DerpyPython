new_list = []
num_list = ["1","2","3","11","14","17","29","32","4"]

# sorting numbers as strings
print num_list
print sorted(num_list)
# 1,11,14,17,2,29,3,32,4

# to sort things numerically & return new list
for i in num_list:
    i=int(i)
    new_list.append(i)
print sorted(new_list)
# 1,2,3,4,11,14,17,29,32

# sorting strings
word_list = ["the", "cat", "sat", "on", "the", "mat"]
# 'cat' 'mat' 'on' 'sat' 'the' 'the'
print sorted(word_list)

# sorting booleans
bool_list = [True, False]
# False True
print sorted(bool_list)

