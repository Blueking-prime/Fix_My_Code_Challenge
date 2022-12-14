#!/usr/bin/python3
'''This is a square'''

class Square():
    '''This is a square's documentation'''

    width = 0
    height = 0


    def __init__(self, *args, **kwargs):
        '''Initializes the instance'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        ''' Perimeter of a square '''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        ''' Returns a string in the form width/height '''
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
