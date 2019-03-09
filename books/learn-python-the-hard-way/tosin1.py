from sys import argv

script, tosin_file = argv

prompt = "Salary in %s: "

january = input(prompt% "January")
february = input(prompt% "February")
march = input(prompt% "March")
april = input(prompt% "April")
may = input(prompt% "May")
june = input(prompt% "June")
july = input(prompt% "July")
august = input(prompt% "August")
september = input(prompt% "September")
october = input(prompt% "October")
november = input(prompt% "November")
december = input(prompt% "December")

total = january + february + march + april + may + june + july + august + september + october + november + december

output = """
        \n\rMonth \t Amount
        \nJan   \t %r
        \nFeb   \t %r
        \nMar   \t %r
        \nApr   \t %r
        \nMay   \t %r
        \nJun   \t %r
        \nJul   \t %r
        \nAug   \t %r
        \nSep   \t %r
        \nOct   \t %r
        \nNov   \t %r
        \nDec   \t %r
        \n
        \nTotal \t %r
        """% (january, february, march, april, may, june, july, august, september, october, november, december, total)

open(tosin_file, 'w').write(output)
