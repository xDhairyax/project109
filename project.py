import csv 
import statistics as st 
import pandas as pd 
import plotly.figure_factory as ff 

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()

fig=ff.create_distplot([df["reading score"].tolist()],["Score"],show_hist=False)
#fig.show()

mean=st.mean(data)
print(mean)

median=st.median(data)
print(median)

mode=st.mode(data)
print(mode)

standardDeviation=st.stdev(data)
print(standardDeviation)

sd1start,sd1end=mean-standardDeviation,mean+standardDeviation
sd2start,sd2end=mean-(2*standardDeviation),mean+(2*standardDeviation)
sd3start,sd3end=mean-(3*standardDeviation),mean+(3*standardDeviation)

listsd1=[r for r in data if r>sd1start and r<sd1end]
listsd2=[r for r in data if r>sd2start and r<sd2end]
listsd3=[r for r in data if r>sd3start and r<sd3end]

print("{}% of data lies in Standard Deviation 1".format(len(listsd1)*100.0/len(data)))
print("{}% of data lies in Standard Deviation 2".format(len(listsd2)*100.0/len(data)))
print("{}% of data lies in Standard Deviation 3".format(len(listsd3)*100.0/len(data)))