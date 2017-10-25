# -*- coding: utf-8 -*-
import xlwt
from datetime import datetime

def main():

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet',cell_overwrite_ok=True)
    fil = open("final.txt", "r")
    iterador = 0
    for linea in fil:
        string = linea.replace("\n", "")
        partes = string.split('-----')
        ws.write(iterador, 0, partes[0])
        ws.write(iterador, 1, partes[1])
        ws.write(iterador, 2, partes[2])
        iterador += 1

    wb.save('sinOrdenar.xls')
    fil.close()

if __name__ == '__main__':
    main()
