import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_ecommerce_data(num_customers=1000, start_date='2024-01-01', end_date='2024-12-31'):
    np.random.seed(42) # for reproducibility

    customer_ids = [f'CUST_{i:04d}' for i in range(num_customers)]
    data = []

    for cust_id in customer_ids:
        # Simulate customer acquisition date
        acquisition_date = datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=np.random.randint(0, 365))

        # Simulate total purchase amount
        total_spent = np.random.normal(loc=5000, scale=2000)
        total_spent = max(100, round(total_spent, 2)) # Ensure minimum spent

        # Simulate average order value
        avg_order_value = np.random.normal(loc=1000, scale=300)
        avg_order_value = max(50, round(avg_order_value, 2))

        # Simulate number of orders
        num_orders = int(total_spent / avg_order_value) if avg_order_value > 0 else 1
        num_orders = max(1, num_orders) # Ensure at least 1 order

        # Simulate last purchase date (more recent for non-churners)
        # Churn probability based on total_spent and num_orders
        churn_prob = 1 / (1 + np.exp(0.0005 * total_spent + 0.1 * num_orders - 5))
        is_churn = np.random.rand() < churn_prob

        if is_churn:
            # Last purchase date is older for churned customers
            last_purchase_days_ago = np.random.randint(60, 365) # 2 to 12 months ago
        else:
            # Last purchase date is more recent for active customers
            last_purchase_days_ago = np.random.randint(1, 60) # 1 day to 2 months ago

        last_purchase_date = datetime.now() - timedelta(days=last_purchase_days_ago)

        # Calculate recency (days since last purchase)
        recency = (datetime.now() - last_purchase_date).days

        # Add some random features
        product_category_pref = np.random.choice(['Electronics', 'Apparel', 'Home Goods', 'Books', 'Groceries'], p=[0.2, 0.3, 0.2, 0.15, 0.15])
        marketing_channel = np.random.choice(['Social Media', 'Email', 'Referral', 'Paid Ads'], p=[0.3, 0.3, 0.2, 0.2])

        data.append({
            'customer_id': cust_id,
            'acquisition_date': acquisition_date.strftime('%Y-%m-%d'),
            'total_spent': total_spent,
            'num_orders': num_orders,
            'avg_order_value': avg_order_value,
            'last_purchase_date': last_purchase_date.strftime('%Y-%m-%d'),
            'recency_days': recency,
            'product_category_pref': product_category_pref,
            'marketing_channel': marketing_channel,
            'is_churn': int(is_churn) # 1 for churn, 0 for not churn
        })

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_ecommerce_data(num_customers=2000) # Generate 2000 sample customers
    df.to_csv('ecommerce_customer_data.csv', index=False)
    print("Generated 'ecommerce_customer_data.csv' with 2000 entries.")
    print(df.head())
    print(df['is_churn'].value_counts())