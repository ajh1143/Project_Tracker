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

    #def setMemberTask(self, task, member):
        #self.Assigned = {task:member}

    #def getMemberTask(self):
       # return self.Assigned

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
TaskList1 = ["Task A", "Task B", "Task C"]
MemberList1 = ["aaron", "mike", "dave"]
myClass = Tasks("Project A", TaskList1, MemberList1)
myClass.setMembers(MemberList1)
myClass.setTaskList(TaskList1)
print(myClass.getTaskList())
print(myClass.getMembers())
myClass.updateTaskList("Task A", "complete")
print(myClass.getTaskList())
