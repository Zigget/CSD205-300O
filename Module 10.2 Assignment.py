# Made by: Samuel Sidzyik
# Module 10.2 Assignment.py
# Start Date December 13, 2025
# 
# This creates thye employee class and production employee subclass.
# It creates methods and functions to set up and review data for objects created in each class.
# Finally it creates dummy data then prints the data in the terminal.



class Employee:
    def __init__(self):
        self.employee_name = None
        self.employee_gender = None
        self.hourly_pay_rate = None
        self.employee_number = None

    # Set values
    def set_name(self, name):
        self.employee_name = name

    def set_gender(self, gender):
        self.employee_gender = gender
    
    def set_hourly_pay_rate(self, pay_rate):
        self.hourly_pay_rate = pay_rate

    # My job has employee ID numbers as A123 and we refer to them by a-numbers.
    def set_employee_number(self, aNumber):
        self.employee_number = aNumber

    # Get values
    def get_name(self):
        return self.employee_name

    def get_gender(self):
        return self.employee_gender
    
    def get_name(self):
        return self.hourly_pay_rate 

    def get_name(self):
        return self.employee_number 
    
    def show_employee(self):
        print("Employee Information:")
        print(f"Name: {self.employee_name}")
        print(f"Gender: {self.employee_gender}")
        print(f"Hourly Pay Rate: ${self.hourly_pay_rate}")
        print(f"Employee Number: {self.employee_number}")
        print("----------")


    # subclass production employee
class ProductionWorker(Employee):
    def __init__(self):
        super().__init__()
        self.employee_shift = None

    def set_shift(self, shift):
        self.employee_shift = shift

    def get_shift(self):
        return self.employee_shift
    
    def show_employee(self):
        super().show_employee()
        shift_name = {
            1: "Day Shift",
            2: "Swing Shift",
            3: "Graveyard Shift"
        }.get(self.employee_shift, "Unknown Shift")
        print(f"Shift Number: {self.employee_shift} ({shift_name})")
        print("----------")


def main():
    # Main program
    employee_1 = Employee()
    employee_1.set_name("Betty Boop")
    employee_1.set_gender("Female")
    employee_1.set_hourly_pay_rate(25.50)
    employee_1.set_employee_number(101)

    employee_2 = Employee()
    employee_2.set_name("Tom Test")
    employee_2.set_gender("Male")
    employee_2.set_hourly_pay_rate(30.00)
    employee_2.set_employee_number(102)

    # ProductionWorker instances
    worker1 = ProductionWorker()
    worker1.set_name("Scooby Doo")
    worker1.set_gender("Male")
    worker1.set_hourly_pay_rate(28.75)
    worker1.set_employee_number(201)
    worker1.set_shift(1)

    worker2 = ProductionWorker()
    worker2.set_name("")
    worker2.set_gender("Female")
    worker2.set_hourly_pay_rate(32.00)
    worker2.set_employee_number(202)
    worker2.set_shift(3)

    # Display info
    print("=== Employee Records ===")
    employee_1.show_employee()
    employee_2.show_employee()

    print("=== Production Worker Records ===")
    worker1.show_employee()
    worker2.show_employee()


if __name__ == "__main__":
    # I did this a few programs ago and have left it in. It doesn't hurt but I don't think it's necessary unless this program is getting called..
    main()