class Date:
    def __init__(self):
        self.date = None
        self.valid_months = [
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
            "December",
        ]

    def valid_date(self, date):
        if "/" in date:
            m, d, y = map(int, date.split("/"))
            if 1 <= m <= 12 and 1 <= d <= 31:
                return [y, m, d]
        else:
            try:
                date = date.replace(",", "")
                m, d, y = date.split(" ")
                d, y = map(int, [d, y])
                if m in self.valid_months and 1 <= d <= 31:
                    m = self.valid_months.index(m) + 1
                    return [y, m, d]
            except:
                return None

    def get_date(self, loop=False):
        while True:
            try:
                input_date = input("Enter date: ").title().strip()
                if new_date := self.valid_date(input_date):
                    self.date = new_date
                    break
            except ValueError:
                print("Enter a valid date!")
            except TypeError:
                print("Not a valid date!")
            except EOFError:
                break
            if not loop:
                break

    def out_date(self, fmt = "ISO 8601"):
        y, m, d = self.date
        if fmt == "ISO 8601":
            print(f"{y}-{m:02}-{d:02}")


def main():
    date = Date()
    date.get_date()
    date.out_date(fmt = "ISO 8601")


main()

