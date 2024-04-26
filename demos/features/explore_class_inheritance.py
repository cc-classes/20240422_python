# inheritance defines "is-a" relationship
# Student is-a Person


class Person:
    def __init__(self, fn: str, ln: str) -> None:
        self.first_name = fn
        self.last_name = ln

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, sid: str, fn: str, ln: str) -> None:
        super().__init__(fn, ln)
        self.student_id = sid

    def record_info(self) -> str:
        return f"{self.student_id} {self.last_name}, {self.first_name}"


student1 = Student(1, "Bob", "Smith")
print(student1.full_name())
print(student1.record_info())
