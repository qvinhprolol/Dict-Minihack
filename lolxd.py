name = ['Huy','Tung','M.Duc']
role = ['Waiting','Cook','Manager']
hours = [12,24,20]
salary = [0.8,1.5,2]
Number1 = {
    "Name": name[0],
    "Role": role[0],
    "Hours": hours[0],
    "Salary per Hour": salary[0]
}

Number2 = {
    "Name": name[1],
    "Role": role[1],
    "Hours": hours[1],
    "Salary per Hour": salary[1]
}

Number3 = {
    "Name": name[2],
    "Role": role[2],
    "Hours": hours[2],
    "Salary per Hour": salary[2]
}

bangluong = [Number1, Number2, Number3]


Number4 = {
    "Name": 'Don',
    "Role": 'Waiter',
    "Hours": 12,
    "Salary per Hour": 0.9
}

for i in range(3):
    print('Name: ', bangluong[i]['Name'])
    print('Role: ', bangluong[i]['Role'])
    print('Hours: ', bangluong[i]['Hours'])
    print('Salary per Hour: ',bangluong[i]['Salary per Hour'])

bangluong[0]['Name']= 'Huyen'
bangluong[0]['Role']= 'Waitress'
bangluong[0]['Hours']= 14
bangluong[0]['Salary per Hour']= 1


print('')
budget = 0
for i in range(3):
    print('Name: ', bangluong[i]['Name'])
    print('Role: ', bangluong[i]['Role']) 
    luongthang = bangluong[i]['Hours'] * bangluong[i]['Salary per Hour']
    print('Monthly earnings: ', luongthang)
    budget = budget + luongthang
print('Budget: ',budget)




