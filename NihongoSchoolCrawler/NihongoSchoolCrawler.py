import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

title = ['地區', '學校名稱', '總學生數', '中文學生比例', '中國學生數', '台灣學生數',
         'N2合格率', 'N2應考人數', 'N2合格人數', 'N1合格率', 'N1應考人數', 'N1合格人數',
         'N3合格率', 'N3應考人數', 'N3合格人數', '網址']
ws.append(title)

url = 'https://www.nisshinkyo.org/search/area.php?lng=4'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

div_all_area = soup.find('div', id='areajapan')
li_all_area = div_all_area.find_all('li')
for li_single in li_all_area:
    a_single_area = li_single.find('a')
    text_single_area = a_single_area.text
    href_single_area = a_single_area.get('href')
    print(text_single_area)

    url_area = 'https://www.nisshinkyo.org/search/' + href_single_area
    r = requests.get(url_area)
    html = r.text
    soup_single_area = BeautifulSoup(html, 'html.parser')

    table_search_result = soup_single_area.find('table', class_='termsDetail')
    for tr_single_school in table_search_result.find_all('tr')[1:]:
        a_single_school = tr_single_school.find('th').find('a')
        href_single_school = a_single_school.get('href')

        url_school = 'https://www.nisshinkyo.org/search/' + href_single_school
        r = requests.get(url_school)
        html = r.text
        soup_single_school = BeautifulSoup(html, 'html.parser')

        # 學校名稱
        text_school_name = soup_single_school.find('p', class_='bsp10 center').text

        # 學生數、國籍比例
        table_student_count = soup_single_school.find_all('table', class_='tableStyle04')[1]
        td_China_student = table_student_count.select_one('td:contains("中國")')
        td_Taiwanese_student = table_student_count.select_one('td:contains("台灣")')
        td_total_student = table_student_count.select_one('span:contains("總計")').parent
        text_China_student = td_China_student.text.split('\n')[1].lstrip()
        text_Taiwanese_student = td_Taiwanese_student.text.split('\n')[1].lstrip()
        text_total_student = td_total_student.text.split('\n')[1].lstrip()
        try:
            Chinese_student_rate = (int(text_China_student) + int(text_Taiwanese_student)) / float(text_total_student)
            text_Chinese_student_rate = str(round(Chinese_student_rate * 100, 2)) + '%'
        except ZeroDivisionError:
            text_Chinese_student_rate = '0.0%'

        # N2合格率、應試人數
        table_N2 = soup_single_school.find('table', class_='tableStyle03')
        tr_take_test = table_N2.select_one('th:contains("應考者")').parent
        tr_pass_test = table_N2.select_one('th:contains("合格者")').parent
        text_N2_take_test = tr_take_test.find_all('td')[1].text
        text_N2_pass_test = tr_pass_test.find_all('td')[1].text
        try:
            text_N2_pass_rate = str(round((int(text_N2_pass_test) / int(text_N2_take_test)) * 100, 2)) + '%'
        except ZeroDivisionError:
            text_N2_pass_rate = '0.0%'
        text_N1_take_test = tr_take_test.find_all('td')[0].text
        text_N1_pass_test = tr_pass_test.find_all('td')[0].text
        try:
            text_N1_pass_rate = str(round((int(text_N1_pass_test) / int(text_N1_take_test)) * 100, 2)) + '%'
        except ZeroDivisionError:
            text_N1_pass_rate = '0.0%'
        text_N3_take_test = tr_take_test.find_all('td')[2].text
        text_N3_pass_test = tr_pass_test.find_all('td')[2].text
        try:
            text_N3_pass_rate = str(round((int(text_N3_pass_test) / int(text_N3_take_test)) * 100, 2)) + '%'
        except ZeroDivisionError:
            text_N3_pass_rate = '0.0%'

        # 結果
        print('學校名稱：' + text_school_name)
        print('總學生數：' + text_total_student)
        print('中文學生比例：' + text_Chinese_student_rate)
        print('中國學生數：' + text_China_student)
        print('台灣學生數：' + text_Taiwanese_student)
        print('N2合格率：' + text_N2_pass_rate)
        print('N2應考人數：' + text_N2_take_test)
        print('N2合格人數：' + text_N2_pass_test)
        print('N1合格率：' + text_N1_pass_rate)
        print('N1應考人數：' + text_N1_take_test)
        print('N1合格人數：' + text_N1_pass_test)
        print('N3合格率：' + text_N3_pass_rate)
        print('N3應考人數：' + text_N3_take_test)
        print('N3合格人數：' + text_N3_pass_test)
        print('網址：' + url_school)
        school_info = [text_single_area, text_school_name, int(text_total_student), text_Chinese_student_rate,
                       int(text_China_student), int(text_Taiwanese_student), text_N2_pass_rate, int(text_N2_take_test),
                       int(text_N2_pass_test), text_N1_pass_rate, int(text_N1_take_test), int(text_N1_pass_test),
                       text_N3_pass_rate, int(text_N3_take_test), int(text_N3_pass_test), url_school]
        ws.append(school_info)
        wb.save('日本語言學校清單.xlsx')
    print('----------------------------------------------------------')

wb.save('日本語言學校清單.xlsx')
