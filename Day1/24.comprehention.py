
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

leap_years = []
for y in years:
    if y % 4 == 0:
        leap_years.append(y)
print(leap_years)

leap_years = [ y for y in years if y % 4 == 0]
print(leap_years)