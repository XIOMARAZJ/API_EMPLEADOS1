import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'My User Agent 1.0',
})

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    # cantidad de empleados
    total_employees = len(data)
    print(f"CANTIDAD TOTAL DE EMPLEADOS : {total_employees}")

    # promedio de salario
    total_salary = sum(float(employee['employee_salary']) for employee in data['data'])
    average_salary = total_salary / total_employees
    print(f" PROMEDIO DEL SALARIO  : {average_salary}")

    # promedio de edad de los empleados
    total_age = sum(int(employee['employee_age']) for employee in data['data'])
    average_age = total_age / total_employees
    print(f"PROMEDIO DE LA EDAD DE LOS EMPLEADOS : {average_age}")

    # salario mínimo y máximo
    salaries = [float(employee['employee_salary']) for employee in data['data']]
    min_salary = min(salaries)
    max_salary = max(salaries)
    print(f"SALARIO MINIMO: {min_salary}")
    print(f"SALARIO BASICO: {max_salary}")


    # edad mínima y máxima
    ages = [int(employee['employee_age']) for employee in data['data']]
    min_age = min(ages)
    max_age = max(ages)
    print(f"EDAD MENOR: {min_age}")
    print(f"EDAD MAYOR: {max_age}")


else:
    print("Error al obtener los datos de empleados. Código de estado:"), response.status_code