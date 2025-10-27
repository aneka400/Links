import tracemalloc
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print(1)
            cls.obj=range(0, 10_000_000_000)
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
    def __init__(self)-> None:
        ...
    
    def foo(self):
        return "Singleton"

class NotSingleton(object):
    def __init__(self) -> None:
        self.obj=range(0, 10_000_000_000)
    
    def foo(self):
        return "NotSingleton"
    
if __name__ == '__main__':
    """
    singleton1 = Singleton()
    print(id(singleton1))
    singleton2 = Singleton()
    print(id(singleton2))

    not_singleton1 = NotSingleton()
    print(id(not_singleton1))
    not_singleton2 = NotSingleton()
    print(id(not_singleton2))
    """
    tracemalloc.start()
    rs = []
    for _ in range(0,1000):
        singleton3 = Singleton()
        singleton3.foo()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

    tracemalloc.start()
    for _ in range(0,1000):
        not_singleton3 = NotSingleton()
        not_singleton3.foo()
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()