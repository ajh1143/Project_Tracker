class Tasks:
    def __init__(self, ProjectName, TaskList, Members):
        self.ProjectName = ProjectName
        self.TaskList = TaskList
        self.Members = Members

    def getTaskList(self):
        return self.TaskList

    def setTaskList(self, List):
        self.TaskList = List

    def getMembers(self):
        return self.Members

    def setMembers(self, Members):
        self.Members = Members

 def setMemberTask(self, Assignment, task, *member):
        self.task = task
        self.member = member
        self.Assignment = Assignment
        self.Assignment.setdefault(self.task, [])
        self.Assignment[self.task].append(member)
        return self.Assignment


    def getMemberTask(self):
        return self.Assignment

    def updateTaskList(self, task, choice):
        self.task = task
        self.choice = choice
        if self.choice == "complete":
            for x in self.TaskList:
                if x == task:
                    print("DELETING TASK...")
                    self.TaskList.remove(x)
                    print("Tasks Remaining: " + str(len(self.TaskList)))

#testing logic
AssignedList = {}
TaskList1 = ["Task A", "Task B", "Task C"]
MemberList1 = ["Aaron", "Mike", "Dave"]
myClass = Tasks("Project A", "Task A", MemberList1)
members_list = myClass.setMembers(MemberList1)
list_of_tasks = myClass.setTaskList(TaskList1)
assigned_tasks = myClass.setMemberTask(AssignedList, "Task A", "Aaron", "Brian")
assigned_tasks = myClass.setMemberTask(AssignedList, "Task B", "Mike", "Chet")
assigned_tasks = myClass.setMemberTask(AssignedList, "Task C", "Greg", "Sharon" )
assignments = myClass.getMemberTask()
pprint(assignments)
