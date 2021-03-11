import sys, time

animation = r'\|/-\|/-'
for char in 'OPENING ATTENDANCE PROJECT...\n': 
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.2)

for i in range(20):
    time.sleep(0.2)
    sys.stdout.write('\r' + animation[i % len(animation)])
    sys.stdout.flush()

while True:
    teacher_name = input("\nEnter name of teacher: ")
    class_name = input('Enter class(standard and section): ')

    import datetime
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        hour_status='Good Morning!'
    elif hour>=12 and hour<18:
        hour_status='Good Afternoon!'    
    else:
        hour_status='Good Evening!'    
    print(f'\n{hour_status}')
    print(f'Teacher Name - {teacher_name}\nClass - {class_name}\nDate - {date}')

    check = input('\nIf the above data is correct press \'C\' for Correct; Else \'W\' for Wrong:\n> ').upper()
    if check == 'C':
        break
    
    elif check == 'W':
        continue

p_total = 0
a_total = 0

print("\nPress \'P\' for Present and \'A\' for Absent: ")

from names import names_list

atd_list=[]
atd_table = []

i = 0

while i < len(names_list):
    status = input(f"> {names_list[i]}: ").upper()
    if status != 'P' and status != 'A': 
        print('Invalid input!')
    else:
        if status == 'P':
            status = 'Present' 
            p_total += 1

        else:    
            status = 'Absent'
            a_total += 1

        atd_list.append(f'{names_list[i]} - {status}')
        atd_table.append(f'{names_list[i]} {" "*(9-len(names_list[i]))}|      {status}')
        i += 1
  
listToStr = '\n'.join([str(elem) for elem in atd_table]) 

while True:
    take_input = input("\nPress \'L\' to view Attendance List and \'T\' to view Attendance Table:\n> ").upper()
    if take_input == "L":
        print(f'\nAttendance List of {class_name} as on {date}:\n{atd_list}\n')
        break   

    elif take_input == 'T':   
        print(f'''-------------------------
Teacher Name - {teacher_name}
Class - {class_name}
Date - {date}\n
Name      |      Status\n
{listToStr}
-------------------------
''')
        break
    
press_enter = input('Press enter to view Attendance Summary')
print("\nAttendance Summary: ")
print(f"> Total Present - {p_total}\n> Total Absent - {a_total}")

print(f'\nThank You,\nHave a nice day {teacher_name}')

while True:
    quit = input("\nPress q to quit: ").upper()
    if quit == 'Q':
        for char in 'CLOSING ATTENDANCE PROJECT...\n': 
            print(char, end='') 
            sys.stdout.flush() 
            time.sleep(0.2)    
        
        for i in range(20):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        sys.exit()   

    else:
        print('Try again!')
        continue    


