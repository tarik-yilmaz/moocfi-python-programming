# Write your solution here:
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
        return list(set(order for order in self.orders if order.is_finished()== True))

    def unfinished_orders(self):
        return list(set(order for order in self.orders if order.is_finished() == False))

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



if __name__ == "__main__":

    # Test of part 1
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)
    print("--------------------------\n")

    # Test of part 2
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)
    print("--------------------------\n")

    # Test of part 3
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)
    print("--------------------------\n")


    # Test of part 4
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
        