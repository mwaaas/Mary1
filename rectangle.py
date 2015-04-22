class Rectangle:
    def __init__(self,__length=1,__width=1):
        self.setlength(__length)
        self.setwidth(__width)
        #self.__length=1
        #self.__width=1
    def setlength(self, __length):
        if(0.0< __length <20.0):
            self.__length =__length
        else:
            raise ValueError, "Invalid length value:", __length
    def setwidth(self, __width):
        if(0.0<__width < 20.0):
            self.__width=__width
        else:
            raise ValueError, "Invalid width value:", __width
    def getlength(self):
        return self.__length

    def getwidth(self): 
        return self.__width

    def display(self):
        print "the length is",self.__length

    def perimeter(self):
        p=2*(self.__length  + self.__width)
        #if i write p=2(self.__length  + self.__width),i get the error
        #p=2(self.__length  + self.__width) TypeError: 'int' object is not callable
        return p
         

    def area(self):
        a=self.__length * self.__width
        return a

    '''reason for the error above You are trying to use 2 as a function:
     2(-1/6.)
     Insert a * to multiply:

     2*(-1/6.)
     or as a full expression:

     s=s+d*2*(-1/6.)*(u-1)*(u-2)*(u+2)*(u-4)'''
            
