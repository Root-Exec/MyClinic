class Employee:
    FirstName: str
    MiddleName: str
    LastName: str

    Address: str
    City: str
    ZipCode: str

    TelephoneNumber: str
    StartEmployment: str

    def __int__(self, fname, mname, lname, phone_number):
        self.FirstName = fname
        self.MiddleName = mname
        self.LastName = lname
        self.TelephoneNumber = phone_number

    def update_address(self, address, city, zipcode):
        self.Address = address
        self.City = city
        self.ZipCode = zipcode
