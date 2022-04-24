class kasr:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m

    def sum(self, mehman):
        result = kasr(None, None)
        result.soorat = self.soorat * mehman.makhraj + self.makhraj * mehman.soorat
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def div(self, mehman):
        result = kasr(None, None)
        result.soorat = self.soorat * mehman.makhraj
        result.makhraj = self.makhraj * mehman.soorat
        return result

    def sub(self, mehman):
        result = kasr(0, 0)
        result.soorat = self.soorat * mehman.makhraj - self.makhraj * mehman.soorat
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def mul(self, mehman):
        result = kasr(0, 5)
        print(result.soorat)
        result.soorat = self.soorat * mehman.soorat
        result.makhraj = self.makhraj * mehman.makhraj
        return (result)

    def convert_time_second(self):
        seconds = int(self.hour) * 3600 + int(self.minute) * 60 + int(self.second)
        return(seconds)

    def show(self):
        print(self.soorat, '/', self.makhraj)


a = kasr(3, 5)
b = kasr(5, 3)
c = a.mul(b)
c.show()
d = a.sub(b)
d.show()
e = a.div(b)
e.show()
f = a.sum(b)
f.show()
