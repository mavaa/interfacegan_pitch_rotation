import math
import matplotlib.pyplot as plt
import numpy as np

# Load statistics for all estimated faces
faces = np.load("./data/all_face_angles.npy")
pitches_raw = faces[:, 0]
yaws_raw = faces[:, 1]
rolls_raw = faces[:, 2]

# Convert angles to degrees and sort them
pitches_angles_sorted = np.sort(np.degrees(pitches_raw))
yaws_angles_sorted = np.sort(np.degrees(yaws_raw))
rolls_angles_sorted = np.sort(np.degrees(rolls_raw))


##################
# Print minmax values for all axes
print("====Angle axes stats====")
def print_minmax(name, data):

    index_min = np.argmin(data)
    index_max = np.argmax(data)
    print(name)
    print("Min index: " + str(index_min))
    print("Max index: " + str(index_max))
    print("Degrees min: " + str(math.degrees(data[index_min])))
    print("Degrees max: " + str(math.degrees(data[index_max])))

print_minmax("Pitch", pitches_raw)
print_minmax("Yaw", yaws_raw)
print_minmax("Roll", rolls_raw)


##################
# Plot normal dist for all axes as bell curves (not used in paper)
def normal_dist(x, mean, sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

#Apply function to the data.
pdf_pitch = normal_dist(pitches_angles_sorted, np.mean(pitches_angles_sorted), np.std(pitches_angles_sorted))
pdf_yaw = normal_dist(yaws_angles_sorted, np.mean(yaws_angles_sorted), np.std(yaws_angles_sorted))
pdf_roll = normal_dist(rolls_angles_sorted, np.mean(rolls_angles_sorted), np.std(rolls_angles_sorted))

#Plotting the Results
plt.plot(pitches_angles_sorted, pdf_pitch, color='red')
plt.plot(yaws_angles_sorted, pdf_yaw, color='blue')
plt.plot(rolls_angles_sorted, pdf_roll, color='green')
plt.xlabel('Angle')
plt.ylabel('Probability Density')


##################
# Box plots for absolute pitch angles
def addBoxPlot(plotter, data, name):
    figbox, boxplot = plotter.subplots()
    boxplot.set_title(name)
    boxplot.boxplot(data, vert=False)
    return boxplot

# Separate absolute pitch angles
positive_pitches = pitches_angles_sorted[pitches_angles_sorted > 0]
negative_pitches = np.sort(np.abs(pitches_angles_sorted[pitches_angles_sorted < 0]))

pitch_box = addBoxPlot(plt, [positive_pitches, negative_pitches], "Absolute pitch angles")
pitch_box.set_xlabel('Angle')
pitch_box.set_yticklabels(["Positive", "Negative"])


##################
# Violin plot comparing all axes
vifil, filplot = plt.subplots()
axes = ("Pitch", "Yaw", "Roll")
plt.ylabel('Angle')
plt.title('Angle axes')
plt.xticks(np.arange(len(axes)) + 1, axes)
filplot.violinplot([pitches_angles_sorted, yaws_angles_sorted, rolls_angles_sorted], showmedians=True)


##################
# Angle counts by threshold
thresholds = (0, 5, 10, 15, 20)
positive_pitches_counts = [3498, 1181, 471, 185, 82]
negative_pitches_counts = [5017, 1995, 527, 139, 21]

barfig, barchart = plt.subplots()
index = np.arange(len(thresholds))
bar_width = 0.35
opacity = 0.8

rects_pos = plt.bar(index, positive_pitches_counts, bar_width,
                    alpha=opacity, color='g', label='Positive angle')

rects_neg = plt.bar(index+bar_width, negative_pitches_counts, bar_width,
                    alpha=opacity, color='r', label='Negative angle')

plt.xlabel('Threshold')
plt.ylabel('Number of samples')
plt.title('Samples kept by threshold')
plt.xticks(index + (bar_width/2), thresholds)
plt.legend()

plt.tight_layout()


##################
# Show all plots
plt.show()
