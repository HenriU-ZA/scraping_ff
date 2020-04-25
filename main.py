from bs4 import BeautifulSoup
import requests
from time import sleep
from random import randint

BASE_URL = "https://www.fantasticfiction.com"
# ==================================================================

# url = "/h/joe-hill/20th-century-ghosts.htm"
url = input(f"Please complete the URL for the first book by the author: {BASE_URL}")

author = url.split("/")[2]
author = author.split('-')
c_author = ''
for i in author:
    c_author =f"{c_author}{i[0].upper()}{i[1:]} "
str_len = len(c_author)
seperator = "="*str_len
# WRITE TO FILE..... ====================================
f2 = c_author.replace(" ","_")
filename= f"{f2}.txt"
with open(filename, "w", encoding='utf-8') as file:
    file.write("BOOKS BY:\n")
    file.write(f"{seperator}\n")
    file.write(f"{c_author}\n")
# =======================================================
test = 1
while url:
    r = requests.get(f"{BASE_URL}{url}")
    soup = BeautifulSoup(r.text, "html.parser")

    # GET The  Next URL... =======================================
    nxt_url = soup.findAll(class_="nb")
    # print(results)
    for item in nxt_url:
        try:
            url = item.find("a").attrs["href"]
            # print(f"NEXT URL = {next_url}")
        except AttributeError:
            url = None
    # ============================================================
    # BOOK NAME AND YEAR==========================================
    res_name = soup.find_all(class_="bookheading")
    # print(res_name)
    for name in res_name:
        book_name = name.find("h1").text
        book_year = name.find("a").text
        # print(f"Name of Book: {book_name} ({book_year})")
    # ============================================================
    # BOOK SYNOPSIS===============================================
    book_syn = soup.find(class_="blurb").text
    # print(book_syn)
    n_sep = int(len(book_name) + len(book_year) +4)
    f_sep = "="*n_sep
    # WRITE TO FILE..... ====================================
    with open(filename, "a", encoding='utf-8') as file:
        file.write(f"{f_sep}\n")
        file.write(f"BOOK NR:{test}\n")
        file.write(f"{book_name} - {book_year}\n")
        file.write(f"{f_sep}\n")
        file.write(f"{book_syn}\n")
    # =======================================================
    print(f"{test} books captured. Checking for more books... Please wait.")
    waiter = randint(1,3)
    sleep(waiter)
    test += 1
    # if test==3:
    #     break

