import statistics
import matplot.lib.pyplot as plt

GroupA_Scores = [.89, .93, .82, .95, .99]
GroupB_Scores = [.77, .65, .60, .78, .77]
GroupC_Scores = [.72, .88, .87, .86, .67]

GroupA_Mean = statistics.mean(GroupA_Scores)
GroupB_Mean = statistics.mean(GroupB_Scores)
GroupC_Mean = statistics.mean(GroupC_Scores)

x = ["GroupA", "GroupB", "GroupC"]
y = [GroupA_Mean, GroupB_Mean, GroupB_Mean]
plt.bar(x,y,label="Group Average Score", color="black")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bar")
plt.legend()
plt.show()
