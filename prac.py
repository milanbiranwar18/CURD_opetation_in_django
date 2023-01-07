from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def B(self):
        pass

    @abstractmethod
    def ab(self):
        pass


class C(A):
    def B(self):
        print('derived class')


obj = C()
obj.B()




