import xlwt
import xlrd
from datetime import datetime

wb = xlwt.Workbook()
ws = wb.add_sheet('Enlaces David',cell_overwrite_ok=True)
book = xlrd.open_workbook("sinOrdenar.xls")
sh = book.sheet_by_index(0)

mega = ""
putlocker = ""
mediafire = ""
freakshare = ""
uploaded = ""
hotfile = ""
letitbit = ""
netload = ""
jumbofiles = ""
glumbouploads = ""
dfiles = ""
zippyshare = ""
depositfiles = ""
error = ""

descargas = ["mega", "putlocker", "mediafire", "freakshare", "uploaded", "depositfiles", "zippyshare", "dfiles", "glumbouploads", "jumbofiles", "netload", "letitbit", "hotfile"]
for rx in range(sh.nrows):
    enlaces = sh.cell_value(rowx=rx, colx=2).split(', ')
    ws.write(rx, 0, sh.cell_value(rowx=rx, colx=0))

    for enlace in enlaces:
        if "mega" in enlace:
            mega += " " + enlace
        elif "putlocker" in enlace:
            putlocker += " " + enlace
        elif "mediafire" in enlace:
            mediafire += " " + enlace
        elif "freakshare" in enlace:
            freakshare += " " + enlace
        elif "uploaded" in enlace:
            uploaded += " " + enlace
        elif "depositfiles" in enlace:
            depositfiles += " " + enlace
        elif "zippyshare" in enlace:
            zippyshare += " " + enlace
        elif "dfiles" in enlace:
            dfiles += " " + enlace
        elif "glumbouploads" in enlace:
            glumbouploads += " " + enlace
        elif "jumbofiles" in enlace:
            jumbofiles += " " + enlace
        elif "netload" in enlace:
            netload += " " + enlace
        elif "letitbit" in enlace:
            letitbit += " " + enlace
        elif "hotfile" in enlace:
            hotfile += " " + enlace
        else:
            error = "ERROR!"

    ws.write(rx, 2, mega)
    ws.write(rx, 3, putlocker)
    ws.write(rx, 4, mediafire)
    ws.write(rx, 5, freakshare)
    ws.write(rx, 6, uploaded)
    ws.write(rx, 7, depositfiles)
    ws.write(rx, 8, zippyshare)
    ws.write(rx, 9, dfiles)
    ws.write(rx, 10, glumbouploads)
    ws.write(rx, 11, jumbofiles)
    ws.write(rx, 12, netload)
    ws.write(rx, 13, letitbit)
    ws.write(rx, 14, hotfile)
    ws.write(rx, 1, error)
    mega = ""
    putlocker = ""
    mediafire = ""
    freakshare = ""
    uploaded = ""
    hotfile = ""
    letitbit = ""
    netload = ""
    jumbofiles = ""
    glumbouploads = ""
    dfiles = ""
    zippyshare = ""
    depositfiles = ""
    error = ""

wb.save('ordenado.xls')
