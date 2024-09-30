
start_year = 1999
stop_year = 2222

# for i in range(start_year, stop_year + 1):
#     if i % 400 == 0:
#         print(i)
#     elif i % 4 == 0 and i % 100 != 0:
#         print(i) 

for i in range(start_year, stop_year + 1):
    if (i % 400 == 0) or (i % 4 == 0 and i % 100 != 0):
        print(i)