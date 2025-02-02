Import statistics
import matplot.lib.pyplot as plt

Exam1 = [.89, .93, .82, .95, .99]
Exam2 = [.77, .65, .60, .78, .77]
Exam3 = [.72, .88, .87, .86, .67]
Exam4 = [.84, .86, .91, .93, .95]

Exam1_Mean = statistics.mean(Exam1_Scores)
Exam2_Mean = statistics.mean(Exam2_Scores)
Exam3_Mean = statistics.mean(Exam3_Scores)
Exam4_Mean = statistics.mean(Exam4_Scores)

x = ["Exam 1", "Exam 2", "Exam 3", "Exam 4"]
y = [Exam1_Mean, Exam2_Mean, Exam3_Mean, Exam4_Mean]
plt.bar(x,y,label="Exam Average Score", color="blue")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bar")
plt.legend()
plt.show()
