class sar:
    def __init__(self , x ,y):
        self.x = x
        self.y = y
    def draw(self):
        print("draw")
    def start(self):
        print("start")


sarthak = sar(10, 20)
print(sarthak.x)
print(sarthak.y)
