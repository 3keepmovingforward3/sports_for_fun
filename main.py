from pathlib import Path
import pandas as pd
import kagglehub

'''
Column things to check
open close, except zero check if minus
check columns j to v match w

forumla = previous 4 games total points => (aj & ak) of each team in matchup predict match outcome
LAST = game played
AL,AK == aj&ak / 4
AD = previous game
IDN = last games total points 
AVG = 35 to 10, 7 to 24; crossed summation of last game
TOT = Straight summation
AV2 = cross average of AVG and IDN
ID2 = straight average of AVG and IDN
LAST4 = points for points allowed (order matters)
LAST4AVG = average of LAST4
MOV = difference LAST4
MOVAVG = MOV/4
SUMLAST4 = Cross summation of LAST4
SUMLAST4AVG = SUMLAST4/4
IDN = straight summ LAST4
IDNAVG = IDN / 4
TOT = MAX(LAST4) goes into lower row, then we sum lesser values into that row
higher values go into upper row
TOTAVG = TOT/4
AV2 = cross average SUMLAST4 and IDN
AV2AVG = average AV2
ID2 = straight average SUMLAST4 and IDN
ID2AVG = average ID2

wayback picture, we want open and stardust from 1 day

'''

'''
    fill_na()

    Fill NA/NAN with zeros because we are mostly working with ints
'''
def data_cleanup(df):
    #for index, row in df.iterrows():
    #    row['DATE'] =  str(row['DATE']).replace('/', '-')
    
    # make dates match format
    #df['DATE'].dt.time = df['TIME'].to_datetime()
    #df.to_excel("data/NBA_Formula.xlsx", index=False)
    for row in df.iterrows():
        row['DATE'] = row['DATE'].split()[0] + ' ' + str(row['TIME'])
    df.to_excel("data/NBA_Formula.xlsx", index=False)
    
# def check_scores_against_database(df_csv, df_excel):
#     # if csvdate == exceldate &&
#     # we select from excelTEAM, which we split into city and name
#     # and we select excelTEAM A or H, which selects csv column home/away team/city
#     # check total score of excel against csv
#     # if same continue, if different replace excel value with CSV
#     
#     # first we split date time is csv
#     for index, row in df_csv.iterrows():
#         break
#         print(row['gameDateTimeEst'].split()[0])

def fill_na(df):
    df.fillna(0)

def data_cleanup(df):
    # check if any NAN, if true fill nan values with 0
    if df.isnull().values.any() == True:
        fill_na(df)

def main() -> int:
    # load excel
    p = Path('data/NBA_Formula.xlsx')
    df_work = pd.read_excel(p)
    data_cleanup(df_work)

    p = Path('data/Games.csv')
    df_dataset = pd.read_csv(p)
    return 0

if __name__ == '__main__':
    main()
