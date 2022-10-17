import re

# For email validation
def solve(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False

# For password validation
def solvepw(p):
   reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
   com = re.compile(reg)
   res = re.search(com, p)
   if res:
      return True
   else:
      return False

# For new user registration (only registered when email and password gets validated based on given conditions and if the email is not already present in the database)
def register():
    f=open("database.txt","r")
    email=input("Create your e-mail address:")
    password=input("Create your password:")
    name = []
    pw = []
    for i in f:
        a, b = i.split(", ")
        b = b.strip()
        name.append(a)
        pw.append(b)
    try:
        if email not in name:
            if solve(email) == True & solvepw(password) == True:
                f=open("database.txt","a")
                f.write(email+", "+password+"\n")
                print("New account created!")
            else:
                print("Invalid email address or password. Please enter a valid one.")
                register()
        else:
            print("Email address already exists. Create a new one.")
    except:
        print("Email address already exists.")

# For user login (only for users already in database)
def login():
    f = open("database.txt", "r")
    email = input("Enter your e-mail address:")
    password = input("Enter your password:")
    if not len(email or password)<1:
       name = []
       pw = []
       for i in f:
          a,b = i.split(", ")
          b=b.strip()
          name.append(a)
          pw.append(b)
       data = dict(zip(name, pw))

       try:
           if data[email]:
               try:
                  if password == data[email]:
                     print("Hi "+email+"! Welcome to your account!!")
                  else:
                     print("Email or password is incorrect.")
               except:
                   print("Incorrect email or password.")
           else:
               print("Email address or password doesn't exist.")
       except:
           op=input("This account doesn't exist. Do you want to register a new one? (Y/N)")
           if op=="Y":
               register()
           elif op=="N":
               home()
    else:
        print("Please enter a value.")

# For users who forget their password or to change the old password
def forgetpw():
   f = open("database.txt", "r")
   email = input("Enter your e-mail address:")
   name = []
   pw = []
   for i in f:
      a, b = i.split(", ")
      b = b.strip()
      name.append(a)
      pw.append(b)
   data = dict(zip(name, pw))
   try:
      if email in name:
         op=input("Do you want your old password? (Y/N)")
         if op=="Y":
            for (key,value) in data.items():
               if key==email:
                  ans=value
            print("Your password is ", ans)
         elif op=="N":
            new_password=input("Enter your new password:")
            for (key, value) in data.items():
               if key == email:
                  ans = value
            f=open("database.txt","r")
            filedata=f.read()
            filedata=filedata.replace(ans,new_password)
            f=open("database.txt","w")
            f.write(filedata)
            print("Password successfully changed.")
         else:
            print("Please enter a value.")
      else:
         print("Email address not found. Register a new one.")
   except:
      print("Email address not found.")

# Base function to call all the functionalities
def home():
   print("""Welcome to the portal!!!
                1. Register 
                2. Login
                3. Forget Password""")
   option=input("Enter an option::")
   if option=="1":
      register()
   elif option=="2":
      login()
   elif option=="3":
      forgetpw()
   else:
      print("Select from the given options.")

home()


