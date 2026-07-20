class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets



reebok = Factory("leather", 10, 6)

print(reebok.zips)
