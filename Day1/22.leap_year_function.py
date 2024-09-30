

def leap_years(start_year, stop_year):
    result = []
    for i in range(start_year, stop_year + 1):
        if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
            result.append(i)
    return result

print(leap_years(1999, 2024))

def leap_years(start_year, stop_year):
    return [ i for i in range(start_year, stop_year + 1) if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0)]

print(leap_years(1999, 2024))