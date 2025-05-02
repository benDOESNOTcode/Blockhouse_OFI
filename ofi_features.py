import numpy as np
import pandas as pd


#function to calculate order flow change
# for either bid or ask side
def calculate_order_flow_change(curr_price, prev_price, curr_size, prev_size, side):
    #for the bid side
    if side == 'bid':
        if curr_price > prev_price:
            return curr_size            # new aggressive bid
        elif curr_price == prev_price:
            return curr_size - prev_size  # size update at same price
        else:
            return -curr_size          # bid pulled back or weakened
    #for the ask side
    elif side == 'ask':
        if curr_price > prev_price:
            return -curr_size          # ask moved up → less aggressive
        elif curr_price == prev_price:
            return curr_size - prev_size
        else:
            return curr_size           # ask moved down → more aggressive


#compute Best-Level OFI for a specific depth level
def compute_best_level_ofi(df, level=0):
    level_str = f"{level:02d}"  #format level as 2-digit string (e.g. 00, 01...)

    ofi_list = [0]  #first row has no previous row, so we initialize with 0

    for i in range(1, len(df)):
        #bid side OFI
        bid_of = calculate_order_flow_change(
            df[f'bid_px_{level_str}'].iloc[i],
            df[f'bid_px_{level_str}'].iloc[i - 1],
            df[f'bid_sz_{level_str}'].iloc[i],
            df[f'bid_sz_{level_str}'].iloc[i - 1],
            'bid'
        )
        #ask side OFI
        ask_of = calculate_order_flow_change(
            df[f'ask_px_{level_str}'].iloc[i],
            df[f'ask_px_{level_str}'].iloc[i - 1],
            df[f'ask_sz_{level_str}'].iloc[i],
            df[f'ask_sz_{level_str}'].iloc[i - 1],
            'ask'
        )
        #OFI = Bid pressure - Ask pressure
        ofi_list.append(bid_of - ask_of)

    #return as a pd series with the same index as df
    return pd.Series(ofi_list, index=df.index, name=f'ofi_level_{level_str}')
