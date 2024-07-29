class BrowserHistory:

    def __init__(self, homepage: str):
        self.backq = [homepage]
        self.forwardq = []

    def visit(self, url: str) -> None:
        self.backq.append(url)
        self.forwardq = []

    def back(self, steps: int) -> str:
        ind = 0
        while ind < steps and len(self.backq) > 1:
            self.forwardq.append(self.backq.pop())
            ind += 1
        return self.backq[-1]

    def forward(self, steps: int) -> str:
        if len(self.forwardq) == 0: return self.backq[-1]
        ind = 0
        while ind < steps and len(self.forwardq) > 0:
            self.backq.append(self.forwardq.pop())
            ind += 1
        return self.backq[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)