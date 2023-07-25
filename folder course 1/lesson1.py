# 10003 khởi nghiep
money = 100
wage =5
number_of_days = 5
number_of_weeks = 4
# 1. Tính luong trong 1 thang
Salary = wage * number_of_days * number_of_weeks
money = money + Salary
print(money)
#b mỗi ngày tốn 2$ cho phí sh, sau thang dau con bao nhieu
subsistence_per_day =2
days_per_week = 7
subsistence = subsistence_per_day * days_per_week *number_of_weeks
money = money -subsistence
print(money)
weekend_wage = 7
weekend_day = 2
salary2 = number_of_weeks* (wage * number_of_days + weekend_wage*weekend_day)
print(salary2)
# C số tiền con lai sau 2 thang
money2 = money + salary2
subsistence2 = subsistence
money2 = money2 - subsistence2
print(money)
#cứ sau mỗi 2 tháng làm việc thì bạn được tăng 1$ tiền lương mỗi ngày, hỏi sau 6 tháng bạn có bao nhiêu tiền
TheFirst_every_2month = 30 * 1
Thesecond_every_2Month =30 * 2
TheThird_every_2Month =30 * 3
all_6_everymonth = TheFirst_every_2month + Thesecond_every_2Month + TheThird_every_2Month
print(all_6_everymonth)
bao_nhiêu = all_6_everymonth * money
print(bao_nhiêu)