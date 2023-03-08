"""Python serial number generator."""

class SerialGenerator():
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self,start):
        '''
        Creates two instances beginning with starting argument
        '''
        self.a = start
        self.b = start
    
    def generate(self):
        '''
        adds 1 every time it is generated; beginning with 1 less, so it starts
        at the starting argument
        '''
        self.b += 1
        return self.b -1
    
    def reset(self):
        '''
        'a' is kept as starting argument, so we can recall it during reset
        '''
        self.b = self.a
        return self.a
    