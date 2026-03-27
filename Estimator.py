""" What This Code Does:
This code displays the welcome/introduction screen for your CNC Job Cost Calculator. 
It shows users what the program can do and what information they'll need to provide. """

print("            Program Functions\n            __________________\n")

print("1. Automate material cost calculation based on material type and weight\n"
    "2. Estimate machining labor hours based on complexity and quantity\n"
    "3. Apply business rules (bulk discounts, rush premiums, overhead allocation)\n"
    "4. Generate professional formatted quotes for customer communication\n"
    "5. Enable multi-part job quoting and running totals\n"
    "6. Save quotes to text files for archival and reporting\n"
    "7. Catalog projects")

print('You will be prompted to give the following information:'
    '1. Material type'
    '2. Part weight'
    '3. Order quantity'

    '4. Job complexity level'
    '5. Rush Job')

# component material 
"""What the code below does: 
This code handles the initial setup of a new job quote by getting the project name, displaying 
available materials, and validating the user's material selection with error handling. While 
also allowing the user to add any extra details they want to include in the quote."""

input('Ready? Hit Y then press enter: ')
project_name=input('Please enter a name for this project: ')
print ('Material selection list\nName\t\t\tFormal Code\n___________________________________\n'
    'Aluminum 6061\t\t6061-T6\n'
    'Aluminum 7050\t\t7075-T6\n'
    'Brass\t\t\tC36000\n'
    'Bronze\t\t\tC95400\n'
    'Copper\t\t\tC11000\n'
    'Magnesium\t\tAZ91D\n'
    'Mild Steel\t\t1018\n'
    'Low-Carbon Steel\t1020\n'
    'High-Carbon Steel\t1045\n'
    'Tool Steel\t\t01\n'
    'Cast Iron\t\tASTM A48\n'           
    'Stainless Steel 303\t303\n'
    'Stainless Steel 304\t304\n'
    'Stainless Steel 316\t316\n'
    'Stainless Steel 15-5\t15-5 PH\n'
    'Titanium\t\tTi-6AI-4V\n'
    'Inconel\t\t\tInconel 718\n')
materials=['6061-T6', '7075-T6', 'C36000', 'C95400', 'C11000', 'AZ91D', '1018', '1045', '303', '304', '316', '15-5 PH', 'Ti-6AI-4V', 'INCONEL 718', '1020', '01', 'ASTM A48']
project_material=input('Above is a list machinable materials, please enter a material formal code: ')
while project_material.upper() not in materials:
    print('Invalid material catalogued!')
    project_material=input('Above is a list machinable materials, please enter a material formal code: ')
print('Valid material catalogued.')
print(f'You selected: {project_material.upper()}')

extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
while extra_more.upper() not in ('Y', 'N'):
    print('Invalid input.')
    extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
if extra_more.upper() == 'N':
    extra_project_material = ''
    print('No extra details will be included.')
else:
    extra_project_material = input('What else would you like to add? ').strip()

while (user_confirm := input(f'You entered the following: "{extra_project_material}", is this correct? (Y/N) ')).upper() not in ('Y', 'N'):
    print('Invalid input.')

if user_confirm.upper() == 'N':
    extra_project_material = input('What details did you want attach? ')
    print(f'Updated details: {extra_project_material}')
else:
    print(f'Confirmed details: {extra_project_material}')

# Below is part weight 
"""What the code below does: 
This code collects the part weight of the project. While also allowing the user to add any extra details they want to include in the quote."""

project_weight=input('What is the weight of the single component, in pounds (lbs): ')
while True: 
    try:
        project_weight = float(project_weight) 
        break  
    except ValueError: 
        print('Invalid material weight entered!')
        project_weight = input('What is the weight of the single component, in pounds (lbs): ')
print('Valid material weight catalogued.')
print(f'You selected: {project_weight:.3f} lbs.')

extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
while extra_more.upper() not in ('Y', 'N'):
    print('Invalid input.')
    extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
if extra_more.upper() == 'N':
    extra_project_weight = ''
    print('No extra details will be included.')
else:
    extra_project_weight = input('What else would you like to add? ').strip()

while (user_confirm := input(f'You entered the following: "{extra_project_weight}", is this correct? (Y/N) ')).upper() not in ('Y', 'N'):
    print('Invalid input.')

if user_confirm.upper() == 'N':
    extra_project_weight = input('What details did you want attach? ')
    print(f'Updated details: {extra_project_weight}')
else:
    print(f'Confirmed details: {extra_project_weight}')

# component quantity 
"""What this code below does: 
This code collects the number of parts of the project. While also allowing the user to add any extra details they want to include in the quote."""

while True:
    try:
        project_quantity = int(input('How many components are you ordering? '))
        if project_quantity > 0:
            break
        else:
            print('Invalid component quantity! Must be greater than 0.')
    except ValueError:
        print('Invalid input! Please enter a whole number.')
print(f'Valid component quantity: {project_quantity}')

extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
while extra_more.upper() not in ('Y', 'N'):
    print('Invalid input.')
    extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
if extra_more.upper() == 'N':
    extra_project_quantity = ''
    print('No extra details will be included.')
else:
    extra_project_quantity = input('What else would you like to add? ').strip()

while (user_confirm := input(f'You entered the following: "{extra_project_quantity}", is this correct? (Y/N) ')).upper() not in ('Y', 'N'):
    print('Invalid input.')

if user_confirm.upper() == 'N':
    extra_project_quantity = input('What details did you want attach? ')
    print(f'Updated details: {extra_project_quantity}')
else:
    print(f'Confirmed details: {extra_project_quantity}')

# Job complexity level 
"""Collects the complexity of the project, ambiguous. While also allowing the user to add any extra details they want to include in the quote."""

project_complexity = input('On a scale from 1 to 10, please enter the level of complexity for this project: ')
while True:
    try:
        complexity_value = int(project_complexity)
        if complexity_value < 1 or complexity_value > 10:
            print('Your answer is invalid (must be 1-10)!')
            project_complexity = input('On a scale from 1 to 10, please enter the level of complexity for this project: ')
        else:
            break  # Valid answer, exit loop
    except:
        print('Your answer is invalid (must be a number)!')
        project_complexity = input('On a scale from 1 to 10, please enter the level of complexity for this project: ')

print('Valid project level complexity!')
print(f'Project complexity level: {complexity_value}')

extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
while extra_more.upper() not in ('Y', 'N'):
    print('Invalid input.')
    extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
if extra_more.upper() == 'N':
    extra_project_complexity = ''
    print('No extra details will be included.')
else:
    extra_project_complexity = input('What else would you like to add? ').strip()

while (user_confirm := input(f'You entered the following: "{extra_project_complexity}", is this correct? (Y/N) ')).upper() not in ('Y', 'N'):
    print('Invalid input.')

if user_confirm.upper() == 'N':
    extra_project_complexity=input('What details did you want attach? ')
    print(f'Updated details: {extra_project_complexity}')
else:
    print(f'Confirmed details: {extra_project_complexity}')

#Rush Order? 
"""Collects whether the project is a rush order, ambiguous. While also allowing the user to add any extra details they want to include in the quote."""

rush_order=input('Is this a rushed order? (Y/N) ')
while rush_order.upper() != 'Y' and rush_order.upper() != 'N':
    print('Invalid input.')
    rush_order = input('Is this a rushed order? (Y/N) ')
print(f'Valid Input: {rush_order.upper()}')

extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
while extra_more.upper() not in ('Y', 'N'):
    print('Invalid input.')
    extra_more = input('Are there any more details you would like to include? (Y/N) ').strip()
if extra_more.upper() == 'N':
    extra_project_rush = ''
    print('No extra details will be included.')
else:
    extra_project_rush = input('What else would you like to add? ').strip()

while (user_confirm := input(f'You entered the following: "{extra_project_rush}", is this correct? (Y/N) ')).upper() not in ('Y', 'N'):
    print('Invalid input.')

if user_confirm.upper() == 'N':
    extra_project_rush = input('What details did you want attach? ')
    print(f'Updated details: {extra_project_rush}')
else:
    print(f'Confirmed details: {extra_project_rush}')

# Final table 
print('All information has been collected for this project, now generating a summary table of the information you provided and any extra details you attached to the quote.')
print('\n\tProject Summary\n\tCategory\tValue\tExtra Information\n___________________________________________________\n')
print(f'Project Name: \t{project_name}\t')
print(f'Project Material: \t{project_material}\t Extra details: {extra_project_material}\n')
print(f'Project Weight: \t{project_weight}(lbs)\t Extra details: {extra_project_weight}\n')
print(f'Project Quantity: \t{project_quantity}\t Extra details: {extra_project_quantity}\n')
print(f'Project Complexity: \t{complexity_value}\t Extra details: {extra_project_complexity}\n')
print(f'Is this a Rush Order? (Y/N): \t{rush_order}\t Extra details: {extra_project_rush}\n')































































































































































