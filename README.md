# NihongoSchoolCrawler
A Python tool that scrapes Japanese language school data from the  
[Association for the Promotion of Japanese Language Education (日本語教育振興協会)](https://www.nisshinkyo.org/) website  
and exports it to an Excel file. Useful for comparing student numbers, nationality ratios, and JLPT pass rates.

## 📦 Features
- Scrapes school data from the official Nisshinkyo website
- Extracts student counts, nationality distribution, and JLPT pass rates
- Outputs data to an Excel file (`.xlsx`)
- Includes archived data (`日本語言學校清單.xlsx`) for historical comparison

## 🚀 Output Sample
- Historical data from July 2, 2019: [日本語言學校清單_20190702.xlsx](https://github.com/setsu-shouka/NihongoSchoolCrawler/blob/main/NihongoSchoolCrawler/output/%E6%97%A5%E6%9C%AC%E8%AA%9E%E8%A8%80%E5%AD%B8%E6%A0%A1%E6%B8%85%E5%96%AE_20190702.xlsx)

## 🛠️ Tech Stack
- Python 3.7+
- `requests`
- `BeautifulSoup`
- `openpyxl`

## 📸 Screenshots (Output)
<img width="1919" height="697" alt="image" src="https://github.com/user-attachments/assets/7c28beb9-43bc-4d9c-b7dc-0c3e0436db01" />

## 📚 Background
This tool was created to collect and analyze data on Japanese language schools in Japan.  
It helps users compare institutions based on key metrics such as student demographics and JLPT success rates.  
The project includes an older dataset for reference and comparison.

## 📄 License
MIT License
