class time():
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def sub_of_time(self, mehman):
        result = time(None,None,None)
        result.hour = self.hour - mehman.hour
        result.minute = self.minute - mehman.minute
        result.second = self.second - mehman.second
        return(result)

    def sub_of_time(self, mehman):
        result = time(None,None,None)
        result.hour = self.hour + mehman.hour
        result.minute = self.minute + mehman.minute
        result.second = self.second + mehman.second
        return(result)

    def standard_of_time(self):
        while self.second >= 60:
            self.second -= 60
            self.minute += 1
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        while self.second < 0:
            self.second += 60
            self.minute -= 1
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        return(self)

    def convert_second_time(self):
        while self.second >= 60:
            self.minute = self.second // 60
            self.second = self.second % 60
            while self.minute >= 60:
                self.minute -= 60
                self.hour += 1
        return(self)


    def convert_time_second(self):
        seconds = int(self.hour) * 3600 + int(self.minute) * 60 + int(self.second)
        print('Tne entire time is:', seconds, 'seconds')


    def show(self):
        print (self.hour , ':' , self.minute , ':', self.second)


def time_menu():
        choice = int(input(
            'summation press 1,'
            'subtraction press 2,'
            'convet second to time press 3,'
            'convert time to second enter 4:'))
        if choice == 1:
            t1 = time(int(input('Enter hour: ')),int(input('Enter minute: ')),int(input('Enter second: ')))
            t2 = time(int(input('Enter hour: ')),int(input('Enter minute: ')),int(input('Enter second: ')))
            sub = t1.sub_of_time(t2)
            sub.standard_of_time()
            sub.show()
        elif choice == 2:
            t1 = time(int(input('Enter hour: ')), int(input('Enter minute: ')), int(input('Enter second: ')))
            t2 = time(int(input('Enter hour: ')), int(input('Enter minute: ')), int(input('Enter second: ')))
            sum = t1.sub_of_time(t2)
            sum.standard_of_time()
            sum.show()
        elif choice == 3:
            t3 = time(0, 0, int(input('Enter seconds:')))
            t3 = t3.convert_second_time()
            t3.show()
        elif choice == 4:
            t4 = time(int(input('Enter hour: ')),int(input('Enter minute: ')),int(input('Enter second: ')))
            t4.show()
            t4.convert_time_second()
            t4.show()
        else:
            print('Enter a valid number')


time_menu()