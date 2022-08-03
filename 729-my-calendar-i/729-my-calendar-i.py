
class MyCalendar:

    def __init__(self):
        self.bookings = {}
        

    def book(self, s1: int, e1: int) -> bool:
        for s2, e2 in self.bookings.items():
            if not (s1 >= e2 or s2 >= e1):
                return False
        self.bookings[s1] = e1
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)