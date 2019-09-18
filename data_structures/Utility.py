#import sys
class Utility:
    
    def beg_week_of_month(month_find, year_find):
        d = int(1)
        m = int(month_find)
        y = int(year_find)
        try:
            if ((m in range(1,13)) and (y > 0 ) ):
                if(m == 1):
                    m = 13
                    y = y-1
                elif(m == 2):
                    m = 14
                    y = y-1
                
                N = int(d + 2*m + int(3*(m+1)/5) + y + int(y/4) - int(y/100) + int(y/400) + 2)
        
                N_new = N%7

                return N_new
        except:
            print("Error in the month or year !!!!")
    
    def leap_year_find(year):

        if(year in range(1000,10000)):
            if(year%400 == 0):
                return True
            elif((year%4 == 0) and (year%100 !=0)):
                return True
            else:
                return False


    def month_days(month, year):
        
        mon = month
    
        if(mon == 2):
            is_leap = Utility.leap_year_find(year)
            if(is_leap):
                return 29
            else:
                return 28
        elif month in [1,3,5,7,8,10,12]:
            return 31
        else:
            return 30


if __name__ == "__main__":

    rem = Utility.beg_week_of_month(1,1998)
    print(rem)

