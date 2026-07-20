class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f" Your object details are {self.material} , {self.pockets} , {self.zips}")    


reebok = Factory("leather", 10, 6)
campus = Factory("nylon" , 5 , 8)

reebok.show()
campus.show()