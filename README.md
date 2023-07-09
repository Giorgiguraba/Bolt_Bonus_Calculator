# Bolt Bonus Calculator

This Python script generates a bonus dataset for Bolt, consisting of bonus campaigns with payout dates and amounts. The dataset is saved as a CSV file.

### Prerequisites
- Python 3.x
- pandas library

### Usage

1. Clone the repository or download the code.

2. Install the required dependencies by running the following command:
   pip install pandas
3. Run the script `bonus_dataset_generation.py`:
   python bonus_dataset_generation.py
4. The generated bonus dataset will be saved as a CSV file named `bonus_dataset_bolt.csv` in the same directory as the script.

## Dataset Structure

The generated dataset contains the following columns:

- Bonus Campaign: The name of the bonus campaign.
- Payout Date: The date of payout for the campaign.
- Payout Amount: The amount of the payout.

## Example Output

The script will display the total spend for each bonus campaign per week:
Week 01:
Bonus Campaign A: $500
Bonus Campaign B: $800
Bonus Campaign C: $600

Week 02:
Bonus Campaign B: $750
Bonus Campaign C: $900
Bonus Campaign D: $550
