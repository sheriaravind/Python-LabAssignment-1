class Flight(object):
    flight_count = 0
    def __init__(self, Flight_Number, From, To, Date):
        self.Flight_Number = Flight_Number
        self.From_Loc = From
        self.To_Loc = To
        self.Date = Date
        Flight.flight_count += 1

    def get_Flight_Details(self):
        #print("Details of flight are: ", self.Flight_Number, self.From_Loc, self.To_Loc, self.Date)
        return self.Flight_Number, self.From_Loc, self.To_Loc, self.Date
    def get_flight_count(self):
        print("Total number of flights are: " , self.flight_count)


class Person(object):
    person_count = 0
    def __init__(self, Name, Age, Sex):
        self.Name = Name
        self.Age = Age
        self.Sex = Sex
        Person.person_count += 1


    def Print_Person_Details(self):
        return str((self.Name, self.Sex,self.Age))

    def get_person_count(self):
        print("Total number of persons are: ", self.person_count)

class Employee(Person):
    employee_count = 0
    def __init__(self, Name, Age, Sex, Emp_ID):
        super().__init__(Name, Age, Sex)
        #super.__init__(self,Name, Age, Sex)
        self.Emp_ID = Emp_ID
        Employee.employee_count += 1

    def Print_Employee_Details(self):
        #Person.Print_Person_Details(self)
        print("Employee Details are",self.Print_Person_Details(),self.Emp_ID)

    def get_employee_count(self):
        print("Total Number of employees are: ", self.employee_count)

class Passenger(Person):
    flight_details = None
    passenger_count = 0
    def __init__(self, Name, Age, Sex, ID_No, flight):
        Person.__init__(self,Name, Age,Sex)
        self.ID_No = ID_No
        self.flight_details = flight.get_Flight_Details()
        Passenger.passenger_count += 1

    def Print_Passenger_Details(self):
        #Person.Print_Person_Details(self)
        print("Passenger Details are",self.Print_Person_Details(),self.ID_No , "and Flight details are", self.flight_details )

    def get_passenger_count(self):
        print("Total Number of passengers are: ", self.passenger_count)

class Pilot(Person, Flight):
    pilot_count = 0
    assigned_flight = None
    def __init__(self, Name, Age, Sex, Pilot_ID, flight):
        Person.__init__(self,Name, Age, Sex)
        self.assigned_flight = flight.get_Flight_Details()
        self.Pilot_ID = Pilot_ID
        Pilot.pilot_count += 1

    def pilot_Details(self):
        print("Pilot Details are",Person.Print_Person_Details(self),self.Pilot_ID,"and assigned flight detils are",self.assigned_flight)

    def get_pilot_count(self):
        print("Totlal number of pilots are: ", self.pilot_count)

if __name__ == '__main__':
    person1 = Person('Dj', 34, 'Male')
    flight1 = Flight(1234, 'Kansas', 'Chicago','Jun-10-18')
    flight2 = Flight(1235, 'New York', 'Dallas','Jun-15-18')
    passenger1 = Passenger('John', 25, 'Male', 'P3456', flight1)
    passenger2 = Passenger('Mary', 19, 'Female', 'P1234', flight2)
    passenger3 = Passenger('Rachel', 30, 'Female', 'P0787', flight1)
    Employee1 = Employee('Tom', 26, 'Male', 'E1231234')
    Employee2 = Employee('Monica', 23, 'Female', 'E1231289')
    pilot1 = Pilot('Ross', 35, 'Male', 'P123', flight1)

    Employee1.Print_Employee_Details()
    Employee2.Print_Employee_Details()
    passenger1.Print_Passenger_Details()
    passenger2.Print_Passenger_Details()
    passenger3.Print_Passenger_Details()
    pilot1.pilot_Details()
    pilot1.get_pilot_count()
    person1.get_person_count()
    flight1.get_flight_count()
    passenger1.get_passenger_count()
    Employee1.get_employee_count()


