def scope_test():
    def do_local():
        # This creates a new local variable 'spam'
        spam = "local spam"
        
    def do_nonlocal():
        # This modifies the 'spam' variable from the nearest enclosing scope
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        # This modifies the global 'spam' variable
        global spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()            
    print("After global assignment:", spam)
    
scope_test()
print("In global scope:", spam) 