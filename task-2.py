import pandas as pd


def compute_score(json_file_path: str, output_file_path:str):
    data = pd.read_json(json_file_path)
    exploded_df = data.explode('app', ignore_index=True)
    exploded_df = pd.concat([exploded_df.drop('app', axis = 1), pd.json_normalize(exploded_df['app'])], axis = 1)

    exploded_df['Debt_to_EBITDA'] = (exploded_df['Reports.1510'] + exploded_df['Reports.1510'])/exploded_df['Factors.10007']
    exploded_df['Score_fin'] = exploded_df['Debt_to_EBITDA'].apply(lambda x: 100 if x < 2 else (50 if x < 4 else 0))
    exploded_df['Score_qual'] = exploded_df['Factors.MARKET_LVL'].apply(lambda x: 0 if x == 'A' else (50 if x == 'B' else 100))
    exploded_df['Total_score'] = 0.8 * exploded_df['Score_fin'] + 0.2 * exploded_df['Score_qual']

    exploded_df[['RqUID', 'DateTime', 'Score_fin', 'Score_qual', 'Total_score']].to_json(output_file_path, orient='records', date_format='iso')


if __name__ == '__main__':
    compute_score('in_data.json', 'out_data.json')