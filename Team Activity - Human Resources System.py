with open ("hr_system.txt") as file:
    for line in file:
        line = line.strip()

        infoList = line.split(" ")

        employeeId = int(infoList[1])
        employeeSalary = float(infoList[3]) / 24

        if infoList[2] == "Engineer":
            employeeSalary = employeeSalary + 1000

        print(f"{infoList[0]} (ID: {employeeId}), {infoList[2]} - ${employeeSalary:.2f}")