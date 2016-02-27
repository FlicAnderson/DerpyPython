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

# dictionary fun
zoo_feeding = {
    "apples":20,
    "oranges":30,
    "chimpanzees":5,
    "leopards":2
}
zoo_list = [20, 30, 5, 2]

# print 4th item of dictionary, leopards
print zoo_feeding["leopards"]
# print 4th item from list
print zoo_list[3]
# returns "2" - ZERO IS THE FIRST NUMBER

out_list=[]
# to sort things numerically & return new list
# original num_list input is character
for i in num_list:
    i=int(i)    # for each instance, integer the item
    new_list.append(i)  # append the integer to the new_list empty list
    if i < 15: # if number is less than 15
        # create out_result from number (as string) with text, then newline
        out_result = str(i) + " is smallish" + "\n"
        # then append out_result to the empty list called out_list
        out_list.append(out_result)
# create output file by opening a new text file with write access
out_file = open('outputOfListThing.txt', 'w')
# use writelines() to write out_list list of lines into the new file out_file
out_file.writelines(out_list)

# run helloWorld.py file by treating it as a module
import helloWorld

# end the program with witty remark to console
print "... that\'s all, folks!"





