import requests
from time import sleep
from lxml import html
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

categories = [
    "ANTH ",
    "ART  ",
    "ASAM ",
    "BMSE ",
    "BLKST",
    "CNENG",
    "CHEM ",
    "CHST ",
    "CLASS",
    "L&amp;S  ",
    "COMM ",
    "CLIT ",
    "CMPSC",
    "CNCSP",
    "CRSTU",
    "DA   ",
    "DYNS ",
    "ERTSC",
    "EALCS",
    "EEMB ",
    "ECON ",
    "EDUC ",
    "ECE  ",
    "ENGSC",
    "ENGL ",
    "ESM  ",
    "ENVST",
    "ESS  ",
    "FEMST",
    "FLMST",
    "FR&amp;IT",
    "GEOG ",
    "GERSL",
    "GLOBL",
    "GRDIV",
    "HIST ",
    "ARTHI",
    "INT  ",
    "LAIS ",
    "LAWSO",
    "LING ",
    "MARSC",
    "MATRL",
    "MATH ",
    "ME   ",
    "MAT  ",
    "MDVST",
    "MILSC",
    "MCDB ",
    "MUSIC",
    "NO   ",
    "PHIL ",
    "PHYS ",
    "POLS ",
    "PSY  ",
    "RELST",
    "RENST",
    "SOC  ",
    "SP&amp;PT",
    "SPCH ",
    "STATS",
    "TMP  ",
    "THTDA",
    "WRIT "
]

viewstates = open("viewstate.dat", "r").readlines()
login_vs = viewstates[0].strip()
find_vs = viewstates[1].strip()
credentials = open("credentials.dat", "r").readlines()
username = credentials[0].strip()
password = credentials[1].strip()
login = {
    "__LASTFOCUS":"",
    "__VIEWSTATE":login_vs,
    "__VIEWSTATEGENERATOR":"00732C32",
    "__EVENTTARGET":"",
    "__EVENTARGUMENT":"",
    "__EVENTVALIDATION":"/wEdAAdbKm4OU/lsarSPEWzw3woTFPojxflIGl2QR/+/4M+LrK6wLDfR+5jffPpLqn7oL3ttZruIm/YRHYjEOQyILgzL2Nu6XIik3f0iXq7Wqnb39/ZNiE/A9ySfq7gBhQx160NmmrEFpfb3YUvL+k7EbVnKgIKH2XlDUw30P837MyfVDMpYxIk=",
    "ctl00$pageContent$userNameText":username,
    "ctl00$pageContent$passwordText":password,
    "ctl00$pageContent$loginButton":"Login",
    "ctl00$pageContent$PermPinLogin$userNameText":"",
    "ctl00$pageContent$PermPinLogin$passwordText":""
}

find = {
    "__EVENTTARGET":"",
    "__EVENTARGUMENT":"",
    "__LASTFOCUS":"",
    "__VIEWSTATE":find_vs,
    "__VIEWSTATEGENERATOR":"B22B3C44",
    "ctl00$pageContent$quarterDropDown":"20194",
    "ctl00$pageContent$departmentDropDown":categories[0],
    "ctl00$pageContent$subjectAreaDropDown":"",
    "ctl00$pageContent$courseNumberTextBox":"",
    "ctl00$pageContent$courseLevelDropDown":"",
    "ctl00$pageContent$startTimeFromDropDown":"",
    "ctl00$pageContent$startTimeToDropDown":"",
    "ctl00$pageContent$daysCheckBoxList$0":"M",
    "ctl00$pageContent$daysCheckBoxList$1":"T",
    "ctl00$pageContent$daysCheckBoxList$2":"W",
    "ctl00$pageContent$daysCheckBoxList$3":"R",
    "ctl00$pageContent$daysCheckBoxList$4":"F",
    "ctl00$pageContent$daysCheckBoxList$5":"S",
    "ctl00$pageContent$daysCheckBoxList$6":"U",
    "ctl00$pageContent$unitsFromDropDown":"0",
    "ctl00$pageContent$unitsToDropDown":"12",
    "ctl00$pageContent$enrollcodeTextBox":"",
    "ctl00$pageContent$instructorTextBox":"",
    "ctl00$pageContent$keywordTextBox":"",
    "ctl00$pageContent$GECollegeDropDown":"",
    "ctl00$pageContent$GECodeDropDown":"",
    "ctl00$pageContent$searchButton":"Begin+Search",
}
login_url = "https://my.sa.ucsb.edu/gold/Login.aspx"
find_url = "https://my.sa.ucsb.edu/gold/CriteriaFindCourses.aspx"
scrape_url = "https://my.sa.ucsb.edu/gold/ResultsFindCourses.aspx"
home_url = "https://my.sa.ucsb.edu/gold/Home.aspx"
session = requests.session()
session.post(url=login_url, data=login)
for category in categories:
     c = True
     while c == True:
        try:
             c = False
             find["ctl00$pageContent$departmentDropDown"] = category
             session.post(url=find_url, data=find, headers=header)
             depts = session.get(url=find_url, data=find, headers=header)
             url = session.get(url=scrape_url, headers=header)
             print("Downloaded {}".format(category.lower().strip()))
             open("pages/{}.html".format(category.strip().lower()), "w").write(url.content.decode("utf-8"))
        except requests.exceptions.ConnectionError:
            c = True
            sleep(5)
