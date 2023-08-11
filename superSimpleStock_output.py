import pandas
import math
import datetime
import dateutil


def get_div_yield(in_csv_data, stock, in_price):
    dstock= in_csv_data[in_csv_data['Stock_Symbol'] == stock]
    if list(dstock['Type'])[0] == 'Common':
        return list(dstock['Last_Dividend'])[0] / in_price
    elif list(dstock['Type'])[0] == 'Preferred':
        return (list(dstock['Fixed_Dividend'])[0] * list(dstock['Par_Value'])[0]) / in_price
    
def get_pe_ratio(in_csv_data,stock, in_price):
    div= get_div_yield(in_csv_data,stock, in_price)
    return in_price / div

def record_trade(trade,stock, quantity, sold, price):
    newtrade= {'Stock_Symbol': stock,
            'timestamp': datetime.datetime.now(),
            'quantity': quantity,
            'sold': sold,
            'price': price}
    trade = pandas.concat([trade,pandas.DataFrame([newtrade])],ignore_index=True)
    return trade

def get_all_share_index():
        all_share_index= 1
        n= 0
        for p in list(trade['price']):
            all_share_index *= p
            n += 1
        return all_share_index ** (1 / n)

if __name__ == "__main__":
    csv_data= pandas.read_csv('sample_data.csv')
    div_yield = get_div_yield(csv_data,'ALE',4)
    pe_ratio = get_pe_ratio(csv_data,'ALE',4)
    trade= pandas.DataFrame({'Stock_Symbol': [], 'timestamp': [], 'quantity': [], 'sold': [], 'price': []})
    trade = record_trade(trade,stock= 'ALE', quantity= 5, sold= True, price= 6)
    print(trade)
    share_index = get_all_share_index()
    print(share_index)
