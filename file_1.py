

''' in this task i neede to creat a class of greating cards and init with two given names 
for sender and reciver of the cards'''


class GreetingCard:

    def __init__(self):
        self._recipient = "Dana Ev"
        self._sender = "Eyal Ch"

    def greeting_msg(self):
        print(f"the sender is: {self._sender} the recipient is: {self._recipient}")


BDcrad = GreetingCard()
BDcrad.greeting_msg()
