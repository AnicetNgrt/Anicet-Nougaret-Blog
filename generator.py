import os.path
from os import path

def build_date_text(array):
    date_text = ""
    day = array[0]
    month = array[1]
    year = array[2]
    if day != "":
        date_text += day+"/"
    if month != "":
        date_text += day+"/"
    if year != "":
        date_text += year_path(year)
    return date_text

def year_path(year):
    return f"../Timeline/{year}.md"

def is_date_empty(array):
    return array[0] == "" and array[1] == "" and array[2] == ""

print("MD PORTFOLIO FEEDER")
print("\n")

name = input("Name: ")

category = input("Category: ")

start_date = ["", "", ""]
next = next = input("Add a start date? [Y/n]: ")
if next == "Y":
    start_date_text = input("Start (dd/mm/yyyy): ")
    start_date = start_date_text.split("/")

end_date = ["", "", ""]
next = next = input("Add an end date? [Y/n]: ")
if next == "Y":
    end_date_text = input("End (dd/mm/yyyy): ")
    end_date = end_date_text.split("/")

techs = []
next = input("Add a tech? [Y/n]: ")
while(next == "Y"):
    next = input("Add a tech? [Y/n]: ")
    techs.append(input("Tech name: "))

status = input("Status: ")

links = []
next = input("Add a link? [Y/n]: ")
while(next == "Y"):
    links.append({
        "name":input("Link name: "),
        "address":input("Address: ")
    })
    next = input("Add a link? [Y/n]: ")

if not os.path.exists(f"./{category}"):
    os.mkdir(f"./{category}")

file = open(f"./{category}/{name}.md", "w+")
file.write(f"# {name}\n")
if category != "":
    file.write(f"*Category*: [{category}](./{category}.md)\n\n")
if not is_date_empty(start_date):
    file.write(f"*Start*: {build_date_text(start_date)}\n\n")
if not is_date_empty(end_date):
    file.write(f"*End*: {build_date_text(start_date)}\n\n")
if len(techs) > 0:
    file.write("*Techs*: ")
    for tech in techs:
        if not os.path.exists(f"../Techs/{tech}.md"):
            category_file = open(f"../Techs/{tech}.md", "w+")
            category_file.close()
        file.write(f"[{tech}](../Techs/{tech}.md) ")
    file.write("\n\n")
if status != "":
    file.write(f"*Status: {status}*\n\n")
if len(links) > 0:
    file.write("*Links*: ")
    for link in links:
        file.write(f"[{link.get('name')}]({link.get('address')}) ")
    file.write("\n\n")
file.write("---\n\n")
file.close()
    