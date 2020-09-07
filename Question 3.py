
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Folder',
                       metavar='path',
                       type=str,
                       help='the path to list')


my_parser.add_argument('-o','--order',
                       metavar='order',
                       type=str,default='Ascending',
                       help='Script Order')  

my_parser.add_argument('-f','--Filename',
                       metavar='filename',
                       type=str,default='all',
                       help='Name of file name that will be running')  
my_parser.add_argument('-out',"--output", help = "output filename")

args = my_parser.parse_args()
input_path = args.Folder

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()
if args.Filename=='all':
    if args.order=='Ascending':
        
        for line in reversed(os.listdir(input_path)):
            print(line)

    elif args.order=='Descending':
        for line in (os.listdir(input_path)):
            print(line)
else:
    for line in reversed(os.listdir(input_path)):
        if args.Filename==line:
            print(line)





print('outputfile:', args.output)
print('okay')