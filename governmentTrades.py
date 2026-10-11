import pandas as pd

#This is used to organize the Federal Disclosures CSV. Starts with 2026FD.txt, which has sloppy data.

inputTxt = '2026FD.txt'
outputCSV = 'FederalDisclosures.csv'

df = pd.read_csv(inputTxt, sep='\t')
df.to_csv(outputCSV, index=False)
