import os

from Data_download import load_data
from  Features_engineering import features
from Model_loader import purchase_model
from Optimization_func import Optimization


def main():
    db_url = os.getenv("DB_URL")
    discount_range = os.getenv("DISCOUNT_RANGE")
    probability_threshold = os.getenv("PROBABILITY_THRESHOLD")
    
    data = load_data(db_url)
    
    features_set = features(data)
    
    optimal_discounts = Optimization(feature_set, purchase_model, discount_range, probability_threshold)

    
    
    
    
    