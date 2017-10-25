# -*- coding: utf-8 -*-
import urllib
from lxml import html
import requests
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def sacar_posts(pagina):
    page = html.fromstring(urllib.request.urlopen(pagina).read()) #PYTHON 3
    #page = html.fromstring(urllib.urlopen(pagina).read()) #PYTHON 2
    lista = ""
    for link in page.xpath("//li//dl//dd//div//div//h2//a"):
        dominio = "http://losjuegosdelcaldero.creaforo.net/" + str(link.get("href"))
        if "Normas Internas"not in link.text:
            lista = lista + dominio + "\n"
    return lista

def sacar_paginas_categoria(categoria):
    paginas = [categoria]
    page = html.fromstring(urllib.request.urlopen(categoria).read()) #PYTHON 3
    #page = html.fromstring(urllib.urlopen(categoria).read())

    for pag in page.xpath("//*[@id=\"main-content\"]/div[3]/span/a"):
        if "http://losjuegosdelcaldero.creaforo.net/" + str(pag.get("href")) not in paginas:
            paginas.append("http://losjuegosdelcaldero.creaforo.net/" + str(pag.get("href")))

    posts = ""
    for p in paginas:
        posts = posts +sacar_posts(p)
    return posts

def main():
    print ("Logueando...")
    browser = webdriver.PhantomJS (service_args = ["--ignore-ssl-errors=true", "--ssl-protocol=any"])
    wait = WebDriverWait (browser, 20)
    browser.get ("http://losjuegosdelcaldero.creaforo.net/login")
    browser.find_element_by_id ("username").send_keys ("AmazonHater")
    browser.find_element_by_id ("password").send_keys ("password123.")
    browser.find_element_by_name ("login").click()
    print ("Logueado!")
    #browser.save_screenshot ("bla.png")

    categorias = ["http://losjuegosdelcaldero.creaforo.net/f40-novedades", "http://losjuegosdelcaldero.creaforo.net/f41-objetos-ocultos", "http://losjuegosdelcaldero.creaforo.net/f43-match-3", "http://losjuegosdelcaldero.creaforo.net/f77-accion-y-arcade", "http://losjuegosdelcaldero.creaforo.net/f42-gestion-de-tiempo", "http://losjuegosdelcaldero.creaforo.net/f45-cartas-y-tableros", "http://losjuegosdelcaldero.creaforo.net/f62-puzzles", "http://losjuegosdelcaldero.creaforo.net/f44-aventura-y-gran-aventura", "http://losjuegosdelcaldero.creaforo.net/f88-infantiles-y-educativos"]
    #categorias = ["http://losjuegosdelcaldero.creaforo.net/f40-novedades"]

    
    posts = ""
    for cat in categorias:
        posts = posts + sacar_paginas_categoria(cat)
    f = open("posts.txt", "w")
    f.write(posts)
    f.close()

if __name__ == '__main__':
    main()
