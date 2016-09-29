

# for 1 thru 9
# 91 times for 1 thru 9
# 10 times for 10 thru 19
# 100 times for 20,30,40 etc...
# 900 times for 'hundred'
# 891 times for 'and'
# 1 time for 'one thousand'

set1 = len('one' + 'two' + 'three' + 'four' + 'five' + 'six' + 'seven' + 'eight' + 'nine')
set2 = len('ten' + 'eleven' + 'twelve' + 'thirteen' + 'fourteen' + 'fifteen' + 'sixteen' + 'seventeen' + 'eighteen' + 'nineteen')
set3 = len('twenty' + 'thirty' + 'forty' + 'fifty' + 'sixty' + 'seventy' + 'eighty' + 'ninety')
set4 = len('hundred')
set5 = len('and')
set6 = len('one' + 'thousand')

sam = 91 * set1 + 10 * set2 + 100 * set3 + 900 * set4 + 891 * set5 + set6
print(set1 , set2 , set3 , set4 , set5 , set6)
print(sam)
