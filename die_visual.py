from die import Die
import plotly.express as px

die = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die.num_sides + die2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "6 sided die results"
fig = px.bar(x=poss_results, y=frequencies, title=title)
fig.show()