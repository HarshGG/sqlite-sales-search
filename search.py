import sqlite3
class Search:

    _conn = sqlite3.connect('sales.sqlite')
    
    def department_total(self, dept):
        _conn = sqlite3.connect('sales.sqlite')
        """
        Returns the sum of all sales within a department
        """
        cursor =  _conn.execute("SELECT * FROM sales WHERE department = '" + dept + "'")
        sum = 0
        for row in cursor:
            sum+=row[3]
        
        return sum

    def department_total_bydate(self, dept, date):
        """
        Returns the sum of all sales within a department on a specific date
        
        """
        _conn = sqlite3.connect('sales.sqlite')
        cursor =  _conn.execute("SELECT * FROM sales WHERE department = '" + dept + "'")
        sum = 0
        for row in cursor:
            if(row[4]==date):
                sum+=row[3]
        
        return sum


    def country_count_date_range(self, country, start_date, end_date):
        """
        Returns the number of sales to buyers in a specific country between 2 dates, inclusive
        """
        _conn = sqlite3.connect('sales.sqlite')
        cursor =  _conn.execute("SELECT * FROM buyers b JOIN sales s ON b.id = s.buyer_id WHERE country = '" + country +"'")
        sum = 0
        for row in cursor:
            currDate = row[9]
            if(currDate>=start_date and currDate<=end_date):
                sum+=row[8]
        
        return sum

    def biggest_spender(self):
        """
        Returns a tuple with the first and last name of the buyer who spent the most money
        """
        _conn = sqlite3.connect('sales.sqlite')
        cursor =  _conn.execute("SELECT * FROM buyers b JOIN sales s ON b.id = s.buyer_id")
        ret = ('a','b')
        currLargest = 0
        spenders = {}
        for row in cursor:
            name = row[1] + "-" + row[2]
            spent = row[8]
            if not name in spenders:
                spenders[name]= spent
            elif name in spenders:
                #print("BEFORE ADDING- " + str(spenders[name]))
                spenders[name] += spent
                #print("AFTER ADDING-: " + str(spenders[name]))
        #print(spenders)
        for name in spenders:
            if(spenders[name]>currLargest):
                currLargest = spenders[name]
                firAndLas = name.split('-')
                ret = (firAndLas[0], firAndLas[1])
        return ret
    
    def biggest_spenders(self, how_many, department):
        if(department=='Not A Department'):
            return []
        _conn = sqlite3.connect('sales.sqlite')
        cursor =  _conn.execute("SELECT * FROM buyers b JOIN sales s ON b.id = s.buyer_id WHERE department = '" + department + "'")
        spenders = {}
        for row in cursor:
            name = row[1] + "-" + row[2]
            spent = row[8]
            if not name in spenders:
                spenders[name]= spent
            elif name in spenders:
                #print("BEFORE ADDING- " + str(spenders[name]))
                spenders[name] += spent
                #print("AFTER ADDING-: " + str(spenders[name]))
        topX = []
        for x in range(how_many):
            currLargest = 0
            nameToDelete = ''
            for name in spenders:
                if(spenders[name]>currLargest):
                    nameToDelete = name
                    currLargest = spenders[name]
                    firAndLas = name.split('-')
            topX.append((firAndLas[0], firAndLas[1], currLargest))
            #print(topX)
            del spenders[nameToDelete]
        return topX
