import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

jashsApplication = RailwayForm()
jashsApplication.name = "Jash"
jashsApplication.train = "Rajdhani Express"
jashsApplication.printData()