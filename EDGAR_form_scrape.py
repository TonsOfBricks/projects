"""
File: search_sort.py
Date: 07/03/2019
Author: Nikita Sinha
Description: Basic script for webscraping based on certain parameters.
"""

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from splinter import Browser
import urllib.request as ur
import webbrowser as wb
import requests
import re #I hate this library
import os

#Imported libraries include BeatifulSoup4, splinter
#Imported package from AUR: geckodriver (for selenium based browsers, including firefox)

page = ur.urlopen("https://searchwww.sec.gov/EDGARFSClient/").read() #Global expression for webpage used.
keyword = '"chief sustainability"' #Global expression for keyword to be used. Can be changed to any string. Keep the quotation marks for best results.
formType = "8-K" #Global Expression for formtype needed to be used. Can be changed to anystring that is supported by the website.
debug_inf = "chief sustainability"
body = {"search_text":keyword}
browser = Browser()

def search_alg():
    f1 = open("search.txt", "w+")
    counter = 0
    url = "https://searchwww.sec.gov/EDGARFSClient/" #Required for testing, debugging and working...
    browser.visit(url)
    browser.find_by_name("search_text").fill(keyword)
    browser.find_by_name('advancedSearch').click()
    browser.find_by_id('formType').select_by_text(formType)
    browser.find_by_name("numResults").select_by_text("100")
    browser.find_by_name("search").click()
    userin = str(input("Paste your generated url:"))
    page3 = requests.post(userin)
    while re.findall(debug_inf, page3.content.decode('utf-8')):
        counter += 1
        break
    print(counter, " <----- This is debug info") #Not required, mostly for debugging...
    web_raw = bs(page3.content, features='lxml')
    for a in web_raw.find_all('a', href=True):
        if a.has_attr('class') and 'filing' in a['class']:
            f1.write(str(a['href'])+"\n")

def data_fix():
    """
    This function was made poorly and was probabbly not required at all...
    """
    tempstr = ""
    fo = open("final.txt", "w+")
    with open("search.txt") as fil:
        for line in fil:
            urls = (re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)[0]) #Regex used for filtering the raw links
            sep = "'"
            tempstr = urls.split(sep, 1)[0]
            fo.write(tempstr+"\n")

def data_pull(): #This function could probabbly kill your computer... Specially if you use chrome(I would suggest using firefox). Exercise caution!
    """
    This function is designed to pull up the webpages yielded by the search that was made, in case the user finds that easier to read. 
    This function also preps the final document
    """
    res = open("result.txt", "w+")
    with open("final.txt", "r") as f2:
        for i in f2: #The variable i here is the link read from the file. 
            wb.open(i)
            res.write("=================================================" + "\n") #Used mainly for formatting
            res.write("Source for this information was taken from this link: " + i + "\n")
            html = urlopen(i)
            result_page = bs(html.read(), 'html.parser')
            for element in result_page.find_all('p'): #Leaves some empty paragraphs in results.txt but they can be ignored.
                res.write(str(element.getText()) + "\n")
            res.write("Over" + "\n") #Required only for formatting


def main(): #Main function that handles the working of the program.
    print("Based on the parameters you have a link will be generated and opened in a browser.")
    print("Copy the generated link and paste it in the console.")
    print("The program will open the websites and will also pull data from them and store it in a text file called result.txt")
    inp = str(input("enter any key as input to begin: "))
    search_alg()
    data_fix()
    data_pull()
    os.remove('search.txt') #Removes extra files

if __name__ == '__main__':
    main()

