import pandas as pd
import requests
import io

ChuquiCamata = requests.post(r"https://webservice.hobolink.com/restv2/data/custom/file", json={"authentication":{"password": "Chuquicamata2022@","token": "z33VfGRP4k","user": "Chuquicamata"},"query": "ChuquiCamata"})

ChuquiCamata =  ChuquiCamata.text.encode('ISO-8859-1')

ChuquiCamataPandas = pd.read_csv(io.StringIO( ChuquiCamata.decode('utf-8')), sep= "\t", index_col= 0, encoding= 'ISO-8859-1', low_memory= False)

EscribirChuquiCamata = ChuquiCamataPandas.to_csv( r"C:\Users\rey\Desktop\Mtec\ChuquiCamata.csv" )