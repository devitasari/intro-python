kata = True
if type(kata) == bool:
    if kata == False:
        print 'cannot proceed without agreement'
    elif kata == True:
        print 'thank you for agreeing'
elif type(kata) == str:
    print 'username:',kata
elif type(kata) == int:
    print 'age:',kata