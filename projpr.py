import PySimpleGUI as sg
from dbshka import *
import random

sg.theme('Black')
menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'E&xit'  ]],
            ['&Edit', ['Paste', ['Special', 'Normal'], 'Undo']],
            ['&Help', '&About...']]

layout1 = [[sg.Menu(menu_def)],
           [sg.Text('Possible activities', size=50, justification='c')],
           [sg.Button('Add Profile', button_color='#6c757d')],
           [sg.Button('Add Game', button_color='#6c757d')],
           [sg.Button('Add Studio', button_color='#6c757d')],
           [sg.Button('Check Profile', button_color='#6c757d')],
           [sg.Button('Exit')]]

window1 = sg.Window('Homepage', layout1, element_justification='c')

while True:
    event, values = window1.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add Profile':
        layout2 = [[sg.Text('Name', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Text('Surname', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Text('Phone', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Text('E-mail', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Button('Submit', button_color='#6c757d'), sg.Button('Cancel')]]

        window2 = sg.Window('Adding Profile', layout2)
        event, values = window2.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            window2.close()
        if event == 'Submit':
            mas = [values[0], values[1], values[2], values[3]]
            cur.execute(""" INSERT INTO Customers (name, surname, phone, email) VALUES (?, ?, ?, ?)""", mas)
            con.commit()
            sg.popup("Profile added!", title="Success")
            window2.close()
    if event == 'Add Game':
        layout3 = [[sg.Text('Name', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Text('Year', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Text('Price', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Button('Submit', button_color='#6c757d'), sg.Button('Cancel')]]

        window3 = sg.Window('Adding a Game', layout3)
        event, values = window3.read()

        if event == 'Cancel' or event == sg.WIN_CLOSED:
            window3.close()
        if event == 'Submit':
            mas = [values[0], values[1], values[2]]
            value2 = float(values[2])
            mas.append(round(value2*0.1))

            x = random.randint(1, 2)
            if x == 1:
                mas.append('yes')
            else:
                mas.append('no')

            cur.execute("""SELECT id_studio FROM Studios""")
            ids = cur.fetchall()
            mas.append(ids[len(ids)-1][0]+1)

            cur.execute(""" INSERT INTO Games (name, year, price, rent_price_d, accessib, id_studio) VALUES (?, ?, ?, ?, ?, ?)""", mas)
            con.commit()
            sg.popup("Game added!", title="Success")
            window3.close()

    if event == 'Add Studio':
        layout4 = [[sg.Text('Name', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Text('Country', size=10), sg.InputText(do_not_clear=False)],
                   [sg.Button('Submit', button_color='#6c757d'), sg.Button('Cancel')]]

        window4 = sg.Window('Adding a Studio', layout4)
        event, values = window4.read()

        if event == 'Cancel' or event == sg.WIN_CLOSED:
            window4.close()
        if event == 'Submit':
            mas = [values[0], values[1]]
            cur.execute(""" INSERT INTO Studios (name, country) VALUES (?, ?)""", mas)
            con.commit()
            sg.popup("Studio added!", title="Success")
            window4.close()

    if event == 'Check Profile':
        cur.execute("""SELECT name, surname, phone, email FROM Customers""")
        cust_info = cur.fetchall()
        prof = cust_info[len(cust_info)-1]
        layout5 = [[sg.Text('Name:', size=10), sg.Text(f'{prof[0]}', size=10)],
                   [sg.Text('Surname:', size=10), sg.Text(f'{prof[1]}', size=10)],
                   [sg.Text('Phone:', size=10), sg.Text(f'{prof[2]}', size=10)],
                   [sg.Text('E-mail:', size=10), sg.Text(f'{prof[3]}', size=10)],
                   [sg.Button('Ok')]]

        window5 = sg.Window('Information', layout5)
        event, values = window5.read()
        if event == 'Ok' or event == sg.WIN_CLOSED:
            window5.close()
