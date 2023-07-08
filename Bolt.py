import random
import pandas as pd
from datetime import datetime, timedelta

num_rows = 1000

bonus_campaigns = ["Campaign A", "Campaign B", "Campaign C", "Campaign D"]
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

dataset = []
for _ in range(num_rows):
    campaign = random.choice(bonus_campaigns)
    payout_date = random.choice(pd.date_range(start_date, end_date))
    payout_amount = random.randint(100, 1000)
    entry = {"Bonus Campaign": campaign, "Payout Date": payout_date, "Payout Amount": payout_amount}
    dataset.append(entry)

df = pd.DataFrame(dataset)
df.to_csv('bonus_dataset_bolt.csv', index=False)

dataset_file = 'bonus_dataset_bolt.csv'

df = pd.read_csv(dataset_file)
df['Payout Date'] = pd.to_datetime(df['Payout Date'])
df['Week'] = df['Payout Date'].dt.strftime('%U')

total_spend = df.groupby(['Week', 'Bonus Campaign'])['Payout Amount'].sum().reset_index()
for week, week_data in total_spend.groupby('Week'):
    print(f"Week {week}:")
    for _, row in week_data.iterrows():
        bonus_campaign = row['Bonus Campaign']
        spend = row['Payout Amount']
        print(f"  Bonus Campaign {bonus_campaign}: ${spend}")
