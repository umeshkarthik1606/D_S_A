attendence = {}
def show_menu():
    print('Attendence Tracker')
    print('1. Add attendence')
    print('2. veiw Attendence')
    print('3. Exit')
def add_attendence():
    name = input('Enter Student name: ')
    status = input('Enter status (Present/Absent): ')
    attendence[name] = status
    print('Attendence added successfully')
def view_attendence():
    if not attendence:
        print('NO attendence record found')
    else:
        print('----------Attendence Recorded-----------')
        for name, status in attendence.items():
            print(f'{name} - {status}')
def main():
    while True:
        show_menu()
        choice = input('Enter your choises: ')
        if choice == '1':
            add_attendence()
        elif choice == '2':
            view_attendence()        
        elif choice == '3':
            print('Exiting program')
            break
        else:
            print('Invalid choice')
main()