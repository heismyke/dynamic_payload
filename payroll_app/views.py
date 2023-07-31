from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    # suspended employess
    
    suspended = 9
    #date
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%b %Y")
    
    # payroll header
    payroll_header = [
        'Employee details',
        'Earnings',
        'Additions',
        'Deductions', 
    ]
    
    payroll_subheader = {
        'id': [],  
        'Names': [],
        'Basic salary': [],
        'Health insurance': [],
        'Total salary': [],
        'Total additions' : [],
        'Total deductions' : [],
        
    }
    
    payroll_subheader['id'] = [303940,493039,934030,534050,934030,534030,303940,493039,934030,534050,934030,534030]
    payroll_subheader['Names'] = ["Benjamin Thompson", "Emily Williams", "Michael Davis", "Sarah Johnson", "Matthew Brown","Kelvin Bawa","Benjamin Thompson", "Emily Williams", "Michael Davis", "Sarah Johnson", "Matthew Brown","Kelvin Bawa"]
    payroll_subheader['Basic salary'] = [10500, 9500,11400, 10600, 10530,8800,10500, 9500,11400, 10600, 10530,8800]
    payroll_subheader['Health insurance'] = [600,800,800,510,580,640,10500, 9500,11400, 10600, 10530,8800]
    
    payroll_subheader['Total additions'] = [1600,1150,2300,2700,1520,2050,10500, 9500,11400, 10600, 10530,8800]
    payroll_subheader['Total deductions'] = [1400, 1520, 1720, 1250, 3405,5055,10500, 9500,11400, 10600, 10530,8800]
    
    
    id = payroll_subheader['id']
    names = payroll_subheader['Names']
    basic_salaries = payroll_subheader['Basic salary']
    health_insurance = payroll_subheader['Health insurance']
    total_additions = payroll_subheader['Total additions']
    total_deductions =  payroll_subheader['Total deductions']
    
    total_salaries = []
    
    for i in range(len(basic_salaries)):
        total_salary = basic_salaries[i] + health_insurance[i]
        total_salaries.append(total_salary)
    
    
    payroll_subheader['Total salary'] = total_salaries
    
    total = payroll_subheader['Total salary']
    total_sum_total = sum(total)
   
    
    basic_total  = 0
    health_insurance_total = 0
    total_additions_sum = sum(total_additions)
    total_deductions_sum = sum(total_deductions)
   


    all_total = []
    for i in range(len(basic_salaries)):
        basic_total += basic_salaries[i]
        
    for x in range(len(health_insurance)):
        health_insurance_total += health_insurance[x]
    
        
    
    all_total.append(basic_total)
    all_total.append(health_insurance_total)
    all_total.append(total_sum_total)
    all_total.append(total_additions_sum)
    all_total.append(total_deductions_sum)
    
    final_sum = sum(all_total)
    context = {
        "payroll_header": payroll_header,
        "formatted_date": formatted_date,
        "suspended": suspended,
        "payroll_subheader": payroll_subheader,
        "id" : id,
        "names" : names,
        "basic_salaries" : basic_salaries,
        "health_insurance" : health_insurance,
        "total" : total,
        "total_additions" : total_additions,
        "total_deductions" : total_deductions,
        "all_total" : all_total,
        "final_sum" : final_sum
        
        }
    
    return render(request, 'home/index.html', context)
        