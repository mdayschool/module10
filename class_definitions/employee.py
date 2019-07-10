import datetime

class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, address='', phone='', salaried='false',
                start=datetime.datetime.now(), salary=0.0):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = phone
        self.salaried = salaried
        self.start_date = start
        self.salary = salary

    def change_last_name(self, lname):
        """Changes last name"""
        self.last_name = lname

    def change_first_name(self, fname):
        """Changes first name"""
        self.first_name = fname

    def change_address(self, address):
        """Changes address"""
        self.address = address

    def change_phone_number(self, phone):
        """Changes phone number"""
        self.phone_number = phone

    def change_salaried(self, salaried):
        """Changes salaried status"""
        self.salaried = salaried

    def change_start_date(self, start):
        """Changes start date"""
        self.start_date = start

    def change_salary(self, salary):
        """Changes salary or hourly pay"""
        self.salary = salary

    def display(self):
        """Returns string with formatted employee information"""
        s = 'Salaried'
        p = '/year'
        if not self.salaried:
            s = 'Hourly'
            p = '/hour'
        return (str(self.first_name) + ", " + str(self.last_name)
                + "\n" + str(self.phone_number)
                + "\n" + s + " employee: $" + str(self.salary) + p
                + "\nStart date: " + self.start_date.strftime('%m-%d-%Y'))

    def __str__(self):
        """Returns attributes in standardized string"""
        return ('Employee(last_name={},first_name{},address={},'
                + 'phone_number={},salaried={},start_date={},salary={})'
                .format(self.last_name, self.first_name, self.address,
                        self.phone_number, self.salried, self.start_date,
                        self.salary))
    def __repr__(self):
        """Returns attributes in standardized string"""
        return ('Employee(last_name={},first_name{},address={},'
                + 'phone_number={},salaried={},start_date={},salary={})'
                .format(self.last_name, self.first_name, self.address,
                        self.phone_number, self.salried, self.start_date,
                        self.salary))


# Driver
emp = Employee('Ruiz', 'Matthew')   # call the construtor, needs to have a first and last name in parameter
emp.change_first_name('Matt')
print(emp.display())                # display returns a str, so print the information

del emp                             # clean up!
