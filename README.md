## nse_live_stocks

Open source unoffical python library for extracting realtime stock data from National Stock Exchange (India) .

#### Introduction.

nselivestocks library is to collect the real time stock information just by giving the nse symbol.

#### Command to install 

**pip install nse_live_stocks**

### Example:

i) Get current price of any nse stock 
from nse_live_stocks import Nse

stock = Nse()
stock.get_current_price('TCS')

Output:
{'error': False, 'nse_symbol': 'TCS', 'current_value': '4393.65', 'date': '26-Jul-2024 09:07:13'}

###

ii) Get Complete information of any nse stock 

from nse_live_stocks import Nse

stock = Nse()
stock.get_stock_info('ABB')

Output:

{'info': {'symbol': 'ABB', 'companyName': 'ABB India Limited', 'industry': 'ELECTRICAL EQUIPMENT', 'activeSeries': ['EQ'], 'debtSeries': [], 'isFNOSec': True, 'isCASec': False, 'isSLBSec': True, 'isDebtSec': False, 'isSuspended': False, 'tempSuspendedSeries': [], 'isETFSec': False, 'isDelisted': False, 'isin': 'INE117A01022', 'isMunicipalBond': False, 'isTop10': False, 'identifier': 'ABBEQN'}, 'metadata': {'series': 'EQ', 'symbol': 'ABB', 'isin': 'INE117A01022', 'status': 'Listed', 'listingDate': '08-Feb-1995', 'industry': 'Heavy Electrical Equipment', 'lastUpdateTime': '26-Jul-2024 16:00:00', 'pdSectorPe': 110.46, 'pdSymbolPe': 110.46, 'pdSectorInd': 'NIFTY NEXT 50', 'pdSectorIndAll': ['NIFTY NEXT 50', 'NIFTY TOTAL MARKET', 'NIFTY MNC', 'NIFTY 200', 'NIFTY100 QUALITY 30', 'NIFTY ALPHA 50', 'NIFTY100 EQUAL WEIGHT', 'NIFTY100 ESG SECTOR LEADERS', 'NIFTY LARGEMIDCAP 250', 'NIFTY500 MULTICAP 50:25:25', 'NIFTY200 MOMENTUM 30', 'NIFTY500 LARGEMIDSMALL EQUAL-CAP WEIGHTED', 'NIFTY200 ALPHA 30', 'NIFTY500 EQUAL WEIGHT', 'NIFTY100 ESG', 'NIFTY500 MOMENTUM 50', 'NIFTY INDIA MANUFACTURING', 'NIFTY 500', 'NIFTY 100']}, 'securityInfo': {'boardStatus': 'Main', 'tradingStatus': 'Active', 'tradingSegment': 'Normal Market', 'sessionNo': '-', 'slb': 'Yes', 'classOfShare': 'Equity', 'derivatives': 'Yes', 'surveillance': {'surv': None, 'desc': None}, 'faceValue': 2, 'issuedSize': 211908375}, 'sddDetails': {'SDDAuditor': '-', 'SDDStatus': '-'}, 'priceInfo': {'lastPrice': 7849, 'change': 225.19999999999982, 'pChange': 2.95390750019675, 'previousClose': 7623.8, 'open': 7698.95, 'close': 7851.25, 'vwap': 7789.44, 'lowerCP': '6861.45', 'upperCP': '8386.15', 'pPriceBand': 'No Band', 'basePrice': 7623.8, 'intraDayHighLow': {'min': 7649.35, 'max': 7870, 'value': 7849}, 'weekHighLow': {'min': 3850, 'minDate': '26-Oct-2023', 'max': 9149.95, 'maxDate': '18-Jun-2024', 'value': 7849}, 'iNavValue': None, 'checkINAV': False, 'tickSize': 0.05}, 'industryInfo': {'macro': 'Industrials', 'sector': 'Capital Goods', 'industry': 'Electrical Equipment', 'basicIndustry': 'Heavy Electrical Equipment'}, 'preOpenMarket': {'preopen': [{'price': 7471.35, 'buyQty': 0, 'sellQty': 1}, {'price': 7599, 'buyQty': 0, 'sellQty': 1}, {'price': 7608, 'buyQty': 0, 'sellQty': 5}, {'price': 7620, 'buyQty': 0, 'sellQty': 35}, {'price': 7698.95, 'buyQty': 0, 'sellQty': 0, 'iep': True}, {'price': 7800.4, 'buyQty': 1, 'sellQty': 0}, {'price': 7800.9, 'buyQty': 2, 'sellQty': 0}, {'price': 7852.5, 'buyQty': 26, 'sellQty': 0}, {'price': 7918.6, 'buyQty': 58, 'sellQty': 0}], 'ato': {'buy': 71, 'sell': 55}, 'IEP': 7698.95, 'totalTradedVolume': 264, 'finalPrice': 7698.95, 'finalQuantity': 264, 'lastUpdateTime': '26-Jul-2024 09:07:11', 'totalBuyQuantity': 2977, 'totalSellQuantity': 5441, 'atoBuyQty': 71, 'atoSellQty': 55, 'Change': 75.14999999999964, 'perChange': 0.9857289015976237, 'prevClose': 7623.8}}

#### Thank you.
#### Akhil kodati








