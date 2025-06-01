# Dynamic Pricing Engine

A containerised machine learning based engine that calculates optimal product prices in real time using user indicators, competitor prices, churn logic, and price elasticity. Designed to be scaled and personalised with minimal effort (screenshots below).

## Features

- Modular components (user profiling, churn, elasticity, competitor pricing)
- Business logic controls (profit max, churn reduction, loyalty)
- Real time price prediction with pre-trained ML model
- Easily integrated into web apps (FastAPI)
- Lightweight model training with scikit-learn

## Project Structure
```
dynamic-pricing-engine/
├── api/ # FastAPI for outputting prices
│ └── main.py
├── dashboard/ #To control strategy weights
│ └── app.py
├── models/ # Saved ML models
│ └── price_model.pkl
├── modules/ # Modular features
│ ├── user_profile.py
│ ├── churn_model.py
│ ├── competitor_prices.py
│ ├── elasticity.py
│ └── feature_builder.py
├── training/ # Training scripts and notebooks
│ └── train_model.py
├── strategy/ # Logic (weights, utility scoring, presets)
│ ├── strategy_controller.py
│ └── utility_optimiser
├── data/ # Sample or real data (optional .gitignore protected)
│ └── pricing_dataset.csv
├── tests/ # Unit tests
├── requirements.txt
├── .env.example # Change to .env when needed
└── README.md
```

## How it Works
1. **Input**: userID + productID + strategy_weights
2. **Feature builder** gathers data from:

    - User profiling  
    - Competitor pricing API  
    - Churn & elasticity logic  

3. **ML Model** predicts an optimal price  
4. **Output** float (price) served via API  

## Model Training
- Uses `scikit-learn` with `RandomForestRegressor`
- Can be retrained with your own dataset using:

```bash
python training/train_model.py --data data/pricing_dataset.csv
```

## Screenshots / Demo
