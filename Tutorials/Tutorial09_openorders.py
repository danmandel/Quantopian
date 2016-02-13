def initialize(context):
    context.stock = sid(40768)

# Will be called on every trade event for the securities you specify. 
def handle_data(context, data):
    open_orders = get_open_orders()
    if context.stock not in open_orders:
        order_target_percent(context.stock, 1.00) 
    
    record(cash = context.portfolio.cash) # cash at end of each day
