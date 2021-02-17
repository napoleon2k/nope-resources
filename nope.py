# call_chain = Options.chain("call", "SPY", "now", "2023")
# total_call_delta = 0
# for expiration in call_chain.expirations:
#     for strike in expiration.strikes:
#         total_call_delta += strike.delta * strike.todays_volume
# 
# put_chain = Options.chain("put", "SPY", "now", "2023")
# total_put_delta = 0
# for expiration in put_chain.expirations:
#     for strike in expiration.strikes:
#         total_put_delta += strike.delta * strike.todays_volume
# 
# total_share_volume = Stock("SPY").todays_volume
# 
# NOPE = (total_call_delta+total_put_delta) / total_share_volume

# psionara - #nope-questions
# That process looks correct.
# 
# Every time you want to calculate a NOPE score you just iterate through all $strike/expiration combinations currently traded on both the call side and put side and multiply the contracts' respective deltas by their volumes so far for the day. Sum up all the respective delta*option volumes to get the total net delta for the numerator, and then just divide this sum by the share volume so far for the day.
# 
# - For the model on the website, all call deltas are positive; all put deltas are negative. 
# - All deltas for standard options are treated as 0 to +/- 100 (instead of 0.00 to +/-1.00).
# - The NOPE values shown on the website are multiplied by 100%.
