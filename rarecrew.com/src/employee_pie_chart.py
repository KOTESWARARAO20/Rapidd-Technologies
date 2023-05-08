
import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Make a GET request to retrieve the employee data
url = 'https://rc-vault-fap-live-1.azurewebsites.net/api/gettimeentries?code=vO17RnE8vuzXzPJo5eaLLjXjmRW07law99QTD90zat9FfOQJKKUcgQ=='
# url = 'https://google.com'
response = requests.get(url)
data = json.loads(response.text)
durations = [];
for i in data:
	FMT = '%Y-%m-%dT%H:%M:%S'
	durations.append((datetime.strptime(i['EndTimeUtc'], FMT) - datetime.strptime(i['StarTimeUtc'], FMT)).seconds)
percentages = [(i*100)/sum(durations) for i in durations]


labels = [employee['EmployeeName'] for employee in data]
plt.pie(percentages, labels=labels, autopct='%1.1f%%')
plt.title('Percentage of Total Time Worked by Employee')
plt.savefig('employee_pie_chart.png')
plt.show() # display the plot


####- current working directory

import os
print("\n checking")
print(os.getcwd())
