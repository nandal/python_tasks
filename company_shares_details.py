'''
Created on 16-Jun-2014

@author: Sandeep Nandal
@email: sandeep@nandal.in
'''
import random


def create_test_data(filename):
    """ this function will generate the data.txt file and fill it with dummy data for testing """
    #month names whhich will be used to create dummy data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # creating data.txt file in write mode
    file_handler = open(filename, "w")
    
    #write the header to data.txt file
    file_handler.write("Year,Month")
    
    # here we are writing 1 to 99 dummy company names to file
    for i in range(1,100):
        file_handler.write(",Company "+str(i))
        
    # writing end of file
    file_handler.write("\n")
    
    #write dummy data to data.txt file since 1990 till 2014
    for year in range(1990, 2015):
        for month in months:
            # check if the year and month are current then return the function after closing the file
            if month == 'Jun' and year == 2014:
                file_handler.close()
                return 
            
            # writing year and month to data file
            file_handler.write(str(year)+","+str(month))
            
            # writing random share prices under each company name in data file
            for i in range(1,100):
                
                # this random function will return a random value between 10 n 500 for share prices
                file_handler.write(","+str(random.randint(10,500)))
                
            file_handler.write("\n")
    file_handler.close()
    
    
    
    
def get_highest_share_list_of_companies(data_file):
    "this function will return a dictionary of all the companies containing their year n month of highest share prices"
    result_dict = {} # this will be the result dictionary
    company_list = []   # this will contain the names of all the companys
    
    #open file and read first line for collecting heading information
    file_handler = open(data_file, "r")
    headline = file_handler.readline()
    
    #creating list of items of first line of data file
    headings = headline.split(",")
    
    #calculating the total number of headings in data file
    total_headings = len(headings)
    
    # now we read the names of each company and store them in list company_list
    # we start from 2 index because 0 n 1 index contains Year n Month Headings
    for i in range(2, total_headings):
        company_list.append(headings[i].strip())
        
        # we enter default data in result dictionary to the corresponding company keys
        result_dict[headings[i].strip()] =  {"year":None,"month":None,"share_price":0}
        
        
    line = file_handler.readline()
    while line:
        # create a list of data items from the line we read
        share_prices = line.split(",")
        
        # we start loop from 2 because the 0 n 1 index of share_prices list contains year n month
        for i in range(2, total_headings):
            #check if the current share price is higher then the stored one
            #if yes then update the result in result dictionary
            if result_dict[company_list[i-2]]["share_price"] < int(share_prices[i].strip()):
                result_dict[company_list[i-2]]["share_price"] = int(share_prices[i].strip())
                result_dict[company_list[i-2]]["year"] = int(share_prices[0].strip())
                result_dict[company_list[i-2]]["month"] = share_prices[1].strip()
        
        #read next line
        line = file_handler.readline()
    
    # now return the dictionary which contains the months, years, share prices of highest share prices for each company
    return result_dict

def write_result_file(filename, result_dictionary):
    """ this function will create a simple text file of result from dictionary, it can be used for testing the result with main data file"""
    file_handler = open(filename, "w")
    file_handler.write("Company Name, Year, Month, Share Price\n")
    for company in (sorted(result_dictionary.iterkeys())):
        file_handler.write(company)
        file_handler.write(","+str(result_dictionary[company]["year"]))
        file_handler.write(","+str(result_dictionary[company]["month"]))
        file_handler.write(","+str(result_dictionary[company]["share_price"])+"\n")
    file_handler.close()
    
    
    
# here is the main block for which will use above functions to generate the result required
if __name__ == '__main__':
    
    # this will create a data file with dummy n random data for testing
    create_test_data("data.txt")
    print "data file is created"
    
    # now this dictionary will contain the months, year, n share price of highest share price for each company
    # it can be used in any way we want to access the values
    result_dictionary = get_highest_share_list_of_companies("data.txt")
    print "result is fetched from data file"
    
    #lets create a result file which will contain all this info in csv format
    write_result_file("result.txt", result_dictionary)
    print "result file is generated"
