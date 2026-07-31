# Write your solution here

class Checklist:
    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries

class Customer:
    def __init__(self, id: str, balance: float, discount: int):
        self.id = id
        self.balance = balance
        self.discount = discount


class Cable:
    def __init__(self, model: str, length: float, max_speed: int, bidirectional: bool):
        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


if __name__ == "__main__":
    check = Checklist("First Purchase", ["short aux cable, long aux cable"])
    customer = Customer("1", 5000.00, 1000)
    cable = Cable("best  model", 3.00, 280, True)

    print(f"Checklist:\nHeader: {check.header}, Entries: {check.entries}")
    print(f"Customer:\nID: {customer.id}, Balance: {customer.balance}, Discount: {customer.discount}")
    print(f"Cable:\nLength: {cable.length}, Max Speed: {cable.max_speed}, Bidirectionality: {cable.bidirectional}")