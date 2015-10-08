# This is some comments
from sys import argv
# import ipdb
script, arg1, arg2, arg3 = argv
#
# script, original, copy = argv
#
# original_file = open(original)
# new_file = open(copy, 'w')
#
# new_file.write(original_file.read())
#
# new_file.close()
# original_file.close()


# fruit = ['lemon', 'apple', 'banana', 'orange']
# for fruits in fruit:
#    print fruits


def calculate(first_num, second_num, operator):

    ifirst = int(first_num)
    isecond = int(second_num)
    if operator == 'multiple':
        output = ifirst * isecond
    if operator == 'division':
            output = ifirst / isecond
    return output

calculate_result = calculate(arg1, arg2, arg3)
print "Your calculation result is:%s" % calculate_result
