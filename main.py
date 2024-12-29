from flet import *
import sqlite3

conn = sqlite3.connect("dato.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stdname TEXT,
    stdmail TEXT,
    stdphone TEXT,
    stdaddress TEXT,
    stdkrain INTEGER,
    stdaslimeh INTEGER,
    stdarabic INTEGER,
    stdchemistry INTEGER,
    stdenglish INTEGER,
    stdalom INTEGER
)""")
conn.commit()

def main(page: Page):
    page.title = 'Nader'
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left = 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT

    tabe_name = 'student'
    query = f'SELECT COUNT(*) FROM {tabe_name}'
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]

    def add(e):
        cursor.execute("INSERT INTO student (stdname, stdmail, stdphone, stdaddress, stdkrain, stdaslimeh, stdarabic, stdchemistry, stdenglish, stdalom) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (tname.value, tmail.value, tphone.value, taddress.value, krain.value, aslimeh.value, arabic.value, chemistry.value, english.value, alom.value))
        conn.commit()
        print("طالب جديد مضاف")

    def show(e):
        page.clean()
        c = conn.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()

        if users:
            keys = ['id', 'stdname', 'stdmail', 'stdphone', 'stdaddress', 'stdkrain', 'stdaslimeh', 'stdarabic', 'stdchemistry', 'stdenglish', 'stdalom']
            result = [dict(zip(keys, values)) for values in users]
            for x in result:
                ##############العلامات#################
                m = x['stdkrain']
                a = x['stdaslimeh']
                f = x['stdarabic']
                h = x['stdchemistry']
                e = x['stdenglish']
                o = x['stdalom']
                total = m + a + f + h + e + o
                if total < 50:
                    status = Text('😢 راسب', size=19, color='white')
                else:
                    status = Text('🤩 ناجح', size=19, color='white')

                page.add(
                    Card(
                        color='black',
                        content=Container(
                            content=Column(
                                [
                                    ListTile(
                                        leading=Icon(icons.PERSON),
                                        title=Text('Name: ' + x['stdname'], color='black'),
                                        subtitle=Text('Student Email: ' + x['stdmail'], color='amber')
                                    ),
                                    Row([
                                        Text('Phone: ' + x['stdphone'], color='green'),
                                        Text('Address: ' + x['stdaddress'], color='green'),
                                    ], alignment=MainAxisAlignment.CENTER),
                                    Row([
                                        Text(':قرآن كريم ' + str(x['stdkrain']), color='blue'),
                                        Text(':إسلامية ' + str(x['stdaslimeh']), color='blue'),
                                        Text(':العربية ' + str(x['stdarabic']), color='blue'),
                                    ], alignment=MainAxisAlignment.END),
                                    Row([
                                        Text(':الرياضيات ' + str(x['stdchemistry']), color='blue'),
                                        Text(':إنجليزية ' + str(x['stdenglish']), color='blue'),
                                        Text(':العلوم ' + str(x['stdalom']), color='blue'),
                                    ], alignment=MainAxisAlignment.END),
                                    Row([
                                        status
                                    ], alignment=MainAxisAlignment.CENTER)
                                ]
                            )
                        )
                    )
                )
        page.update()

    ############حقول الادخال############
    tname = TextField(label='اسم الطالب', icon=icons.PERSON, rtl=True, height=38)
    tmail = TextField(label='البريد الإلكتروني', icon=icons.MAIL, rtl=True, height=38)
    tphone = TextField(label='رقم الهاتف', icon=icons.PHONE, rtl=True, height=38)
    taddress = TextField(label='العنوان أو السكن', icon=icons.LOCATION_CITY, rtl=True, height=38)
    ######################################
    #############علامات الطالب###########
    marktext = Text("علامات الطالب", text_align='center', width=110)
    krain = TextField(label='قرآن كريم', width=110, rtl=True, height=38)
    aslimeh = TextField(label='إسلامية', width=110, rtl=True, height=38)
    arabic = TextField(label='العربية', width=110, rtl=True, height=38)
    chemistry = TextField(label='الرياضيات', width=110, rtl=True, height=38)
    english = TextField(label='إنجليزية', width=110, rtl=True, height=38)
    alom = TextField(label='العلوم', width=110, rtl=True, height=38)
    ######################################

    addbuttn = ElevatedButton(
        "اضافه طالب جديد",
        width=170,
        style=ButtonStyle(bgcolor='blue', color='white', padding=15),
        on_click=add
    )

    showbuttn = ElevatedButton(
        "عرض كل الطلاب",
        width=170,
        style=ButtonStyle(bgcolor='blue', color='white', padding=15),
        on_click=show
    )

    page.add(
        Row(
            [
                Image(src="N_circle.png", width=280)
            ],
            alignment=MainAxisAlignment.CENTER
        ),
        Row(
            [
                Text("تطبيق الطالب والمعلم في جيبك", size=20, font_family="IBM Plex Sans Arabic", color='black'),
            ],
            alignment=MainAxisAlignment.CENTER
        ),
        Row(
            [
                Text("عدد الطلاب المسجلين:", size=20, font_family="IBM Plex Sans Arabic", color='blue'),
                Text(str(row_count), size=20, font_family="IBM Plex Sans Arabic", color='black'),
            ],
            alignment=MainAxisAlignment.CENTER, rtl=True
        ),
        tname,
        tphone,
        tmail,
        taddress,
        Row(
            [
                marktext
            ],
            alignment=MainAxisAlignment.CENTER, rtl=True
        ),
        Row(
            [
                krain,
                aslimeh,
                arabic,
            ],
            alignment=MainAxisAlignment.CENTER, rtl=True
        ),
        Row(
            [
                chemistry,
                english,
                alom
            ],
            alignment=MainAxisAlignment.CENTER, rtl=True
        ),
        Row(
            [
                addbuttn,
                showbuttn
            ],
            alignment=MainAxisAlignment.CENTER, rtl=True
        )
    )

    page.update()

app(main)
