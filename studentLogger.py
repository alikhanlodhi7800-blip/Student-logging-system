from abc import ABC, abstractmethod
from datetime import datetime

class User:
    def __init__(self,user_id,name):
        self.__user_id = user_id
        self.__name = name

    def get_id(self):
        return self.__user_id
    
    def get_name(self):
        return self.__name
    
    def display(self):
        print(f"User id: {self.__user_id}")
        print(f"Name:{self.__name}")

class Student(User):
    def __init__(self, user_id,name,department):
        super().__init__(user_id,name)
        self.department = department
        self.attendence = []

    def mark_attendence(self,status):
        date = datetime.now().strftime("%Y-%m-%d")
        self.attendence.append((date,status))

    def display(self):
        print("/n----Student Details----")
        print(f"ID: {self.get_id()}")
        print(f"Name:{self.get_name()}")
        print(f"Department:{self.department}")

class Admin(User):
    def __init__(self, user_id,name,role):
        super().__init__(user_id,name)
        self.role = role

    def manage_system(self):
        print(f"Admin {self.get_name()} is managing the system")

class Attendence:
    def __init__(self):
        self.records = {}

    def add_record(self,student,status):
        self.records[student.get_name()] = status

    def show_records(self):
        print("/nAttendence Records")
        for student, status in self.records.items():
            print(f"{student} --> {status}")

class LoggerSystem:
    def __init__(self):
        self.logs = []
    
    def add_log(self,message):
        time = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{time}] {message}")

    def show_logs(self):
        print("/nSystem Logs")
        for log in self.logs:
            print(log)

class ErrorDetector:
    def check_errors(self, records):
        print("/nChecking Errors...")
        for student, status in records.items():
            if status not in ["Present", "Absent"]:
                print(f'Invalid attendence found for {student}')

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class ReportGenerator(Report):
    def __init__(self,attendence):
        self.attendence = attendence

    def generate(self):
        print("/n===== Attendence Report =====")
        for student, status in self.attendence.records.items():
            print(f"{student} : {status}")

class SmartStudent(Student):
    def __init__(self, user_id,name,department,cgpa):
        super().__init__(user_id,name,department)
        self.cgpa = cgpa

    def scholarship_status(self):
        if self.cgpa >= 3.5:
            print(f"{self.get_name()} is eligible for scholarship")
        else:
            print(f"{self.get_name()} is not eligible for scholarship")

attendence_system = Attendence()
logger = LoggerSystem()
error_detector = ErrorDetector()

student1 = Student(1,"Ali","Data Science")
student2 = SmartStudent(2,"Ahmed","IT",3.8)
admin1 = Admin(101,"Sir Hamza","System admin")

student1.display()
student2.display()

student1.mark_attendence("Present")
student2.mark_attendence("Absent")

attendence_system.add_record(student1, "Present")
attendence_system.add_record(student2,"Absent")

attendence_system.show_records()

logger.add_log("Ali logged into the system")
logger.add_log("Ahmed marked attendence")
logger.show_logs()

admin1.manage_system()

error_detector.check_errors(attendence_system.records)
Report = ReportGenerator(attendence_system)
Report.generate()
student2.scholarship_status()
