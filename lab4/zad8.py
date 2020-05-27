import pandas as pd
from pandas import read_csv
import os


table = read_csv(os.path.join(os.getcwd(), "countries.csv"),";")

#print(table.nlargest(10,['area'])) # 10 самых маленьких и самых больших стран мира по территории; +
#print(table.nsmallest(10,['ccn3'])) #10 самых маленьких и самых больших стран мира по населению; +
#print(table[table.languages=='French'][['languages','area', 'name']]) #все франкоязычные страны мира; +
#print(table.where(table.borders.isnull()).name.dropna()) #только островные государства; +
'''
print(table.where(pd.Series(
    [float(str(d).split(',')[0]) < 0 for d in table.latlng])
).name.dropna() )#все страны, находящиеся в южном полушарии.+
'''

"""" Групировка по первой букве
for i, group in table.groupby([d[0] for d in table.name]):
    print(i + ': ')
    for i, name in enumerate(group.name, 1):
        print(str(i) + '.', name.split(',')[0])
"""

names = pd.Series([d.split(',')[0] for d in table.name])
names.name = 'name'
lat, lng = zip(*[d.split(',')
                 if isinstance(d, str)
                 else ['nan', 'nan']
                 for d in table.latlng])
lat, lng = map(pd.Series, (lat, lng))
lat.name = 'latitude'
lng.name = 'longitude'
for_export = pd.concat([names,
                        table[['capital', 'area','ccn3' ,'currency']],
                        lat, lng], axis=1)
with pd.ExcelWriter('exported.xls') as excel_writer:
    for_export.to_excel(excel_writer)

#Complete
