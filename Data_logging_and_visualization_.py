import random,time
import matplotlib.pyplot as plt
temps=[]
humidity=[]
time_values=[]
csv_file="environment_data.csv"
txt_file="environment_data.txt"
try:
    with open(csv_file,"a") as csv, open(txt_file,"a") as txt:
        csv.write("Time(s),Temperature(C),Humidity(%)\n")
        txt.write("Time(s)\tTemperature(C)\tHumidity(%)\n")
        for t in range(10):
            temp=25+random.uniform(-1,1)
            hum=60+random.uniform(-5,5)
            temps.append(temp)
            humidity.append(hum)
            time_values.append(t)
            csv.write(f"{t},{temp:.2f},{hum:.2f}\n")
            txt.write(f"{t}\t{temp:.2f}\t\t{hum:.2f}\n")
            time.sleep(0.5)
except IOError as e:
    print("File operation failed:",e)
plt.plot(time_values,temps,label="Temperature (°C)")
plt.plot(time_values,humidity,label="Humidity (%)")
plt.xlabel("Time (s)")
plt.ylabel("Values")
plt.title("Temperature and Humidity Log")
plt.legend()
plt.grid(True)
plt.show()
