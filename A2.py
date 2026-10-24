class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called, Employee deleted.")
def Create_obj():
    print("Creating And Making Employee Object")
    obj = Employee()
    print("Function end....")
    return obj
print("Calling the Create_obj()function...")
obj=Create_obj()
print("Program End....Goodbye For Now!")