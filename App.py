from models import Category, Expense

class Service:
    choice = 0
    catList = []
    expList = []
    
    def startApp(self):
        while True:
            self.printOptions()
            if Service.choice == 1:
                self.addCategory()
            elif Service.choice == 2:
                self.categoryListing()
            elif Service.choice == 3:
                self.expenseEntry()
            elif Service.choice == 4:
                self.reportCatWise()
            elif Service.choice == 5:
                self.reportMonthWise()
            elif Service.choice == 7:
                print(Service.catList)
                break
        

    def printOptions(self):
        print("1. Add Category")
        print("2. Category Listing")
        print("3. Expense Entry")
        print("4. Report (Category wise)")
        print("5. Report (Month-Year)")
        print("6. Report (Month-range)")
        print("7. Exit")
        Service.choice = int(input("Enter your choice: "))

    def addCategory(self):
        cid = int(input("Enter Category ID: "))
        cname = input("Enter Category Name: ")

        c = Category()
        c.setCatId(cid)
        c.setCatName(cname)

        Service.catList.append(c)
        print("Category Added!")

    def categoryListing(self):
        j = 1
        for i in Service.catList:
            print(j, i.getCatName())
            j += 1
        print("==============")

    def getCatIdByUser(self):
        self.categoryListing()
        catNum = int(input("Select Category: "))

        catObj = Service.catList[catNum-1]
        catid = catObj.getCatId()
        return catid

    def expenseEntry(self):
        catid = self.getCatIdByUser()

        amount = float(input("Enter Amount: "))
        remark = input("Enter Remark: ")
        date = input("Enter Date (dd/mm/yyyy): ")

        
        e = Expense()
        
        e.setAmount(amount)
        e.setRemark(remark)
        e.setDate(date)
        e.setCategoryId(catid)

        Service.expList.append(e)
        print("Expense Added successfully...")


    def reportCatWise(self):
        catid = self.getCatIdByUser()
        
        for i in Service.expList:
            if i.getCategoryId() == catid:
                print(i.getAmount(), i.getRemark(), i.getDate())

    
    def reportMonthWise(self):
        month = int(input("Enter Month (01/12): "))
        year = int(input("Enter Year: "))

        for i in Service.expList:
            dt = i.getDate()#dd/mm/yyyy
            newDt = dt.split("/")#['dd', 'mm', 'yyyy']
            if month == int(newDt[1]) and year == int(newDt[2]):
                print(i.getAmount(), i.getRemark(), i.getDate())


"""
Task1: Month range: 04 06, 2020
Task2: Exception handling for complete code
Task3: Uniqueness of Category ID at the time of adding cat./generating random catid
"""


        


Service().startApp()
