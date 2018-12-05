import csv
import matplotlib.pyplot as plt

categories = []
finland = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "FIN":
			finland.append([int(row[0]), row[5], row[6], row[7]]) # multidemensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]]) 
		line_count += 1

print('total medal for finland:', len(finland))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')


gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in finland: 
	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1924.append(medal)

	if medal[0] == 1948 and medal[3] == "Gold":
		gold_1948.append(medal)

	if medal[0] == 1972 and medal[3] == "Gold":
		gold_1972.append(medal)

	if medal[0] == 2002 and medal[3] == "Gold":
		gold_2002.append(medal)

	if medal[0] == 2014 and medal[3] == "Gold":
		gold_2014.append(medal)

print('finland won', len(gold_1924), 'gold medals in 1924')
print('finland', len(gold_1972), 'gold medals in 1972')
print('finland', len(gold_2014), 'gold medals in 2014')

totalMedals = len(gold_1924) + len(gold_1972) + len(gold_2014)

print('processed', line_count, 'rows of data')

gold_1924_percentage = int(len(gold_1924) / totalMedals * 100)
gold_1972_percentage = int(len(gold_1972) / totalMedals * 100)
gold_2014_percentage = int(len(gold_2014) / totalMedals * 100)

print(gold_1924_percentage, gold_1972_percentage, gold_2014_percentage)

print('processed', line_count, 'lines of data, Total medals:', totalMedals)

# do the pie chart / visualization
# 
labels = "Gold_1924", "Gold_1972", "Gold_2014"
sizes = [gold_1924_percentage, gold_1972_percentage, gold_2014_percentage]
colors = ['red', 'lightgreen', 'blue']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medal wins by Finland")
plt.xlabel("Medal Count Since 1924, 1972 & 2014")
plt.show()