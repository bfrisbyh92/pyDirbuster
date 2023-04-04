import argparse
import requests
import os
from colorama import Fore, Style


def main():
    # Parse user input
    parser = argparse.ArgumentParser(description='Directory brute forcer')
    parser.add_argument('-w', '--wordlist', type=str,
                        required=True, help='Path to wordlist file')
    parser.add_argument('-u', '--url', type=str,
                        required=True, help='Target URL')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print all response codes')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    args = parser.parse_args()

    # Read wordlist file
    wordlist_path = os.path.abspath(args.wordlist)
    with open(wordlist_path, 'r') as f:
        wordlist = f.read().splitlines()

    # Send requests
    possible_endpoints = []
    real_endpoints = []
    for i, word in enumerate(wordlist):
        url = args.url + '/' + word
        response = requests.get(url)
        if response.status_code in [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]:
            real_endpoints.append(url)
            print(
                Fore.GREEN + '[+] Possible 200 Status endpoint found ({0}): {1}'.format(i+1, url))
        elif response.status_code in [301, 302, 303, 304, 307, 308]:
            possible_endpoints.append(url)
            print(
                Fore.YELLOW + '[~] Possible 300 Status endpoint found ({0}): {1}'.format(i+1, url))
        elif response.status_code in [401, 403]:
            possible_endpoints.append(url)
            print(
                Fore.BLUE + '[~] Possible 400 Status endpoint found ({0}): {1}'.format(i+1, url))
        elif response.status_code in [400, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 451]:
            if args.verbose:
                print(
                    Fore.RED + '[-] 500 Status Non-existent endpoint ({0}): {1}'.format(i+1, url))
        elif response.status_code in [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]:
            if args.verbose:
                print(
                    Fore.RED + '[-] Possible server error ({0}): {1}'.format(i+1, url))

    # Write results to output file
    if args.output:
        with open(args.output, 'w') as f:
            f.write('[+] Real endpoints:\n')
            f.write('\n'.join(real_endpoints))
            f.write('\n\n[~] Possible endpoints:\n')
            f.write('\n'.join(possible_endpoints))
            print(Fore.YELLOW +
                  '[*] Results written to output file: {0}'.format(args.output))


if __name__ == '__main__':
    main()
