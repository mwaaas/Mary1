from rectangle import Rectangle
def printvalue(values):
    values.perimeter()
    print
    values.area()
    print
firstrec = Rectangle()
secondrec = Rectangle(8.5,12.2)
thirdrec = Rectangle(10.6,10.1)

secondrec.display()
print "for first rectangle, values are perimeter and area respectively",
firstrec.perimeter()
print "for second rectangle, values are perimeter and area respectively",
printvalue(secondrec)
print "for third rectangle, values are perimeter and area respectively",
printvalue(thirdrec)


