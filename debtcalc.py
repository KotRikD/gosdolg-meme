import math
import datetime
import time

def calculateDebt(startYear,startMonth,startDay,baseDebt,perSecondDebt,yearPop,monthPop,dayPop,basePop,perSecondPop):
    one_day_m=1000*60*60*24
    one_day=60*60*24
    one_sec=1000
    one_tenthsec=100
    one_fifthsec=200
    one_halfsec=500

    startdate = datetime.date(startYear, startMonth-1, startDay)
    startPopdate = datetime.date(yearPop, monthPop-1, dayPop)

    startdate = int(time.mktime(startdate.timetuple()))
    startPopdate = int(time.mktime(startPopdate.timetuple()))

    currentUnfundedDebt= 1.14039E+14
    currentUnfundedDebtPerTenth = (168061.9)/10

    currentUnfundedSSDebt= 15100000000000.00
    currentUnfundedSSDebtPerTenth = (38333.21)/10
    currentUnfundedMediCareDebt= 79000000000000.00
    currentUnfundedMediCareDebtPerTenth = (98764.67)/10
    currentUnfundedDrugDebt= 19939000000000.00
    currentUnfundedDrugDebtPerTenth = (18456.11)/10
    currentUnfundedObamaCareDebt= 9200000000000.00
    currentUnfundedObamaCareDebtPerTenth = (7123.21)/10
    currentUnfundedOtherDebt= 0.00
    currentUnfundedDebtOtherPerTenth = (0)/10

    perTenthDebt = perSecondDebt/10
    today = int(time.time())
    elapsedSeconds=math.ceil((today-startdate)/1000)
    elapsedTenths=math.ceil((today-startdate)/100)

    currentDebt=(elapsedTenths*perTenthDebt)+baseDebt

    perTenthPop = perSecondPop/10
    elapsedSeconds=math.ceil((today-startPopdate)/1000)
    elapsedTenths=math.ceil((today-startPopdate)/100)
    currentPop=math.ceil((elapsedTenths*perTenthPop)+basePop)

    currentPersonDebt = currentDebt/currentPop
    currentHouseholdDebt = (currentPersonDebt * 2.59)

    currentUnfundedPersonDebt = currentUnfundedDebt/currentPop
    currentUnfHouseholdDebt = currentUnfundedPersonDebt * 2.59

    return currentDebt

class DebtCalc:

    def __init__(self):
      a = datetime.datetime.now().date()
      self.debt = calculateDebt(a.year,a.month,a.day,21599377345082.36,31610.2,2011,6,6,311496761,0.076923076923077) 