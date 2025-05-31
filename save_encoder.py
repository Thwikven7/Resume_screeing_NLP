import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the data
df = pd.read_csv('UpdatedResumeDataSet.csv')

# Create and fit the encoder
le = LabelEncoder()
le.fit(df['Category'])

# Save the encoder
with open('encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("Encoder saved successfully!") 