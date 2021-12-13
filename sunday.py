class phone_Contacts:  # OOPS

    def __init__(self, Firstname, Lastname, Phone_number, Email_ID, Groups, DOB):  # function
        self.firstname = Firstname
        self.lastname = Lastname
        self.phonenumber = Phone_number
        self.emailid = Email_ID
        self.groups = Groups
        self.dob = DOB

    def open_phcontacts(self):
        print("Phone Contacts")

    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:  # LEN FUNCTION
                print("Firstnameame verified")
            else:
                raise ValueError("Firstnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")

    def lastname_verification(self):
        if type(self.lastname) == str:
            if len(self.lastname) <= 15:  # LEN FUNCTION
                print("Lastnameame verified")
            else:
                raise ValueError("Lastnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Lastname should contain letters only")

    def phonenumber_verification(self):
        if (len(self.phonenumber) == 10):
            if type(self.phonenumber) == str:  # TYPE VALIDATION
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers ")
        else:
            raise ValueError("phone number should not be grater than or lesser than 10")

    def emailid_verification(self):
        if type(self.emailid) == str:  # VALUE VALIDATION
            if len(self.emailid) <= 25:
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid emailid")

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <= 10:  # LEN FUNCTION
                print("Groups verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contain letters only")

    def dob_verification(self):
        if isinstance(self.dob, str):  # ISINSTANCE METHOD
            if len(self.dob) <= 10:  # LEN FUNCTION
                print("DOB verified")
            else:
                raise ValueError("DOB should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("DOB should contain numbers and symbols only")


suriya = phone_Contacts("suriya", "prakash", "9905885387", "suriyaprakash22068@gmail.com", "Family", "16/05/2005")
suriya.open_phcontacts()
suriya.firstname_verification()
suriya.lastname_verification()
suriya.phonenumber_verification()
suriya.emailid_verification()
suriya.groups_verification()
suriya.dob_verification()

phone = [
    {"Firstname": "sasi", "Lastname": "dharan", "Phno": 9789658725, "Email_id": "sasi@gmail.com", "Groups": "Family",
     "DOB": "15/08/2003"},  # DICTIONARY INSIDE LIST
    {"Firstname": "john", "Lastname": "calvin", "Phno": 9981258725, "Email_id": "john@gmail.com", "Groups": "Friends",
     "DOB": "19/05/2001"}, ]

for i in phone:  # LOOPING
    for j, k in i.items():  # KEY VALUES LOOPING
        print(f"{j}:{k}")


