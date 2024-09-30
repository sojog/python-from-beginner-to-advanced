import csv

with open("jokes.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['joke', 'category'])
    writer.writerow(['Chuck Norris...', 'China'])

with open("jokes.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)

