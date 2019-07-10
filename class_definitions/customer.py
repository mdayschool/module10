
class Customer:
    """Customer class"""
    def __init__(self, cid, lname, fname, phone, address):
        try:
            self.change_customer_id(cid)
        except TypeError as e:
            raise e
        self.last_name = str(lname)
        self.first_name = str(fname)
        self.phone_number = str(phone)
        self.address = str(address)

    def change_customer_id(self, cid):
        """Validates and changes customer id"""
        try:
            self.customer_id = int(cid)
        except ValueError:
            raise TypeError("Customer ID must be numeric")

    def change_last_name(self, lname):
        """Changes last name"""
        self.last_name = str(lname)

    def change_first_name(self, fname):
        """Changes first name"""
        self.first_name = str(fname)

    def change_phone_number(self, phone):
        """Changes phone number"""
        self.phone_number = str(phone)

    def change_address(self, address):
        self.address = str(address)

    def display(self):
        """Returns string with formatted customer information"""
        return (self.first_name + " " + self.last_name + "\n"
                + str(self.customer_id) + "\n"
                + self.phone_number + "\n"
                + self.address)

    def __str__(self):
        return ('Customer(customer_id={},last_name={},first_name={},'
                'phone_number={},address={})'
                .format(self.customer_id, self.last_name, self.first_name,
                        self.phone_number, self.address))

    def __repr__(self):
        return ('Customer(customer_id={},last_name={},first_name={},'
                'phone_number={},address={})'
                .format(self.customer_id, self.last_name, self.first_name,
                        self.phone_number, self.address))

customer1 = Customer(123, 'Ruse', 'Michelle', '515-248-7500',
                     '1100 7th St, Des Moines, IA 50314')

try:
    customer2 = Customer('cat', 'Day', 'Michael', '515-989-1077',
                        '2006 S Ankeny Blvd, Ankeny, IA 50032')
except TypeError as e:
    print(str(e))

print(customer1.display())

# Exception here is raised by the mutator via the constructor because
# raising the exception in the display method would mean that any other
# method accessing cid would require redundant validation.
