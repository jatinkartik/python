class Train:
    def __init__(self,name,price,seat):
        self.name = name
        self.price = price
        self.seat = seat
    def bookTicket(self,user):
        self.user = user
        if self.seat > 0:
            print(f"welcome {user}, your seat is now booked ")
            self.seat = self.seat -1
            print(self.seat," seats now left")
        else:
            print("Seat is full please visit tatkaal")
    def getStatus(self):
        if self.seat > 0:
            print("Seat is available, you can book now!")
        else:
            print("No seat available")
    def cancelTicket(self,user):
        print(f"hello user {self.user}, your ticket is now cancelled ")
        self.seat = self.seat + 1
        
    
admin = Train("harry",55,4)
admin.getStatus()
admin.bookTicket("jatin")
admin.bookTicket("kartik")
admin.bookTicket("tyagi")
admin.bookTicket("mani")
admin.bookTicket("manni")
admin.bookTicket("manni")
admin.bookTicket("manni")
admin.getStatus()
admin.cancelTicket("manni")
admin.getStatus()
