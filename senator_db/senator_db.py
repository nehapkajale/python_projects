#!/usr/bin/env python

import argparse
import os
import sys

'''
Import a list of senators from a CSV database.  Print a list sorted by first name.

Senator contact details obtained from -
http://www.usglc.org/downloads/2013/07/Senate_Contact-List.xls
'''

class Senator:
    def __init__(self, first_name, last_name, party, state, address, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.party = party
        self.state = state
        self.address = address
        self.phone = phone

    def __str__(self):
        if self.party == 'D':
            party_str = "Democratic"
        else:
            party_str = "Repulibcan"

        out = "Senator {} {} from the {} party \n".format(self.first_name, self.last_name, party_str)
        out += "Address: {} \n".format(self.address)
        out += "State: {} \n".format(self.state)
        out += "Phone: {} \n ".format(self.phone)
        return out

def print_senators(senator_list):
    for s in senator_list:
        print s

def sort_senators(senator_list):
    sorted_senator_list = []
    name_list = []

    #gather names in a separate list
    for s in senator_list:
        name_list.append(s.first_name)

    name_list = sorted(name_list)
    print name_list

    #Add matching Senator objects in sorted_senator_list
    for n in name_list:
        for s in senator_list:
            if s.first_name == n:
                sorted_senator_list.append(s)

    #Using lambda
    #sorted_senator_list = sorted(senator_list, key = lambda s : s.first_name)

    return sorted_senator_list

'''
Main program
'''
def main():
    parser  = argparse.ArgumentParser()
    parser.add_argument("-d", "--dbfile", type=str, help="Path of the database file")
    args = parser.parse_args()
    
    if(len(sys.argv) == 1):
        print "Please provide the DB file name \n"
        sys.exit()

    if not (os.path.exists(args.dbfile)):
        print "The file {} does not exist, please try again\n".format(args.dbfile)
        sys.exit()

    dbfile = open(args.dbfile, "r")
    if not dbfile:
        print "Unable to open file {} \n".format(args.dbfile)
        sys.exit()

    print "Reading in Senator Database file ..{} \n".format(args.dbfile)

    senator_list = []

    #ignore the header row
    header_row = dbfile.readline()

    for line in dbfile:
        #print line
        fields = line.split(',')
        #print fields
        s = Senator(fields[0], fields[1], fields[2], fields[3], fields[4], fields[5])
        #print s
        senator_list.append(s)

    dbfile.close()

    print "Unsorted senator list\n"
    print_senators(senator_list)

    sorted_list = sort_senators(senator_list)

    print "Sorted senator list\n"
    print_senators(sorted_list)

if __name__ == '__main__':
    main()
