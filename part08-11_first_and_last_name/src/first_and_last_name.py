# Write your solution here:

class Person():
    def __init__(self, name: str):
        self.name = name

    def name_ok(self):
         parts = self.name.split()
         return len(parts) >= 2
    
    def return_first_name(self):
        if self.name_ok():
            parts =  self.name.split()
            return parts[0]
        return ""

    def return_last_name(self):
        if self.name_ok():
            parts = self.name.split()
            return parts[1]
        return ""

if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())








