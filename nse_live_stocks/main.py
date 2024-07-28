import requests
import os
from datetime import datetime
from io import BytesIO
import  zipfile 
from pathlib import Path

class Nse():
    def __init__(self):
        self.url = "https://www.nseindia.com/api/quote-equity?symbol={}"
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        self.session.get('https://www.nseindia.com',
                         headers=self.headers, verify=True)
        self.response = None

    def get_current_price(self, symbol):
        self.response = self.session.get(self.url.format(symbol), headers=self.headers, verify=True)
        if self.response.status_code == 200:
            if self.response.json().get('message') != "TypeError: Cannot read property 'length' of undefined":
                return {"error":False,"nse_symbol":symbol,"current_value":str(self.response.json()['priceInfo']['lastPrice']) ,"date": self.response.json()['metadata']['lastUpdateTime']}
            return {"error":True,"message":"Stock Not Found/Invalid Input."}
        raise Exception(
                f"Not Found status code: {self.response.status_code}")

    def get_stock_info(self, symbol):
        self.response = self.session.get(self.url.format(symbol), headers=self.headers, verify=True)
        if self.response.status_code == 200:
            return self.response.json()
        raise Exception(
                f"Not Found status code: {self.response.status_code}")

    def download_nse_historical_data_csv(self,reqdate,fullpath=None):
        """ reqdate format is '07-28-2024 """
        try:
            date_object = datetime.strptime(reqdate, '%m-%d-%Y').date()
        except Exception as exec:
            raise Exception(exec)
        datastring = date_object.strftime('%d%b%Y')
        if  date_object > datetime.strptime('07-08-2024', '%m-%d-%Y').date():
            weburl = "https://www.nseindia.com/api/reports?archives=[{\"name\":\"CM-UDiFF Common Bhavcopy Final (zip)\",\"type\":\"daily-reports\",\"category\":\"capital-market\",\"section\":\"equities\"}]&date="+date_object.strftime('%d-%b-%Y')+"&type=equities&mode=single"
        else:
            stringdata = "{}/{}/cm{}bhav.csv.zip".format(date_object.strftime("%Y"),date_object.strftime("%b").upper(),datastring.upper())
            weburl = 'https://archives.nseindia.com/content/historical/EQUITIES/{}'.format(stringdata)
        try:
            resp = self.session.get(weburl,headers=self.headers,verify=True)
            zipdownload = zipfile.ZipFile(BytesIO(resp.content))
            if fullpath:
                zipdownload.extractall(fullpath)
                resp = {"error":False,"requesteddate":date_object.strftime('%m-%d-%Y'),"message":"File Downloaded to {}".format(fullpath)}
            else:
                zipdownload.extractall(str(Path.home())+"/Downloads")
                resp = {"error":False,"requesteddate":date_object.strftime('%m-%d-%Y'),"message":"File Downloaded to {}".format(str(Path.home())+"/Downloads")}
            return resp
        except Exception:
            return {"error":True,"requesteddate":date_object.strftime('%m-%d-%Y'),"message":"Please Provide valid trading date/invalid trading date format. \n sample format : %m-%d-%Y 07-24-2024"}

""" Developed by Akhil kodati https://github.com/akhilkodati """