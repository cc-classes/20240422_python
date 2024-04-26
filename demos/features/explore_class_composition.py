# composition defines "has-a" relationship
# Person has-a StudentRole


class StudentRole:
    def __init__(self, sid: str) -> None:
        self.student_id = sid

    def record_info(self, fn: str, ln: str) -> str:
        return f"{self.student_id} {ln}, {fn}"


class Person:
    def __init__(self, fn: str, ln: str) -> None:
        self.first_name = fn
        self.last_name = ln

    def assign_student_role(self, student_role: StudentRole) -> None:
        self.student_role = student_role

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def record_info(self) -> str:
        return self.student_role.record_info(self.first_name, self.last_name)


student1 = Person("Bob", "Smith")
student1.assign_student_role(StudentRole(1))
print(student1.full_name())
print(student1.record_info())
