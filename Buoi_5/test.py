sodien=int(input("Nhập số kWh đã tiêu thụ:"))
if sodien <= 50 :
    sotien = sodien*1728
elif sodien > 50 and sodien<=100:
    sotien = sodien*1768
elif sodien >100 and sodien<=200 :
    sotien = sodien*2074
elif sodien > 200 and sodien <= 300 :
    sotien = sodien*2612
elif sodien > 300 and sodien<=400:
    sotien = sodien*2919
else:
    sotien = sodien*3015
print("Số tiền điện của bạn là:",sotien,"đồng")
