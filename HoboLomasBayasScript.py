import pandas as pd
import requests
import io

LomasBayasHEAP = requests.post(r"https://webservice.hobolink.com/restv2/data/custom/file", json={"authentication":{"password": "Mtecingenieriaspa2022@","token": "z33VfGRP4k","user": "mtecingenieriaspa"},"query": "Lomas Bayas "})
LomasBayasROM = requests.post(r"https://webservice.hobolink.com/restv2/data/custom/file", json={"authentication":{"password": "Mtecingenieriaspa2022@","token": "z33VfGRP4k","user": "mtecingenieriaspa"},"query": "LobasBayasROM"})

LomasBayasHEAP =  LomasBayasHEAP.text.encode('ISO-8859-1')
LomasBayasROM =  LomasBayasROM.text.encode('ISO-8859-1')

LomasBayasHEAPPandas = pd.read_csv(io.StringIO( LomasBayasHEAP.decode('utf-8')), sep= "\t", index_col= 0, encoding= 'ISO-8859-1', low_memory= False)
LomasBayasROMPandas = pd.read_csv(io.StringIO( LomasBayasROM.decode('utf-8')), sep= "\t", index_col= 0, encoding= 'ISO-8859-1', low_memory= False)

EscribirLomasBayasHEAP = LomasBayasHEAPPandas.to_csv( r"C:\Users\rey\Desktop\Mtec\LomasBayasHEAP.csv" )
EscribirLomasBayasROM = LomasBayasROMPandas.to_csv( r"C:\Users\rey\Desktop\Mtec\LomasBayasROM.csv" )