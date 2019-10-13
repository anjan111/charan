# difference  between input and raw_input
'''
input function of resultant datatype is input data of data type

raw_input function of resultant datatype is str daatatype for any input data of datatype

'''
print "************input*************"
var = input("enter any datatype : ")
print "data in var : ",var
print(type(var))
print "memory loc : ",id(var)

print "************raw_input*************"
var = raw_input("enter any datatype : ")
print "data in var : ",var
print(type(var))
print "memory loc : ",id(var)

# execute the above code 10 times for 10 diffrent daatatype
