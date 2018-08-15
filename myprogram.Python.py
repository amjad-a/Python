print('Hello user, this is a basic sign up/login program')

username = input('Enter your user name please: ')
password = input ('Enter your user password please: ')
password_varification = input ('varify your password: ')

if password == password_varification :
   print (' You have been successfuly sign up')
else:
    print (" The password and password varification don't match, please try again")
    
