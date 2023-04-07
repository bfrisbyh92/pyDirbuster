import argparse
import requests
import os
from colorama import Fore, Style, Back


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

    banner = Back.BLACK + Fore.RED + '''
█▀█ █▄█ █▀▄ █ █▀█ █▄▄ █░█ █▀ ▀█▀ █▀▀ █▀█
█▀▀ ░█░ █▄▀ █ █▀▄ █▄█ █▄█ ▄█ ░█░ ██▄ █▀▄
    '''
    github = Fore.WHITE + Back.BLACK + '''
ᴳⁱᵗʰᵘᵇ⠘ h̳t̳t̳p̳s̳:̳/̳/̳g̳i̳t̳h̳u̳b̳.̳c̳o̳m̳/̳b̳f̳r̳i̳s̳b̳y̳h̳9̳2̳
    '''

    # Read wordlist file
    wordlist_path = os.path.abspath(args.wordlist)
    print(banner)
    print(Back.BLACK + Fore.GREEN +
          "S̅i̅m̅p̅l̅e̅ P̅y̅t̅h̅o̅n̅ D̅i̅r̅e̅c̅t̅o̅r̅y̅ B̅u̅s̅t̅i̅n̅g̅")
    print(github)
    with open(wordlist_path, 'r') as f:
        print(Fore.GREEN + Back.BLACK + "Reading Wordlist...")
        print(Back.BLACK + Fore.GREEN + "  ")
        wordlist = f.read().splitlines()
        print(Fore.GREEN + Back.BLACK + "𝟚𝟘𝟘 𝕊𝕥𝕒𝕥𝕦𝕤 𝔾𝕣𝕖𝕖𝕟")
        print(Fore.YELLOW + Back.BLACK + "𝟛𝟘𝟘 𝕊𝕥𝕒𝕥𝕦𝕤 𝕐𝕖𝕝𝕝𝕠𝕨")
        print(Fore.BLUE + Back.BLACK + "4̲0̲0̲ S̲t̲a̲t̲u̲s̲ B̲l̲u̲e̲")
        print(Fore.RED + Back.BLACK + "5̶0̶0̶ S̶t̶a̶t̶u̶s̶ R̶e̶d̶")

    # Send requests
    possible_endpoints = []
    real_endpoints = []
    for i, word in enumerate(wordlist):
        if args.url.endswith('/'):
            url = args.url + word
        else:
            url = args.url + "/" + word
        response = requests.get(url)
        if response.status_code in [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]:
            real_endpoints.append(url)
            print(
                Fore.BLACK + Back.GREEN + '[+] 200 Status definite endpoint found \n line ({0}): {1}'.format(i+1, url))
        elif response.status_code in [301, 302, 303, 304, 307, 308]:
            possible_endpoints.append(url)
            print(
                Back.YELLOW + Fore.BLACK + '[~] 300 Status possible endpoint found \n line ({0}): {1}'.format(i+1, url))
        elif response.status_code in [401, 403]:
            possible_endpoints.append(url)
            print(
                Fore.WHITE + Back.BLUE + '[~] 400 Status restricted endpoint found \n line ({0}): {1}'.format(i+1, url))
        elif response.status_code in [400, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 451]:
            if args.verbose:
                print(
                    Fore.WHITE + Back.RED + '[-] 500 Status Non-existent endpoint \n line ({0}): {1}'.format(i+1, url))
        elif response.status_code in [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]:
            if args.verbose:
                print(
                    Back.RED + Fore.WHITE + '[-] Possible server error \n line ({0}):{1}'.format(i+1, url))

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
