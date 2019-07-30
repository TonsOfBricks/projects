from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium import webdriver
from splinter import Browser
import random as r
import time as t

browser = webdriver.Firefox()
#browser2 = Browser()
url = "https://spb.flamp.ru/addreview/5348553838509440?utm_source=widget&utm_medium=post_review&utm_campaign=responsive_widget&utm_content=flamp4"

def rekt(string_messg):
    browser.get(url)
    action = ac(browser)
    #element = browser.find_element_by_xpath("//input[@name='rating' and @value='1']")
    element = browser.find_element_by_xpath("//div[contains(@class, 'inputs-rating__value inputs-rating__value--1')]")
    action = ac(browser)
    action.move_to_element(element).click()
    action.move_by_offset(244, 244).click().perform()
    print(element.location_once_scrolled_into_view) #Debug Info
    browser.find_element_by_name("").send_keys(string_messg)
    element2 = browser.find_element_by_xpath("//div[contains(@class, 'button__label button__label js-button-label loader-holder__content')]")
    action.move_to_element(element2).click()
    print(element2.location_once_scrolled_into_view)
    action.move_by_offset(224, 652).click().perform()


def text_selector():
    list_rev = []
    with open("rev.txt") as f1:
        for line in f1:
            list_rev.append(line.strip())
    shit_to_give = r.choice(list_rev)
    return shit_to_give

def spam_gen():
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{};:',<.>/?fojewiofhjqhfrehgeriuwhgoewrhug"
    size = 100
    spam = "".join(r.sample(char_set, size))
    return spam


def main():
    lmao = text_selector()
    spam = spam_gen()
    if len(lmao) < 100:
        lmao = lmao + " Ловите спам, удачи убирать его " + spam
    rekt(lmao)

if __name__ == '__main__':
    main()
