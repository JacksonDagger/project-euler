class grid:
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

        
