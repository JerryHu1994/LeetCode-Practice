from threading import Lock
class Foo:
    def __init__(self):
        self.firstjobdone = Lock()
        self.secondjobdone = Lock()
        self.firstjobdone.acquire()
        self.secondjobdone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstjobdone.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.firstjobdone.acquire()
        printSecond()
        self.secondjobdone.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.secondjobdone.acquire()
        printThird()