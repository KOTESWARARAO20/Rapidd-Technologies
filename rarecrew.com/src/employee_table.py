import requests
import json
from datetime import datetime

url = 'https://rc-vault-fap-live-1.azurewebsites.net/api/gettimeentries?code=vO17RnE8vuzXzPJo5eaLLjXjmRW07law99QTD90zat9FfOQJKKUcgQ=='
response = requests.get(url)
data = json.loads(response.text)

for i in data:
    FMT = '%Y-%m-%dT%H:%M:%S'
    i['totalTimeWorked'] = (datetime.strptime(i['EndTimeUtc'], FMT) - datetime.strptime(i['StarTimeUtc'], FMT)).seconds;

data.sort(key=lambda x: x['totalTimeWorked'], reverse=True)

table_html = '<style>th{font-weight:bold}table, th, td {border: 1px solid black;border-collapse: collapse;</style><table><tr><th>Name</th><th>Total Time Worked</th></tr>'
for employee in data:
    if employee['totalTimeWorked'] < 1000:
        row_html = '<tr style="background:red; color:white"><td>{}</td><td>{}</td></tr>'.format(employee['EmployeeName'], employee['totalTimeWorked']);
    else:
        row_html = '<tr><td>{}</td><td>{}</td></tr>'.format(employee['EmployeeName'], employee['totalTimeWorked']);
    table_html += row_html
table_html += '</table>'

with open('employee_table.html', 'w') as f:
    f.write(table_html)