# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def extraer_links(browser, post):
    print ("-------------------------------------------------------")
    print ("Extrayendo links...")
    browser.get(post)
    browser.implicitly_wait(5)
    try:
        titulo = browser.find_element_by_xpath("//*[@id='main-content']/h1/a")
    except:
        titulo = "No disponible"
    enlaces = browser.find_elements_by_tag_name("a")
    enlace_final = ""
    print (titulo.text)
    #descargas = ["mega", "putlocker", "mediafire", "freakshare", "uploaded", "depositfiles", "zippyshare", "dfiles", "glumbouploads", "jumbofiles", "netload", "letitbit", "hotfile"]
    for enlace in enlaces:#MEGA-PUTLOCKER-MEDIAFIRE-FREAKSHARE-UPLOADED-DEPOSITFILES-ZIPPYSHARE-DFILES-GLUMBOUPLOADS-JUMBOFILES-NETLOAD-LETITBIT-HOTFILE
        if "mega" in str(enlace.get_attribute("href")) or "putlocker" in str(enlace.get_attribute("href")) or "mediafire" in str(enlace.get_attribute("href")) or "freakshare" in str(enlace.get_attribute("href")) or "uploaded" in str(enlace.get_attribute("href")) or "depositfiles" in str(enlace.get_attribute("href")) or "zippyshare" in str(enlace.get_attribute("href")) or "dfiles" in str(enlace.get_attribute("href")) or "glumbouploads" in str(enlace.get_attribute("href")) or "jumbofiles" in str(enlace.get_attribute("href")) or "netload" in str(enlace.get_attribute("href")) or "letitbit" in str(enlace.get_attribute("href")) or "hotfile" in str(enlace.get_attribute("href")):
            #titulos.append(titulo.text)
            '''print enlace.get_attribute("href")
            links.append(enlace.get_attribute("href"))'''
            if enlace_final == "":
                enlace_final += enlace.get_attribute("href")
            else:
                enlace_final += ", " + enlace.get_attribute("href")
    print (enlace_final)
    return post + "-----" + titulo.text + "-----" + enlace_final + "\n"

def main():
    print ("Logueando...")
    browser = webdriver.PhantomJS (service_args = ["--ignore-ssl-errors=true", "--ssl-protocol=any"])
    WebDriverWait (browser, 20)
    browser.get ("http://losjuegosdelcaldero.creaforo.net/login")
    browser.find_element_by_id ("username").send_keys ("AmazonHater")
    browser.find_element_by_id ("password").send_keys ("password123.")
    browser.find_element_by_name ("login").click()
    print ("Logueado!")

    fil = open("posts.txt", "r+")
    for linea in fil:
        if linea != "":
            gu = open("final.txt", "a")
            gu.write(extraer_links(browser, linea.replace("\n", "")))
            linea = ""
            gu.close()
    fil.close()

if __name__ == '__main__':
    main()
