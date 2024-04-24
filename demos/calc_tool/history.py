# defines a contract - yes, this is an interface
from typing import Protocol


# protocol uses structural typing
class History(Protocol):
    def get_history(self) -> list[tuple[int, str, float]]: ...

    def append_history_entry(self, operation: str, operand: float) -> None: ...

    def remove_history_entry(self, entry_id: int) -> None: ...

    def clear_history_entries(self) -> None: ...


# class Person:
#     def full_name(self) -> str:
#         return ""


# class OtherPerson:
#     def full_name(self) -> str:
#         return ""

# # nominal typing
# person: Person = Person()

# person2: OtherPerson = Person()

# # typescript example

# class Person {
#     full_name() { return "" }
# }

# interface PersonB {
#     full_name(): string
# }

# type PersonC = {
#     full_name(): string
# }

# # valid in typescript, structural typing
# const p: PersonC = new Person();
