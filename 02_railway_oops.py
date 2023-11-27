class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


nihasApplication = RailwayForm()
nihasApplication.name = "Niha"
nihasApplication.train = "Rajdhani Express"
nihasApplication.printData()