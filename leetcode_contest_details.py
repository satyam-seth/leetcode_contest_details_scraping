import asyncio
from pyppeteer import launch

contests_details=[]

async def run():
    browser = await launch(headless=True , slowMo = 20, executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

    page = await browser.newPage()
    await page.goto('https://leetcode.com/contest/',{'timeout':0,'waitUntil':'domcontentloaded'})

    for i in range(9):
        data={}
        details=await page.evaluate(f"()=> document.getElementsByClassName('reactable-data')[0].children[{i}].innerText")
        details=details.split('\n')
        data['title']=details[0]
        data['date']=details[1]
        data['duration']=details[3]
        data['type']=details[4]
        contests_details.append(data)
asyncio.get_event_loop().run_until_complete(run())

print(contests_details)

"""
Output Sample-

[
    {'title': 'Weekly Contest 268', 'date': 'Nov 21, 2021 at 8:00 AM', 'duration': 'Virtual', 'type': '1 h 30 m'}, 

    {'title': 'Weekly Contest 267', 'date': 'Nov 14, 2021 at 8:00 AM', 'duration': 'Virtual', 'type': '1 h 30 m'}, 

    {'title': 'Biweekly Contest 65', 'date': 'Nov 13, 2021 at 8:00 PM', 'duration': 'Virtual', 'type': '1 h 30 m'}, 

    {'title': 'Weekly Contest 266', 'date': 'Nov 07, 2021 at 8:00 AM', 'duration': 'Virtual', 'type': '1 h 30 m'}, 

    {'title': 'Weekly Contest 265', 'date': 'Oct 31, 2021 at 8:00 AM', 'duration': 'Virtual', 'type': '1 h 30 m'}, 

    {'title': 'Biweekly Contest 64', 'date': 'Oct 30, 2021 at 8:00 PM', 'duration': 'Virtual', 'type': '1 h 30 m'}, 

    {'title': 'Weekly Contest 264', 'date': 'Oct 24, 2021 at 8:00 AM', 'duration': 'Virtual', 'type': '1 h 30 m'}, 

    {'title': 'Weekly Contest 263', 'date': 'Oct 17, 2021 at 8:00 AM', 'duration': 'Virtual', 'type': '1 h 30 m'}, 

    {'title': 'Biweekly Contest 63', 'date': 'Oct 16, 2021 at 8:00 PM', 'duration': 'Virtual', 'type': '1 h 30 m'}
]

"""