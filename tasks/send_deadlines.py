from database import DeadlinesModel, StudentsModel


async def send_deadlines():
    print("before get deadlines")
    deadlines = await DeadlinesModel.get_deadlines()
    print("after get deadlines")
    print(deadlines)





