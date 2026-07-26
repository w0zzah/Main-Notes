def backwards(s):
    #For all recursive set basecase/finish
    if s == '':
        return ""
    #return last item + cmd ending just before last item
    return s[-1] + backwards(s[0:-1])

print(backwards("Hi there!"))