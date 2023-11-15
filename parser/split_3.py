import pandas as pd

main_data_input = 'data105.xlsx'
output_data = 'split_data_05.xlsx'

def load_excel_and_split():
    # Load the xlsx file
    excel_data = pd.read_excel(main_data_input)

    # Extract the "about" column
    about_column = excel_data['about']

    # Split the sentences into three parts based on more than 3 spaces
    data = pd.DataFrame(excel_data['name'].str.split(r'\s{3,}', n=2).to_list(), columns=['name', 'author', 'longer'])

    # Add the "about" column to the new DataFrame
    data['about'] = about_column

    # Save the modified data to a new Excel file
    data.to_excel(output_data, index=False)

    return data

load_excel_and_split()