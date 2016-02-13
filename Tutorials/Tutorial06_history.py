import numpy as np

def initialize(context):
    context.stock = sid(24)
    context.market = sid(8554)
 

def before_trading_start(context, data):
    pass
    
def handle_data(context, data):
    '''log.info(get_datetime())
    for stock in data:
        log.info('Close price for %s: %.2f' % (stock.symbol, data[stock].close_price))
    log.info('\n')'''
    
    #print history(5, '1m', 'close_price')
    #hist = history(11, '1d', 'close_price')
    hist1 = history(10, '1m', 'close_price')
    
    for stock in data:
        # Excludes last row since today has partial information.
        #print '10-day mean close price for stock %s: %.2f' % (stock.symbol, np.mean(hist[stock][:-1])) 
              
        # Doesn't have to exclude last row since it uses minutely data.
        print '10-minute mean close price for stock %s: %.2f' % (stock.symbol, np.mean(hist1[stock]))
