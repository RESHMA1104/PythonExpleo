class TeamMember:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def display(self):
        print(f"TeamMember : {self.name}, UID: {self.uid}")


class Worker:
    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle

    def display(self):
        print(f"Worker : {self.jobtitle}, Pay : {self.pay}")


class TeamLeader(TeamMember, Worker):
    def __init__(self, name, uid, pay, jobtitle, exp):
        self.exp = exp
        super().__init__(name, uid)             # calls TeamMember
        Worker.__init__(self, pay, jobtitle)    # manually call Worker

    def display(self):
        super().display()   # calls TeamMember.display()
        Worker.display(self)
        print(f"Experience : {self.exp}")


tl = TeamLeader("Jake", 10001, 2500000, "Scrum Master", 5)
tl.display()