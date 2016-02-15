import numpy as np

def initialize(context): 
    # Runs every day, half an hour after market open.
    schedule_function(check_mean, date_rules.every_day(), time_rules.market_open(minutes=5))
    schedule_function(check_mean, date_rules.every_day(), time_rules.market_open(minutes=10))
    schedule_function(check_mean, date_rules.every_day(), time_rules.market_open(minutes=15))
    schedule_function(check_mean, date_rules.every_day(), time_rules.market_open(minutes=20))
    schedule_function(check_mean, date_rules.every_day(), time_rules.market_open(minutes=25))

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
    
    hist_1 = history(1, '1m', 'close_price')
    hist_2 = history(2, '1m', 'close_price')
    hist_3 = history(3, '1m', 'close_price')
    hist_4 = history(4, '1m', 'close_price')
    hist_5 = history(5, '1m', 'close_price')
    for stock in data:
        #print '10-minute mean close price for stock %s: %.2f' % (stock.symbol, np.mean(hist[stock]))
        print '%s - mean price: %.2f, total revenue: %.2f' % (stock.symbol, np.mean(hist[stock]), context.fundamental_df[stock][0])
