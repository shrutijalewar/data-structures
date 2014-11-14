class Queue1:
    data = []

    def enq(self, name):
        self.data.append(name)
    def deq(self):
        self.data.pop(0)

#dessert = Queue1()
#dessert.enq('pie')
#dessert.enq('cake')
