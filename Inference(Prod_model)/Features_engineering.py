import pandas as pd


def features(data):

    data = data.sort_values(['user_id', 'sent_at'])
    
    # last_email
    data['sent_at'] = pd.to_datetime(data['sent_at'])
    data = data_raw.sort_values(['user_id', 'sent_at'])
    data_raw['last_email'] = data.groupby('user_id')['purchase'].shift(1).fillna(0).astype(int)
    
    # weekend
    data['weekend'] = ((data['purchase'] == 1) & (data['sent_at'].dt.weekday >= 5).astype(int)
    
    #same_day
    data['day_month'] = data_raw['sent_at'].dt.strftime('%m-%d')
    data['same_day'] = 0
    grouped = purchase_data.groupby(['user_id', 'day_month']).apply(lambda x: x.index[1:] if len(x) > 1 else []).explode()
    data.loc[grouped.dropna(), 'same_day'] = 1
    
    #avg_email_sent
    data['cumcount'] = data.groupby('user_id').cumcount()
    data['cum_purchases'] = data.groupby('user_id')['purchase'].cumsum()
    data['cum_emails'] = data['cumcount'] - data['cum_purchases'] 
    data['avg_email_sent'] = (data['cum_emails'] / data['cum_purchases']).abs()

    #opened_email - dataset column
    
    #discount%'
    data['discount%'] = (data['TOTAL_COST_PRE_DISCOUNT_PENNIES']/data['TOTAL_COST_PENNIES']*10).round(0.05)
                                        
    #max_purchase_discount
    data_raw['max_purchase_discount'] = data_raw.groupby('user_id').apply(
    lambda group: group.apply(
        lambda row: group.loc[:row.name][group.loc[:row.name, 'purchase'] == 1]['discount%'].value_counts().idxmax() 
        if len(group.loc[:row.name][group.loc[:row.name, 'purchase'] == 1]) > 0 else 0, 
        axis=1)
        ).values
                       
    #last_pos_email
    data_raw['last_pos_email'] = data_raw.groupby('user_id')['purchase'].transform(
    lambda x: [x[:i+1].argmax() if (x[:i+1] == 1).any() else i+1 
               for i in range(len(x))]) 
                       
    #avg_days_between_purchases
    data['prev_purchase_date'] = data.groupby('user_id')['sent_at'].shift(1)
    data['days_since_last_purchase'] = (data['sent_at'] - data['prev_purchase_date']).dt.days
    data['purchase_count'] = data.groupby('user_id').cumcount() + 1
    data['cumsum_days'] = data.groupby('user_id')['days_since_last_purchase'].cumsum()
    data['avg_days_between_purchases'] = data['cumsum_days'] / (data['purchase_count'] - 1)
                       
    #dataset cleaning                 
                       
    dataset = data[['user_id','last_email', 'weekend', 'same_day', 'avg_email_sent', 'opened_email',
       'discount%', 'max_purchase_discount', 'last_pos_email','avg_days_between_purchases']] 
                 
                       
    return dataset               
                       
   
                       