import requests

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



""" Developed by Akhil kodati https://github.com/akhilkodati """