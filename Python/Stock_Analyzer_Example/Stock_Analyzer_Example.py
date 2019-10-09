"""
A simple stock analyzer that collects data from 3 stock-listed company files
(NASDAQ, NYSE, and AMEX), and parses it into a single delimited file where
a user can search company data from all 3 file sources.

Author: Oscar Lopez
"""


def clean_data(data):
    """
    Removes any trailing new lines, replaces '"' with tab delimiter, and
    removes trailing commas and unnecessary quotation marks.
    Parameters:
        data: String of data.
    """
    data = data.strip("\n")
    data = data.replace('","', "\t")
    data = data.replace('"', '')
    # remove unnecessary comma at end of data.
    data = data[:len(data) -1]
    return data


def parse_file_as_dict(*filename):
    """
    Parses data from an opened file into a dictionary data.
    Parameters:
        (String) *filename: File name(s) of data to be parsed as dictionary of data.
    """
    parsed_data_dict = dict()
    for f in filename:
        try:
            fopen = open(f)
        except:
            print(f'ERROR: Could not parse data from {f}!')
            continue
        #ignore header of file.
        fopen.readline()
        for line in fopen:
            line = clean_data(line)
            data_list = line.split('\t')
            symbol = data_list[0]
            parsed_data_dict.update(
                {
                    symbol:{
                        'Name': data_list[1],
                        'Last Sale': data_list[2],
                        'Market Cap': data_list[3],
                        'ADR TSO': data_list[4],
                        'IPO Year': data_list[5],
                        'Sector': data_list[6],
                        'Industry': data_list[7],
                        'Summary Quote': data_list[8]
                    }
                }
            )
        fopen.close()
    return parsed_data_dict


def parse_file_as_list(*filename):
    """
    Parses all data from file(s) as a list.
    Parameters:
        (String) *filename: File name(s) of data to be parsed as a list of
        data.
    """
    parsed_data_list = list()
    for f in filename:
        try:
            fopen = open(f)
        except:
            print(f'ERROR: Could not parse data from {f}!')
            continue
        #ignore header of file.
        fopen.readline()
        for line in fopen:
            line = clean_data(line)
            data_list = line.split('\t')
            parsed_data_list.append(data_list)
    return parsed_data_list


def output_data_file(filename, data):
    """
    Writes data to an output file.
    Parameters:
        (String) filename: Name of file to be written to.
        (list) data: Data to be written to file.
    """
    f_write = open(filename, "w+")
    data.sort()
    for line in data:
        for element in line:
            f_write.write(str(element) + '\t')
        f_write.write('\n')
    f_write.close()
    print(f'Finished writing data to {filename}')


def search_symbol(symbol, dict_data):
    """
    Searches for a company symbol and returns its data as a formatted string if
    found.Returns None otherwise.
    Parameters:
        (String) symbol: Company tag to be searched for.
        (dict) dict_data: Dictionary of data to be searched through.
    """
    symbol = symbol.upper()
    if symbol in dict_data:
        name = dict_data[symbol]['Name']
        last_sale = dict_data[symbol]['Last Sale']
        market_cap = dict_data[symbol]['Market Cap']
        ipo_year = dict_data[symbol]['IPO Year']
        sector = dict_data[symbol]['Sector']
        industry = dict_data[symbol]['Industry']
        return f'{symbol}, {name}, {last_sale}, {market_cap}, {ipo_year}, {sector}, {industry}'
    return None

def get_top_15_marketcap(data):
    """
    Gets the top 15 companies based on their marketcap.
    Parameters:
        (list)data: A compiled list of lists of company data.
    """
    top_15_marketcap = list()
    all_company_marketcap = list()
    for line in data:
        company_tag = line[0]
        company_marketcap = line[3]
        all_company_marketcap.append([company_marketcap, company_tag])
    all_company_marketcap.sort(reverse=True)
    for i in range(0,15):
        top_15_marketcap.append(all_company_marketcap[i])
    return top_15_marketcap


def display_menu():
    """
    Returns the main menu of the program.
    """
    return """
            Lopez's CompanyList Data Analyzer
            ======================================
            1 : Export to merged/sorted(by stock symbol) CSV file.
            2 : Search by stock symbol.
            3 : Display 15 Companies with the highest MarketCap value.
            4 : Exit
            """


def promptChoice(prompt):
    """
    Returns the numerical choice of a prompt. Otherwise returns None.
    """
    try:
        return int(input(prompt))
    except ValueError:
        return None

""" Main Program. """
# Parsing and preparing csv datasets.
data_dict = parse_file_as_dict('companylist_nasdaq.csv',
                               'companylist_nyse.csv',
                               'companylist_amex.csv')
data_list = parse_file_as_list('companylist_nasdaq.csv',
                               'companylist_nyse.csv',
                               'companylist_amex.csv')

print(display_menu())
while True:
    try:
        user_choice = int(promptChoice('> '))
    except:
        print('Plese enter a valid numerical value!')
        continue
    if user_choice == 1:
        filename = input('What will be the name of the file? ')
        output_data_file(filename, data_list)
        print(f'Sorted data exported to {filename}')
    elif user_choice == 2:
        company_symbol = input('Enter company symbol: ')
        result = search_symbol(company_symbol, data_dict)
        if result:
            print(result)
        else:
            print(f'Sorry, {company_symbol} not found!')
    elif user_choice == 3:
        for company in enumerate(get_top_15_marketcap(data_list)):
            print(f'{company[0] + 1} : Company: {company[1][1]} : MarketCap: {company[1][0]}')
    elif user_choice == 4:
        print('Exiting.')
        break
    else:
        print('Please enter a valid choice from the menu!')
