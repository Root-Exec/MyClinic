class Employee:
    FirstName: str
    MiddleName: str
    LastName: str

    Address: str
    City: str
    ZipCode: str

    TelephoneNumber: str

    Salary: int

    def __int__(self, fname, mname, lname):
        self.FirstName = fname
        self.MiddleName = mname
        self.LastName = lname
        self.Salary = 0

    def update_address(self, address, city, zipcode):
        self.Address = address
        self.City = city
        self.ZipCode = zipcode
