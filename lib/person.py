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
    def __init__(self, name='Guido', job='Sales'):
        self.name = name
        self.job = job
    
    @property
    def name(self):
        return self._name.title()
        

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) <= 25:
            self._name = new_name
        else:
            self._name = None 
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
        

    @job.setter
    def job(self, new_job):
        if new_job in APPROVED_JOBS:
            self._job = new_job
        else:
            self._job = None 
            print("Job must be in list of approved jobs.")

guido = Person("Guido")
print(guido.name)        
            

    
