import pandas as pd

def Optimization(dataset, model, discount_range, probability_threshold):
    
    features = data.drop([['user_id', 'purchase']], axis = 1) 
    
    #  Containers
    assigned_discount = pd.Series(np.nan, index=users_df.index, name="optimal_discount")
    assigned_probability = pd.Series(np.nan, index=users_df.index, name="prob_at_optimal")

        #  Feature + discount grid 
    def prepare_batch(features, discount):
        temp = features.copy()
        temp["discount%"] = discount
        temp = pd.get_dummies(temp)
        return temp

    remaining_idx = users_df.index

    #  Run the users batch through the incremented discount loop 
    for d in discount_levels:
        if remaining_idx.size == 0:
            break

        user_batch = prepare_batch(users_df.loc[remaining_idx], d)
        probs = purchase_model.predict_proba(user_batch)[:, 1]

        meets = probs >= probability_threshold
        if not meets.any():
            continue

        qualifying_idx = remaining_idx[meets]
        assigned_discount.loc[qualifying_idx] = d
        assigned_probability.loc[qualifying_idx] = probs[meets]

        # Keep only users that haven't yet qualified
        remaining_idx = remaining_idx[~meets]

    # Assemble result
    result = users_list.copy()
    result["optimal_discount"] = assigned_discount
    result["prob_at_optimal"] = assigned_probability

    # Qualified users only
    return final_result = result.loc[result["optimal_discount"].notna(),
                              ["optimal_discount", "prob_at_optimal"]]

