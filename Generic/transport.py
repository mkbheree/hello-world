#Lists, random, tuples , enemurate, string
import random
list_can_contain_any_dtype = ['Meher', 26, 5.5, True]
transportation = ['car', 'bike', 'bicycle', 'private flight']

for i in range(len(transportation)):
    print('index ' + str(i) + ' in Transport Mode: ' + transportation[i])

transportation.append('titanic')  # adds new value at the end of the list
transportation.insert(1, 'spaceship')  # adds new value at specified index
print(transportation)
random.shuffle(transportation)  # prints the list with shuffled data
print('After shuffling:', transportation)

'''proper way to mutate a string is by slicing and concat'''
sentence = 'I Meher'
new_sentence = sentence[0:1] +' am ' + sentence[2:7]
print(new_sentence)

'''tuples are similar to lists except they're immutable and use parenthesis'''
tuple_can_also_have_any_dtype = ('hi', 45, 5.5, False)

''' 
1.list -[]- mutable
2.string, tuple - () - immutable
3.we can use enumerate data type which return index along with data

4.a,b,c,d = transportation --> will assign the item in list to each variable resp. 
                            no.of items in the list must match no.of variables
5.list.remove('val') - removes the specific val
6.list.sort(reverse =True) - returns the sorted list with reverse true it returns descending order,
                            sort func can't be applied to list which contains both integer & strings
7.the list functions(append,insert,sort,remove etc) all changes the list in place, they don't effect the actual data  

8.code using tuples slightly faster than code using lists       

9.the functions list() and tuple() will return list and tuple versions of the values passed to them                  
10. id() - Python have a unique identity that can be obtained with the id() function
'''