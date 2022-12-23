import os


from prettytable import *

table = PrettyTable()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])

print(table)
print(table.bottom_junction_char * 51)

table1 = PrettyTable()
table1.add_column("City name", ["İstanbul", "Ankara", "İzmir", "Bursa"])
table1.add_column("Population",[20_000_000,10_000_000,5_000_000,3_000_000])


print(table1)
