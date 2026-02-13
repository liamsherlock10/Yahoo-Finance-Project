import pandas as pd

inputTxt = '2026FD.txt'
outputCSV = 'FederalDisclosures.csv'

df = pd.read_csv(inputTxt, sep='\t')


df.to_csv(outputCSV, index=False)
