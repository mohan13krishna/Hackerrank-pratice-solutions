# author: mohan13krishna


# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/usr/bin/env python3

if __name__ == "__main__":
    string = input().strip()
    
    print(*sorted(string, key = lambda x: (-x.islower(), x.isdigit() - x.isupper(), x in '02468', x)), sep='')


