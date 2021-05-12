#Category(cid, catname), Expense(amount,date,remark,catid)

class Category():
    def setCatId(self, catid):
        self.catid = catid
    def setCatName(self, catname):
        self.catname = catname

    def getCatId(self):
        return self.catid
    def getCatName(self):
        return self.catname

class Expense():
    def setAmount(self, amount):
        self.amount = amount
    def setDate(self, date):
        self.date = date
    def setRemark(self, remark):
        self.remark = remark
    def setCategoryId(self, cid):
        self.cid = cid


    def getAmount(self):
        return self.amount
    def getRemark(self):
        return self.remark
    def getDate(self):
        return self.date
    def getCategoryId(self):
        return self.cid
