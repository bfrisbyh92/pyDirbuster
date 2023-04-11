import argparse
import requests
import os
from colorama import Fore, Style, Back
from user_agent import generate_user_agent


def main():
    # Parse user input
    parser = argparse.ArgumentParser(description='Directory brute forcer')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to wordlist file')
    parser.add_argument('-u', '--url', type=str,
                        required=True, help='Target URL')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print all response codes')
    parser.add_argument("-ua", "--useragent", action="store_true",
                        help="Randomize User Agent")
    args = parser.parse_args()
    # print(args)

    G = Fore.GREEN + Back.BLACK + Style.BRIGHT 
    Y = Fore.YELLOW + Back.BLACK + Style.BRIGHT 
    B = Fore.BLUE + Back.BLACK + Style.BRIGHT 
    R = Fore.RED + Back.BLACK + Style.BRIGHT 
    C = Fore.CYAN + Back.BLACK + Style.BRIGHT 
    gh = Fore.LIGHTGREEN_EX + Back.BLACK + Style.BRIGHT 
    
    banner = '''
 █▀█ █▄█ █▀▄ █ █▀█ █▄▄ █░█ █▀ ▀█▀ █▀▀ █▀█
 █▀▀ ░█░ █▄▀ █ █▀▄ █▄█ █▄█ ▄█ ░█░ ██▄ █▀▄
     '''
    github = '''
 ᴳⁱᵗʰᵘᵇ⠘ h̳t̳t̳p̳s̳:̳/̳/̳g̳i̳t̳h̳u̳b̳.̳c̳o̳m̳/̳b̳f̳r̳i̳s̳b̳y̳h̳9̳2̳
    '''
    # Wordlist Checks
    if args.wordlist:
        wordlist = args.wordlist
    else:
        wordlist = input("No wordlist specified, Please enter wordlist location:  \n ")
    print(wordlist)
    # Read wordlist file
    wordlist_path = os.path.abspath(wordlist)
    
    print(R + banner)
    print(G + 
          "S̅i̅m̅p̅l̅e̅ P̅y̅t̅h̅o̅n̅ D̅i̅r̅e̅c̅t̅o̅r̅y̅ B̅u̅s̅t̅i̅n̅g̅")
    print(gh + github)
    print(Fore.LIGHTWHITE_EX + f"Wordlist: \n {wordlist}")
    print(Fore.LIGHTWHITE_EX +  f"URL: \n {args.url}")
    print(Fore.LIGHTWHITE_EX +  f"Output: \n {args.output}")
    print(Fore.LIGHTWHITE_EX +  f"Verbose: \n {args.verbose}")
    with open(wordlist_path, 'r') as f:
        print(G + "Reading Wordlist...")
        print(G + "  ")
        wordlist = f.read().splitlines()
        print(G + "𝟚𝟘𝟘 𝕊𝕥𝕒𝕥𝕦𝕤 𝔾𝕣𝕖𝕖𝕟")
        print(Y + "𝟛𝟘𝟘 𝕊𝕥𝕒𝕥𝕦𝕤 𝕐𝕖𝕝𝕝𝕠𝕨")
        print(B + "4̲0̲0̲ S̲t̲a̲t̲u̲s̲ B̲l̲u̲e̲")
        print(R + "5̶0̶0̶ S̶t̶a̶t̶u̶s̶ R̶e̶d̶")
        print(G + '  ')
        print(G + '  ')

    # Send requests
    possible_endpoints = []
    real_endpoints = []
    for i, word in enumerate(wordlist):
        if args.url.endswith('/'):
            url = args.url + word
        else:
            url = args.url + "/" + word
            # If -ua arg specified, we randomize the User-Agent
        if args.useragent:
            headers = {'User-Agent': generate_user_agent()}
            # print(headers)
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url)
        if response.status_code in [200, 201, 203, 204, 205, 206, 208, 226]:
            real_endpoints.append(url)
            print(
                G + '[+] Definite endpoint found \n line ({0}): {1}'.format(i+1, url))
        elif response.status_code in [300, 301, 302, 303, 307, 308, 401, 402, 403]:
            possible_endpoints.append(url)
            print(
                Y + '[~] Possible endpoint found \n line ({0}): {1}'.format(i+1, url))
        elif response.status_code in [404]:
            if args.verbose:
                print(
                    R + '[~] 404 Response, Page does not exists \n line ({0}): {1}'.format(i+1, url))
        elif response.status_code in [400, 405, 406, 408, 410, 411, 412, 413, 414, 415, 416, 417]:
            if args.verbose:
                print(
                    Fore.WHITE + Back.RED + '[-] Non-existent or error endpoint \n line ({0}): {1}'.format(i+1, url))
        elif response.status_code in [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 599]:
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
            print(Y + f'[*] Results written to output file: {args.output}')


if __name__ == '__main__':
    main()
