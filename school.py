class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class MoneyException(Exception):
    def __init__(self, value):
        self.value = value


class Fellow(Person):
    number_of_fellows = 0

    def __repr__(self):
        return """
        Name:           {}
        Nationality:    {}
        """.format(self.name, self.nationality)

    def __init__(self, name, nationality, happiness_level):

            if Fellow.number_of_fellows == 4:
                try:
                    raise MoneyException('MoneyException:We cannot afford to hire {}'.format(name))
                except MoneyException:
                    print('MoneyException:We cannot afford to hire {}'.format(name))
            else:
                super().__init__(name, nationality)
                self.happiness_level = happiness_level
                Fellow.number_of_fellows += 1

    def eat(self, happiness_level):
        self.happiness_level = happiness_level
        happiness_level += 1

    def teach(self, happiness_level):
        self.happiness_level = happiness_level
        happiness_level -= 1


class EIT(Person):

    def __repr__(self):
        return """
        Name:           {}
        Nationality:    {}
        """.format(self.name, self.nationality)

    def __init__(self, name, nationality, fun_facts=[]):
        nationalities = ['Kenya', 'South Africa', 'Ghana', 'Nigeria', 'Ivory Coast']
        if nationality in nationalities:
            super().__init__(name, nationality)
            self.fun_facts = fun_facts
        else:
            print("Nationality is not allowed")

    def create_fun_fact(self, fun_fact):
        self.fun_facts.append(fun_fact)


class School:
    def __init__(self, eits=[], fellows=[]):
        self.eits = eits
        self.fellows = fellows

    def add_fellow(self, fellow):
        self.fellows.append(fellow)
        for fellow in self.fellows:
            print(fellow)

    def add_eit(self, eit):
        self.eits.append(eit)


mest = School()