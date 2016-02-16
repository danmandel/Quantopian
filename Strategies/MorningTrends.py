import numpy as np

def initialize(context): 
    # Runs every day, half an hour after market open.
    schedule_function(check_mean, date_rules.every_day(), time_rules.market_open(minutes=5))
    
def before_trading_start(context, data):
    context.fundamental_df = get_fundamentals(
        query(
            fundamentals.income_statement.total_revenue
        )
        .filter(
            fundamentals.valuation.market_cap > 300000000000
        )
        .order_by(
            fundamentals.valuation.market_cap.desc()
        )
        .limit(10)
    )
    
    update_universe(context.fundamental_df.columns.values)
    
def handle_data(context, data):
    
    pass
           
def check_mean(context, data):
    print get_datetime('US/Eastern')
    
    hist_1 = history(10, '1m', 'close_price')
  
    for stock in data:
        #print '10-minute mean close price for stock %s: %.2f' % (stock.symbol, np.mean(hist[stock]))
        print '%s - mean price: %.2f, total revenue: %.2f' % (stock.symbol, np.mean(hist[stock]), context.fundamental_df[stock][0])
    print '-----------------------'
    
def get_x_min_history(context, data, x):
    close_history = history(x,'1m', 'close_price')
    for stock in data:
        previous_bar = close_history[stock][-2]
        current_bar = close_history[stock][-1]
