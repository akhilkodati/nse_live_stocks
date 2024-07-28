## nse_live_stocks

Python library for extracting realtime stock data from National Stock Exchange (India) .

#### Introduction.

nselivestocks library is to collect the real time stock information just by giving the nse symbol. This library data accuracy is completely depends upon www.nseindia.com.

### Features 
##### Get the Nse stock live price 
##### Get the nse stock information 
##### Download historical Data (from v0.8)

#### Package link  

**https://pypi.org/project/nse-live-stocks/**

#### Command to install 

**pip install nse-live-stocks**

------------------------------------------------------------------------------------
**i) Get live price of any nse stock**
####
from nse_live_stocks import Nse
####
stock = Nse()
###
result = stock.get_current_price('TCS')
####
print(result)
###
Output:
###
{'error': False, 'nse_symbol': 'TCS', 'current_value': '4393.65', 'date': '26-Jul-2024 09:07:13'}
###
------------------------------------------------------------------------------------
**ii) Download the Historical data from nseindia.**
###
name:  CM-UDiFF Common Bhavcopy Final (zip) | cm bhav csv (zip)
###
Type: daily-reports
###
Category: capital-market
###
Sector: equities
###
Inputs:
###
1) Date - you want to download the historical data.
 **format is '%m-%d-%Y'**
###
2) Fullpath - Full path to download the historical data file 
### 
Example in my case path is '/Users/akhilkodati/Music/myworks/'
###
default path is Downloads folder in Home directory.
######
from nse_live_stocks import Nse
###
stock = Nse() 
###
To Download historical file in Default directory.
###
result = stock.download_nse_historical_data_csv('06-26-2024')
###
Output:
###
{'error': False, 'requesteddate': '06-26-2024', 'message': 'File Downloaded to /Users/akhilkodati/Downloads/'}
###
To Download historical file in custom directory 
###
result = stock.download_nse_historical_data_csv('06-26-2024','/Users/akhilkodati/Music/myworks/')
###
print(result)
###
Output: 
###
{'error': False, 'requesteddate': '06-26-2024', 'message': 'File Downloaded to /Users/akhilkodati/Music/myworks/'}
###
**Tested from 01-01-2016.(You can download historical data from 01-01-2016)**
**If requesteddate before 08/July/2024 it downloads the cm bhav csv(zip) file else it downloads the CM-UDiFF Common Bhavcopy Final (zip)**
###
------------------------------------------------------------------------------------
**iii) Get Complete information of any nse stock**
###
from nse_live_stocks import Nse
###
stock = Nse() 
###
result = stock.get_stock_info('ABB')
###
print(result)
###
Output:
###
{'info': {'symbol': 'ABB', 'companyName': 'ABB India Limited', 'industry': 'ELECTRICAL EQUIPMENT', 'activeSeries': ['EQ'], 'debtSeries': [], 'isFNOSec': True, 'isCASec': False, 'isSLBSec': True, 'isDebtSec': False, 'isSuspended': False, 'tempSuspendedSeries': [], 'isETFSec': False, 'isDelisted': False, 'isin': 'INE117A01022', 'isMunicipalBond': False, 'isTop10': False, 'identifier': 'ABBEQN'}, 'metadata': {'series': 'EQ', 'symbol': 'ABB', 'isin': 'INE117A01022', 'status': 'Listed', 'listingDate': '08-Feb-1995', 'industry': 'Heavy Electrical Equipment', 'lastUpdateTime': '26-Jul-2024 16:00:00', 'pdSectorPe': 110.46, 'pdSymbolPe': 110.46, 'pdSectorInd': 'NIFTY NEXT 50', 'pdSectorIndAll': ['NIFTY NEXT 50', 'NIFTY TOTAL MARKET', 'NIFTY MNC', 'NIFTY 200', 'NIFTY100 QUALITY 30', 'NIFTY ALPHA 50', 'NIFTY100 EQUAL WEIGHT', 'NIFTY100 ESG SECTOR LEADERS', 'NIFTY LARGEMIDCAP 250', 'NIFTY500 MULTICAP 50:25:25', 'NIFTY200 MOMENTUM 30', 'NIFTY500 LARGEMIDSMALL EQUAL-CAP WEIGHTED', 'NIFTY200 ALPHA 30', 'NIFTY500 EQUAL WEIGHT', 'NIFTY100 ESG', 'NIFTY500 MOMENTUM 50', 'NIFTY INDIA MANUFACTURING', 'NIFTY 500', 'NIFTY 100']}, 'securityInfo': {'boardStatus': 'Main', 'tradingStatus': 'Active', 'tradingSegment': 'Normal Market', 'sessionNo': '-', 'slb': 'Yes', 'classOfShare': 'Equity', 'derivatives': 'Yes', 'surveillance': {'surv': None, 'desc': None}, 'faceValue': 2, 'issuedSize': 211908375}, 'sddDetails': {'SDDAuditor': '-', 'SDDStatus': '-'}, 'priceInfo': {'lastPrice': 7849, 'change': 225.19999999999982, 'pChange': 2.95390750019675, 'previousClose': 7623.8, 'open': 7698.95, 'close': 7851.25, 'vwap': 7789.44, 'lowerCP': '6861.45', 'upperCP': '8386.15', 'pPriceBand': 'No Band', 'basePrice': 7623.8, 'intraDayHighLow': {'min': 7649.35, 'max': 7870, 'value': 7849}, 'weekHighLow': {'min': 3850, 'minDate': '26-Oct-2023', 'max': 9149.95, 'maxDate': '18-Jun-2024', 'value': 7849}, 'iNavValue': None, 'checkINAV': False, 'tickSize': 0.05}, 'industryInfo': {'macro': 'Industrials', 'sector': 'Capital Goods', 'industry': 'Electrical Equipment', 'basicIndustry': 'Heavy Electrical Equipment'}, 'preOpenMarket': {'preopen': [{'price': 7471.35, 'buyQty': 0, 'sellQty': 1}, {'price': 7599, 'buyQty': 0, 'sellQty': 1}, {'price': 7608, 'buyQty': 0, 'sellQty': 5}, {'price': 7620, 'buyQty': 0, 'sellQty': 35}, {'price': 7698.95, 'buyQty': 0, 'sellQty': 0, 'iep': True}, {'price': 7800.4, 'buyQty': 1, 'sellQty': 0}, {'price': 7800.9, 'buyQty': 2, 'sellQty': 0}, {'price': 7852.5, 'buyQty': 26, 'sellQty': 0}, {'price': 7918.6, 'buyQty': 58, 'sellQty': 0}], 'ato': {'buy': 71, 'sell': 55}, 'IEP': 7698.95, 'totalTradedVolume': 264, 'finalPrice': 7698.95, 'finalQuantity': 264, 'lastUpdateTime': '26-Jul-2024 09:07:11', 'totalBuyQuantity': 2977, 'totalSellQuantity': 5441, 'atoBuyQty': 71, 'atoSellQty': 55, 'Change': 75.14999999999964, 'perChange': 0.9857289015976237, 'prevClose': 7623.8}}

#### Thank you.
#### Developed by Akhil kodati
### If you like my work please follow me on https://github.com/Akhilkodati
