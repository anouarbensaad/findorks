import requests
import re
import argparse
import os
import sys
from common.banner import banner
from common.colors import run,W,end,good,bad,que,info

banner()

def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg + W)
    sys.exit()

def parse_args():
        parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -u google.com")
        parser.error = parser_error
        parser._optionals.title = "\nOPTIONS"
        parser.add_argument('-D', '--dorks', help='search webs with dorks', dest='dorks' , type=str)
        parser.add_argument('-o', '--output', help='specify output directory',required=False)
        parser.add_argument('-n', '--number-pages', help='search dorks number page limit', dest='numberpage' , type=int)
        parser.add_argument('-l','--dork-list', help='list names of dorks exploits',dest='dorkslist',
                choices=['wordpress', 'prestashop','joomla','lokomedia','drupal','all']) 
        return parser.parse_args()

if __name__ == "__main__":
        #numberpage
        numberpage = args.numberpage or 1  
        output_dir = args.output or 'logs'
        if not os.path.exists(output_dir): # if the directory doesn't exist
                os.mkdir(output_dir) # create a new directory
        args = parse_args()        
        dorks = args.dorks
        dorkslist = args.dorkslist
        if dorks:
                headers = {
                'host' : 'google.com',
                'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',}
                from modules.dorksExplorer import (searchengine,getdorksbyname,wp_contentdorks)
                searchengine(dorks,headers,output_dir,numberpage)
        if dorkslist == 'all':
                from modules.dorksListing import dorkslist as listall
                listall()
        if dorkslist == 'wordpress':
                from modules.dorksListing import wp_dorkTable as listwp
                listwp()
        if dorkslist == 'joomla':
                from modules.dorksListing import joo_dorkTable as listjoo
                listjoo()
        if dorkslist == 'prestashop':
                from modules.dorksListing import ps_dorkTable as listps
                listps()
        if dorkslist == 'lokomedia':
                from modules.dorksListing import loko_dorkTable as listlm
                listlm()
        if dorkslist == 'drupal':
                from modules.dorksListing import dru_dorkTable as listdru
                listdru()