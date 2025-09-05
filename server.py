from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Завантаження даних з employees.json
with open("employees.json", "r") as f:
    employees = json.load(f)

# Функція фільтрації
def filter_employees_by(field, month, department):
    filtered = []
    for emp in employees:
        if emp["department"].lower() != department.lower():
            continue

        # Витягуємо дату народження або найму
        date_str = emp[field]  # 'birthday' або 'hire_date'
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        if date_obj.strftime("%B").lower() == month.lower():
            filtered.append({
                "id": emp["id"],
                "name": emp["name"],
                field: date_obj.strftime("%b %d")  # Формат: "Apr 18"
            })

    return filtered

from flask import Flask, request, jsonify

# Ендпоінт для днів народження
@app.route("/birthdays", methods=["GET"])
def get_birthdays():
    month = request.args.get("month")
    department = request.args.get("department")

    if not month or not department:
        return jsonify({"error": "Missing parameters"}), 400

    results = filter_employees_by("birthday", month, department)
    return jsonify({
        "total": len(results),
        "employees": results
    })

# Ендпоінт для річниць найму
@app.route("/anniversaries", methods=["GET"])
def get_anniversaries():
    month = request.args.get("month")
    department = request.args.get("department")

    if not month or not department:
        return jsonify({"error": "Missing parameters"}), 400

    results = filter_employees_by("hire_date", month, department)
    return jsonify({
        "total": len(results),
        "employees": results
    })

if __name__ == "__main__":
    app.run(port=5000)