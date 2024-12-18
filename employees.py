"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my honor, Luke Guequierre, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: lkg746
"""

from abc import ABC, abstractmethod
import random

DAILY_EXPENSE = 60
HAPPINESS_THRESHOLD = 50
MANAGER_BONUS = 1000
TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD = 50
PERM_EMPLOYEE_PERFORMANCE_THRESHOLD = 25
RELATIONSHIP_THRESHOLD = 10
INITIAL_PERFORMANCE = 75
INITIAL_HAPPINESS = 50
PERCENTAGE_MAX = 100
PERCENTAGE_MIN = 0
SALARY_ERROR_MESSAGE = "Salary must be non-negative."


class Employee(ABC):
    """
    Abstract base class representing a generic employee in the system.
    """

    def __init__(self, name, manager, salary, savings):
        self.relationships = {}
        self.savings = savings
        self.is_employed = True
        self.__name = name
        self.__manager = manager
        self._performance = INITIAL_PERFORMANCE
        self._happiness = INITIAL_HAPPINESS
        if salary >= 0:
            self._salary = salary
        else:
            raise ValueError

    @property
    def salary(self):
        """
        Returns hidden variable "salary"
        """
        return self._salary

    @salary.setter
    def salary(self, new):
        """
        Sets hidden variable "salary"
        """
        if new >= 0:
            self._salary = new
        else:
            raise ValueError

    @property
    def performance(self):
        """
        Returns hidden variable "performance"
        """
        return self._performance

    @performance.setter
    def performance(self, new):
        """
        Sets hidden variable "performance"
        """
        if new > 100:
            self._performance = 100
        elif new < 0:
            self._performance = 0
        else:
            self._performance = new

    @property
    def happiness(self):
        """
        Returns hidden variable "performance"
        """
        return self._happiness

    @happiness.setter
    def happiness(self, new):
        """
        Sets hidden variable "performance"
        """
        if new > 100:
            self._happiness = 100
        elif new < 0:
            self._happiness = 0
        else:
            self._happiness = new

    @property
    def name(self):
        """
        Returns hidden variable "name"
        """
        return self.__name

    @property
    def manager(self):
        """
        Returns hidden variable "manager"
        """
        return self.__manager

    @abstractmethod
    def work(self):
        """
        Abstract method intended to prevent pure employees from being created
        """

    def interact(self, other):
        """
        Simulates an interaction betweeen two employees
        """
        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        if self.relationships[other.name] > RELATIONSHIP_THRESHOLD:
            if self.happiness + 1 <= 100:
                self.happiness += 1
        else:
            if self.happiness >= HAPPINESS_THRESHOLD and other.happiness >= HAPPINESS_THRESHOLD:
                self.relationships[other.name] += 1
            else:
                self.relationships[other.name] -= 1
                if self.happiness - 1 >= 0:
                    self.happiness -= 1

    def daily_expense(self):
        """
        Simulates how the employee is altered by a day of work
        """
        if self.happiness - 1 >= 0:
            self.happiness -= 1
        self.savings -= DAILY_EXPENSE

    def __str__(self):
        return f'{self.__name}\n\tSalary: ${self._salary}\n\tSavings: ${self.savings}\n\tHappiness: {self.happiness}%\n\tPerformance: {self.performance}%'


class Manager(Employee):
    """
    A subclass of Employee representing a manager.
    """
    def work(self):
        """
        Simulates how the manager is effected by one hour of work.
        """
        delta_perf = random.randint(-5,5)
        if delta_perf + self.performance <= 100 and delta_perf + self.performance >= 0:
            self.performance += delta_perf
        elif delta_perf > 0:
            self.performance = 100
        else:
            self.performance = 0
        if delta_perf <= 0:
            if self.happiness - 1 >= 0:
                self.happiness -= 1
            for relationship in self.relationships:
                self.relationships[relationship] -= 1
        else:
            if self.happiness + 1 <= 100:
                self.happiness += 1


class TemporaryEmployee(Employee):
    """
    A subclass of Employee representing a temporary employee.
    """
    def work(self):
        """
        Simulates how a temporary employee is effected by one hour of work.
        """
        delta_perf = random.randint(-15,15)
        if delta_perf + self.performance <= 100 and delta_perf + self.performance >= 0:
            self.performance += delta_perf
        elif delta_perf > 0:
            self.performance = 100
        else:
            self.performance = 0
        if delta_perf <= 0:
            if self.happiness - 2 >= 0:
                self.happiness -= 2
            else:
                self.happiness = 0
        else:
            if self.happiness + 1 <= 100:
                self.happiness += 1

    def interact(self, other):
        """
        Simulates how a temporary worker is effected by an interaction with a manager
        """
        super().interact(other)
        if isinstance(other, Manager):
            if other.happiness >= HAPPINESS_THRESHOLD:
                if self.performance >= TEMP_EMPLOYEE_PERFORMANCE_THRESHOLD:
                    self.savings += MANAGER_BONUS
            elif other.happiness < HAPPINESS_THRESHOLD:
                self.salary = self.salary // 2
                if self.happiness - 5 >= 0:
                    self.happiness -= 5
                else:
                    self.happiness = 0
                if self.salary <= 0:
                    self.is_employed = False


class PermanentEmployee(Employee):
    """
    A subclass of Employee representing a permanent employee.
    """
    def work(self):
        """
        Simulates how a pernmanent employee is effected by one hour of work.
        """
        delta_perf = random.randint(-10,10)
        if delta_perf + self.performance <= 100 and delta_perf + self.performance >= 0:
            self.performance += delta_perf
        elif delta_perf > 0:
            self.performance = 100
        else:
            self.performance = 0
        if delta_perf >= 0:
            if self.happiness + 1 <= 100:
                self.happiness += 1

    def interact(self, other):
        """
        Simulates how a permanent worker is effected by an interaction with a manager
        """
        super().interact(other)
        if isinstance(other, Manager):
            if other.happiness >= HAPPINESS_THRESHOLD:
                if self.performance >= PERM_EMPLOYEE_PERFORMANCE_THRESHOLD:
                    self.savings += MANAGER_BONUS
            elif other.happiness < HAPPINESS_THRESHOLD:
                if self.happiness - 1 >= 0:
                    self.happiness -= 1
