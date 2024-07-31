#!/usr/bin/python3

from threading import *
from argparse import *
from requests import *
from time import time,sleep
import sys
subdomain_list = []


def get_args():
        parser = ArgumentParser(description="A Python Based Subdomain BruteForcer", usage="./%(prog)s domain.com", epilog="./%(prog)s doamin.com -w wordlist -t 10")
        parser.add_argument(dest='domain', metavar='Domain', help="Domain Name")
        parser.add_argument('-w', '--wordlist', dest='wordlist', help="words for tools", metavar="wordlists", default='word.txt', type=FileType('r'))
        parser.add_argument('-t', '--thread', dest='threads',metavar='threads',type=int, help="threads number", default=500)
        parser.add_argument('-v', '--verbose', dest='verbose', help="verbose the output", action='store_true')
        parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0' )
        args = parser.parse_args()
        return args

def prepare_words():
        words = argum.wordlist.read().split()
        # uniqs = set()
        for word in words:
            yield word
            
        

def get_domain():
        
        while True:
            try:
                domain_word = next(word)
                url = f"https://{domain_word}.{argum.domain}"
                req  = get(url, timeout=5)
                if req.status_code == 200:
                    subdomain_list.append(url)
                    if argum.verbose:
                        print(url)
            except (ConnectionError,ReadTimeout):
                continue
            except StopIteration:
                break
           

def prepare_thread():
        thread_list = []
        for _ in range(argum.threads):
            thread_list.append(Thread(target=get_domain))
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()

if __name__ == '__main__':

    argum = get_args()
    word = prepare_words()
    print("Starting......")
    start_time = time()
    prepare_thread()
    end_time = time()
    print("Subdomain_Found - \n","\n".join(i for i in subdomain_list))
    print(f"TIme Taken - {round(end_time-start_time,2)}")
