
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        major_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-")
        if not (name_characters.issuperset(lname)
                and name_characters.issuperset(fname)):
            raise ValueError
        if not major_characters.issuperset(major):
            raise ValueError
        if not isinstance(gpa, float):
            raise ValueError
        if gpa < 0 or gpa > 4:
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return (self.last_name + ", " + self.first_name + " has major "
                + self.major + " with gpa: " + str(self.gpa))
