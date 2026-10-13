# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
    id  = 0

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.finished = False
        
        Task.id += 1
        self.id = Task.id

    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.is_finished() else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"    


class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set(order.programmer for order in self.orders))
    
    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return

        raise ValueError("Task not found")

    def finished_orders(self):
        return list(set(order for order in self.orders if order.is_finished()))

    def unfinished_orders(self):
        return list(set(order for order in self.orders if not order.is_finished()))

    def status_of_programmer(self, programmer: str):
        
        finished = [order for order in self.orders if order.programmer == programmer and order.is_finished()]
        unfinished = [order for order in self.orders if order.programmer == programmer and not order.is_finished()]

        if not finished and not unfinished:
            raise ValueError(f"Programmer {programmer} not found")
        
        return (len(finished), 
                      len(unfinished), 
                      sum(order.workload for order in finished),
                      sum(order.workload for order in unfinished)
        )


def run():
    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")

    orders = OrderBook()
    
    while True:

        command = int(input("command: "))

        if command == 0:
            return

        if command == 1:
            description = input("description: ")
            programmer_workload = input("programmer and workload estimate: ")
            
            try:
                programmer, workload = programmer_workload.split()    
                orders.add_order(description, programmer, int(workload))
                print("added! ")

            except (ValueError, TypeError):
                print("erroneous input")                        
            
        
        elif command == 2:
            if orders.finished_orders():
               for order in orders.finished_orders():
                   print(order)
            else:
                print("no finished tasks")

        elif command == 3:
            if orders.unfinished_orders():
                for order in orders.unfinished_orders():
                    print(order)
            else:
                print("no unfinished tasks")

        elif command == 4:
            try:
                id = int(input("id: "))
                orders.mark_finished(id)
                print("marked as finished")
            
            except (ValueError, TypeError):
                print("erroneous input")
        
        elif command == 5:
            for programmer in orders.programmers():
                print(programmer)

        elif command == 6:
            programmer = input("programmer: ")

            try:
                finished, unfinished, done, scheduled = orders.status_of_programmer(programmer)

                print(f"tasks: finished {finished} not finished {unfinished}, hours: done {done} scheduled {scheduled}")

            except (ValueError, TypeError):
                print("erroneous input")        
run()
