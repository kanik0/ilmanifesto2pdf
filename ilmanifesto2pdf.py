#!/usr/bin/python3
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import urllib.parse as urlparse


def get_path(url):

    parsed = urlparse.urlparse(url)
    return parsed.path.replace('/','')

def get_code(url):

    parsed = urlparse.urlparse(url)
    return parsed.query[2:]

def link2pdf(url):

    req = Request('https://ilmanifesto.it/feed', headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(req).read().decode('utf-8')[:-1]
    root = ET.fromstring(webpage)

    links_raw = []
    ids_raw = []
    links = []
    ids = []

    for link in root.iter('link'):
        links_raw += [link.text]
    links_raw = links_raw[1:]
    for link in links_raw:
        links += [get_path(link)]

    for id in root.iter('guid'):
        ids_raw += [id.text]
    for id in ids_raw:
        ids += [get_code(id)]

    target = get_path(url)
    target_id = ids[links.index(target)]

    return 'https://ilmanifesto.it/read-offline/' + str(target_id) + '/' + target + '/pdf/'

print("##########################################")
print("#       il Manifesto to pdf - v0.1       #")
print("##########################################\n")
url = input("[*] Inserisci l'url completo: ")

print("[*] Cerco il link..")
url_pdf = link2pdf(url)

print("\n[*] Link al pdf: " + url_pdf + "\n")
