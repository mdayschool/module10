
class Invoice:
    """Invoice class"""
    TAX_RATE = 0.06

    def __init__(self, inum, cid, address, lname, fname, phone):
        self.invoice_number = inum
        self.customer_id = cid
        self.address = address
        self.last_name = lname
        self.first_name = fname
        self.phone = phone
        self.items_by_price = dict()

    def change_invoice_number(self, inum):
        """Changes invoice number"""
        self.invoice_number = inum

    def change_customer_id(self, cid):
        """Changes customer id"""
        self.customer_id = cid

    def change_address(self, address):
        """Changes address"""
        self.address = address

    def change_last_name(self, lname):
        """Changes last name"""
        self.last_name = lname

    def change_first_name(self, fname):
        """Changes first name"""
        self.first_name = fname

    def change_phone(self, phone):
        """Changes phone number"""
        self.phone = phone

    def add_item(self, item):
        """Adds an item to the invoice"""
        self.items_by_price.update(item)

    def create_invoice(self):
        """Prints items by price and total with tax"""
        total = 0
        for k,v in self.items_by_price.items():
            print(k + '.....$' + str(round(v, 2)))
            total += v
        tax = total * self.TAX_RATE
        print('Tax......... ' + str(round(tax)))
        print('Total.......' + str(round(total + tax)))

    def __str__(self):
        return ('Invoice(invoice_number={},customer_id={},address={},' \
                'last_name={},first_name={},phone={},items_by_price={})'
                .format(self.invoice_number, self.customer_id, self.address,
                        self.last_name, self.first_name, self.phone, self.items_by_price))

    def __repr__(self):
        return ('Invoice(invoice_number={},customer_id={},address={},' \
                'last_name={},first_name={},phone={},items_by_price={})'
                .format(self.invoice_number, self.customer_id, self.address,
                        self.last_name, self.first_name, self.phone, self.items_by_price))

# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()

