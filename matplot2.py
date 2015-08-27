import matplotlib.pyplot as plt

#define plot size in inches (width, height) & resolution(DPI)
fig = plt.figure(figsize=(4, 5), dpi=100)

#define font size
plt.rc("font", size=14)

#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

#error data
y_error = [0.12, 0.13, 0.2, 0.1]

#plot data
plt.plot(x, y, linestyle="dashed", marker="o", color="green")

#plot only errorbars
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="green")

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

#title
plt.title("Simple plot")

#adjust plot
#plt.subplots_adjust(left=0.19)

#show plot
plt.show()