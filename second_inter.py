import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as stats
import random

df = pd.read_csv('population.csv')

population = df["Math_score"].tolist()

og_mean = stats.mean(population)
og_stdev = stats.stdev(population)

print(og_mean, og_stdev)



def random_sampling(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(population) - 1)
        value = population[random_index]
        dataset.append(value)
     
    mean = stats.mean(dataset)
    return mean

mean_list = []

for i in range(0,1000):
    mean_values = random_sampling(100)
    mean_list.append(mean_values)

sampling_stdev = stats.stdev(mean_list)
sampling_mean = stats.mean(mean_list)
print(sampling_mean, sampling_stdev)



fig = ff.create_distplot([mean_list],["Math Scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0,0.3], mode = "lines", name = "MEAN"))
#fig.show()

stdev1_start = sampling_mean - sampling_stdev
stdev1_end = sampling_mean + sampling_stdev

stdev2_start = sampling_mean - (2*sampling_stdev)
stdev2_end = sampling_mean + (2*sampling_stdev)

stdev3_start = sampling_mean - (3*sampling_stdev)
stdev3_end = sampling_mean + (3*sampling_stdev)

fig.add_trace(go.Scatter(x = [stdev1_start, stdev1_start], y = [0, 0.3], mode = 'lines', name = "Standard Deviation #1 Start"))
fig.add_trace(go.Scatter(x = [stdev1_end, stdev1_end], y = [0, 0.3], mode = 'lines', name = "Standard Deviation #1 End"))

fig.add_trace(go.Scatter(x = [stdev2_start, stdev2_start], y = [0, 0.3], mode = 'lines', name = "Standard Deviation #2 Start"))
fig.add_trace(go.Scatter(x = [stdev2_end, stdev2_end], y = [0, 0.3], mode = 'lines', name = "Standard Deviation #2 End"))

fig.add_trace(go.Scatter(x = [stdev3_start, stdev3_start], y = [0, 0.3], mode = 'lines', name = "Standard Deviation #3 Start"))
fig.add_trace(go.Scatter(x = [stdev3_end, stdev3_end], y = [0, 0.3], mode = 'lines', name = "Standard Deviation #3 End"))

#fig.show()



df2 = pd.read_csv("intervention_2.csv")

population2 = df2["Math_score"].tolist()

intervention2_mean = stats.mean(population2)

fig.add_trace(go.Scatter(x = [intervention2_mean, intervention2_mean], y = [0, 0.3], mode = "lines", name = "Intervention 2 Average"))

fig.show()

z_score = (intervention2_mean - sampling_mean) / sampling_stdev

print("Z SCORE: ", z_score)

# 3 - 2.2838409870295933 2 -  1.4664117981545948 1 - 0.4448270498980099