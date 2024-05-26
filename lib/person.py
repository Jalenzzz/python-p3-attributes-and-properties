#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name: str = "", job: str = ""):
        self.name = name
        self.job = job

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            print("Name must be a string.")
        elif not 1 <= len(value) <= 25:
            print("Name must be between 1 and 25 characters.")
        else:
            self._name = value.title()

    @property
    def job(self) -> str:
        return self._job

    @job.setter
    def job(self, value: str):
        if value not in Person.APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value
