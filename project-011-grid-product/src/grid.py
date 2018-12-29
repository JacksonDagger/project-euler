import NotAGridException


class grid:
    #
    # Constructs a grid with a file. Throws NotAGridException if the file doesn't contain a grid (all lines contains the same number of ints)
    #
    def __init__(self, fname):
        f = open(fname, "r")
        if f.mode == 'r':
            flines = f.readlines()
            self.gridlist = []

            for x in flines:
                stringlist = x.split(" ")
                intlist = []
                for y in stringlist:
                    intlist.append(int(y))
                self.gridlist.append(intlist)

            self.width = len(self.gridlist[0])
            for x in self.gridlist:
                if len(x) != self.width:
                    raise NotAGridException.NotAGridException
            self.height = len(self.gridlist)
        else:
            raise NotAGridException.NotAGridException


    #
    # Returns the largest product of adjacent numbers in a straight line in the grid from size numbers
    #
    def get_product(self, size):
        if size > self.width and size > self.height:
            return 0
        retval = 0
        for x in range(self.width):
            for y in range(self.height):
                temp = self.get_local_product(x, y, size)
                if temp > retval:
                    retval = temp
        return retval

    #
    # Returns the grid's width
    #
    def get_width(self):
        return self.width


    #
    # Returns the grid's height
    #
    def get_height(self):
        return self.height


    #
    # Returns the largest adjacent product from the given coordinate
    #
    def get_local_product(self, x, y, size):
        retval = 0
        roomup = y + 1 - size >= 0
        roomdn = y + size <= self.height
        roomleft = x + 1 - size >= 0
        roomright = x + size <= self.width

        #up
        if roomup:
            temp = 1
            for inc in range(size):
                temp *= self.gridlist[y - inc][x]
            if temp > retval:
                retval = temp
        #down
        if roomdn:
            temp = 1
            for inc in range(size):
                temp *= self.gridlist[y + inc][x]
            if temp > retval:
                retval = temp
        #left
        if roomleft:
            temp = 1
            for inc in range(size):
                temp *= self.gridlist[y][x - inc]
            if temp > retval:
                retval = temp
        #right
        if roomright:
            temp = 1
            for inc in range(size):
                temp *= self.gridlist[y][x + inc]
            if temp > retval:
                retval = temp
        #upleft
        if roomleft and roomup:
            temp = 1
            for inc in range(size):
                temp *= self.gridlist[y - inc][x - inc]
            if temp > retval:
                retval = temp
        #upright
        if roomright and roomup:
            temp = 1
            for inc in range(size):
                temp *= self.gridlist[y - inc][x + inc]
            if temp > retval:
                retval = temp
        #downleft
        if roomleft and roomdn:
            temp = 1
            for inc in range(size):
                temp *= self.gridlist[y + inc][x - inc]
            if temp > retval:
                retval = temp
        #downright
        if roomright and roomdn:
            temp = 1
            for inc in range(size):
                temp *= self.gridlist[y + inc][x + inc]
            if temp > retval:
                retval = temp

        return retval



