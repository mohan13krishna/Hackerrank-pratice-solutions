// author: mohan13krishna

from datetime import datetime

format = '%a %d %b %Y %H:%M:%S %z'

for _ in range(int(input())):
    time1 = datetime.strptime(input(), format)
    time2 = datetime.strptime(input(), format)

    print(int(abs((time1 - time2).total_seconds())))
