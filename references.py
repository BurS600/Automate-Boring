def eggs(someParameter):
    someParameter.append('Hello')


spam = [1,2,3]
eggs(spam)
print(spam)


# instead of the someParameter local variable being destroyed and spam remaining untouched like you would expect with string, because the reference to the list stored somewhere in computer storage is being referred, the changes are actually made to that stored reference list
# due to list reference being passed to the function, this change has transcended local/global scope
    




