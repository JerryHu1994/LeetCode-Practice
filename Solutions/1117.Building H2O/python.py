from threading import Lock
class H2O:
    def __init__(self):
        self.h1 = Lock()
        self.h2 = Lock()
        self.count_h = 0
        self.o = Lock()
        self.h2.acquire()
        self.o.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        if self.count_h == 0:
            self.h1.acquire()
        else:
            self.h2.acquire()
        self.count_h += 1
        releaseHydrogen() 
        if self.count_h == 1:
            self.h2.release()
        else:
            self.o.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o.acquire()
        releaseOxygen()
        self.count_h = 0
        self.h1.release()