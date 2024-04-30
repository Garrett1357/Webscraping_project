
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font


# Creates workbook and sheet
workbook = xl.Workbook()
sheet = workbook.active
sheet.title = 'BoxOfficeReport'

# Define and append headers
headers = ['No.','Movie TItle','Release Date','Number of Theaters','Total Gross','Average Gross by Theater']
sheet.append(headers)


#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2024/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

table_rows = soup.findAll("tr")

for row in table_rows[1:6]:
    td = row.findAll("td")
    number = td[0].text
    title = td[1].text
    release = td[8].text
    Number_of_theaters = float(td[6].text.replace(",",""))
    Total_gross = float(td[7].text.replace(",","").strip("$"))
    Avg_gross_theater = Total_gross / Number_of_theaters


    #print(number)
    #print(title)
    #print(release)
    #print(Number_of_theaters)
    #print(Total_gross)
    #print(Avg_gross_theater)

    data = [number, title, release, Number_of_theaters, Total_gross, Avg_gross_theater]
    sheet.append(data)

for col in ['D', 'E', 'F']:  #formats the columns 
    for cell in sheet[col]:
        if col == 'D':
            cell.number_format = '#,##0'
        elif col == 'E' or col == 'F':
            cell.number_format = '"$ "#,##0.00'

for column_cells in sheet.columns: #Sets width to be the size of the cell 
    length = max(len(str(cell.value)) for cell in column_cells) #Doesnt work with Total Gross yet
    sheet.column_dimensions[column_cells[0].column_letter].width = (length+5)

#Bolds Header Cells
sheet['A1'].font = Font(name='Calibri',size=12,italic=False,bold=True)
sheet['B1'].font = Font(name='Calibri',size=12,italic=False,bold=True)
sheet['C1'].font = Font(name='Calibri',size=12,italic=False,bold=True)
sheet['D1'].font = Font(name='Calibri',size=12,italic=False,bold=True)
sheet['E1'].font = Font(name='Calibri',size=12,italic=False,bold=True)
sheet['F1'].font = Font(name='Calibri',size=12,italic=False,bold=True)


# Save workbook
workbook.save('BoxOfficeReport.xlsx')




# Requirements
## Number
## Movie Title
## Release Date
## Number of Theaters
## Total Gross
## Average Gross by Theater

#add to excel file called BoxOfficeReport.xlsx

