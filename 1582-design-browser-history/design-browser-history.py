class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_site = Node(url)
        new_site.prev = self.current
        self.current.next = new_site
        self.current = new_site

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != None:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next != None:
            self.current = self.current.next
            steps -= 1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)