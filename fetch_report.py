import sys
import requests

# Перевірка аргументів командного рядка
if len(sys.argv) != 3:
    print("Usage: python fetch_report.py <month> <department>")
    sys.exit(1)

month = sys.argv[1]
department = sys.argv[2]

# Формування URL до API
url = f"http://127.0.0.1:5000/birthdays?month={month}&department={department}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching report: {e}")
    sys.exit(1)

# Вивід результатів
print(f"Report for {department} department for {month.capitalize()} fetched.")
print(f"Total: {data['total']}")
print("Employees:")
for emp in data["employees"]:
    name = emp["name"]
    birthday = emp["birthday"]
    print(f"- {birthday}, {name}")