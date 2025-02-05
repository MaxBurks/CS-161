#Max Burks
#2/5/25
#importing needed lib
import psutil

#setting counter to 0
prc_num = 0
#iterating over each process
for prc in psutil.process_iter():
    #for each process, adding one to counter
    prc_num += 1
#printing total processes
print(f' Number of current processes: {prc_num}')