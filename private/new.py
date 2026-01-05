valid_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def valid_date(date):
    if '/' in date:  
      m, d, y = map(int, date.split('/'))
      if 1 < m <= 12 and 1 < d <= 31:
         return [y, m, d]
    else:
      date = date.replace(',', '')
      m, d, y = date.split(' ')
      d, y = map(int, [d, y])
      if m in valid_months and 1 < d <= 31:
          m = valid_months.index(m) + 1
          return [y, m, d]


try:
    date = input("Enter date: ").capitalize().strip()
    if new_date := valid_date(date):
       y, m, d = new_date
       print(f"{y}-{m}-{d}")
       
except ValueError:
    pass
    
