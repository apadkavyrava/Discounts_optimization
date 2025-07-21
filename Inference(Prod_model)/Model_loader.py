import xgboost as xgb

purchase_model = xgb.XGBClassifier()
purchase_model.load_model("path")