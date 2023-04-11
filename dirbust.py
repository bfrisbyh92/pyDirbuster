# import argparse
# import requests
# import os
# from colorama import Fore, Style, Back
# from user_agent import generate_user_agent


# def main():
#     # Parse user input
#     parser = argparse.ArgumentParser(description='Directory Brute Forcer')
#     parser.add_argument('-w', '--wordlist', type=str,
#                         help='Path to wordlist file')
#     parser.add_argument('-u', '--url', type=str, help='Target URL')
#     parser.add_argument('-v', '--verbose', action='store_true',
#                         help='Print all response codes')
#     parser.add_argument('-o', '--output', type=str, help='Output file path')
#     parser.add_argument("-ua", "--useragent", action="store_true",
#                         help="Randomize User Agent")
#     args = parser.parse_args()

#     G = Fore.GREEN + Back.BLACK
#     Y = Fore.YELLOW + Back.BLACK
#     B = Fore.BLUE + Back.BLACK
#     R = Fore.RED + Back.BLACK
#     C = Fore.CYAN + Back.BLACK
#     gh = Fore.WHITE + Back.BLACK

#     banner = '''
# █▀█ █▄█ █▀▄ █ █▀█ █▄▄ █░█ █▀ ▀█▀ █▀▀ █▀█
# █▀▀ ░█░ █▄▀ █ █▀▄ █▄█ █▄█ ▄█ ░█░ ██▄ █▀▄
#     '''
#     github = '''
# ᴳⁱᵗʰᵘᵇ⠘ h̳t̳t̳p̳s̳:̳/̳/̳g̳i̳t̳h̳u̳b̳.̳c̳o̳m̳/̳b̳f̳r̳i̳s̳b̳y̳h̳9̳2̳
#     '''

#     # Read wordlist file
#     if args.wordlist:
#         wordlist = args.wordlist
#     else:
#         wordlist = input(C + "Enter wordlist location:  ")

#     # Read wordlist file
#     wordlist_path = os.path.abspath(args.wordlist)

#     if args.url:
#         url = args.url
#     else:
#         url = input(C + "Please enter URL:  ")
#     if args.output:
#         output = args.output
#     else:
#         output = input(C + "Enter output path:  ")
#     if args.verbose:
#         verbose = args.verbose
#     else:
#         verbose = input(Y + "Verbose? (y or n) \n")
#         if verbose == 'y':
#             verbose = True

#     print(R + banner)
#     print(G +
#           "S̅i̅m̅p̅l̅e̅ P̅y̅t̅h̅o̅n̅ D̅i̅r̅e̅c̅t̅o̅r̅y̅ B̅u̅s̅t̅i̅n̅g̅")
#     print(gh + github)
#     print(C + f"Wordlist: \n {wordlist}")
#     print(C + f"URL: \n {url}")
#     print(C + f"Output: \n {output}")
#     print(C + f"Verbose: \n {args.verbose}")
#     with open(wordlist_path, 'r') as f:
#         print(G + "Reading Wordlist...")
#         print(G + "  ")
#         wordlist = f.read().splitlines()
#         print(G + "𝟚𝟘𝟘 𝕊𝕥𝕒𝕥𝕦𝕤 𝔾𝕣𝕖𝕖𝕟")
#         print(Y + "𝟛𝟘𝟘 𝕊𝕥𝕒𝕥𝕦𝕤 𝕐𝕖𝕝𝕝𝕠𝕨")
#         print(B + "4̲0̲0̲ S̲t̲a̲t̲u̲s̲ B̲l̲u̲e̲")
#         print(R + "5̶0̶0̶ S̶t̶a̶t̶u̶s̶ R̶e̶d̶")
#         print(G + '  ')
#         print(G + '  ')

#     # Send requests
#     possible_endpoints = []
#     real_endpoints = []
#     for i, word in enumerate(wordlist):
#         if url.endswith('/'):
#             url = url + word
#         else:
#             url = url + "/" + word
#         if args.useragent:
#             headers = {'User-Agent': generate_user_agent()}
#             response = requests.get(url, headers=headers)
#         else:
#             response = requests.get(url)
#         if response.status_code in [200, 201, 203, 204, 205, 206, 208, 226]:
#             real_endpoints.append(url)
#             print(
#                 G + '[+] Definite endpoint found \n line ({0}): {1}'.format(i+1, url))
#         elif response.status_code in [300, 301, 302, 303, 307, 308, 401, 402, 403]:
#             possible_endpoints.append(url)
#             print(
#                 Y + '[~] Possible endpoint found \n line ({0}): {1}'.format(i+1, url))
#         elif response.status_code in [404]:
#             if args.verbose:
#                 print(
#                     C + '[~] 404 Response, Page does not exists \n line ({0}): {1}'.format(i+1, url))
#         elif response.status_code in [400, 405, 406, 408, 410, 411, 412, 413, 414, 415, 416, 417]:
#             if args.verbose:
#                 print(
#                     Fore.WHITE + Back.RED + '[-] Non-existent or error endpoint \n line ({0}): {1}'.format(i+1, url))
#         elif response.status_code in [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 599]:
#             if args.verbose:
#                 print(
#                     Back.RED + Fore.WHITE + '[-] Possible server error \n line ({0}):{1}'.format(i+1, url))

#     # Write results to output file
#         with open(output, 'w') as f:
#             f.write(banner)
#             f.write(github)
#             f.write('\n')
#             f.write('\n')
#             f.write('[+] Real endpoints:\n')
#             f.write('\n')
#             f.write('\n'.join(real_endpoints))
#             f.write('\n')
#             f.write('\n\n[~] Possible endpoints:\n')
#             f.write('\n'.join(possible_endpoints))
#             f.write('\n')

# print(Fore.WHITE + Back.BLACK + '[+] Results written to output file')


# if __name__ == '__main__':
#     main()

import argparse
import requests
import os
from colorama import Fore, Style, Back
from user_agent import generate_user_agent


def main():
    # Parse user input
    parser = argparse.ArgumentParser(description='Directory brute forcer')
    parser.add_argument('-w', '--wordlist', type=str,
                        required=True, help='Path to wordlist file')
    parser.add_argument('-u', '--url', type=str,
                        required=True, help='Target URL')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print all response codes')
    parser.add_argument("-ua", "--useragent", action="store_true",
                        help="Randomize User Agent")
    args = parser.parse_args()
    # print(args)

    G = Fore.GREEN + Back.BLACK
    Y = Fore.YELLOW + Back.BLACK
    B = Fore.BLUE + Back.BLACK
    R = Fore.RED + Back.BLACK
    C = Fore.CYAN + Back.BLACK
    gh = Fore.LIGHTGREEN_EX + Back.BLACK
    
    banner = '''
 █▀█ █▄█ █▀▄ █ █▀█ █▄▄ █░█ █▀ ▀█▀ █▀▀ █▀█
 █▀▀ ░█░ █▄▀ █ █▀▄ █▄█ █▄█ ▄█ ░█░ ██▄ █▀▄
     '''
    github = '''
 ᴳⁱᵗʰᵘᵇ⠘ h̳t̳t̳p̳s̳:̳/̳/̳g̳i̳t̳h̳u̳b̳.̳c̳o̳m̳/̳b̳f̳r̳i̳s̳b̳y̳h̳9̳2̳
    '''

    # Read wordlist file
    wordlist_path = os.path.abspath(args.wordlist)
    print(R + banner)
    print(G +
          "S̅i̅m̅p̅l̅e̅ P̅y̅t̅h̅o̅n̅ D̅i̅r̅e̅c̅t̅o̅r̅y̅ B̅u̅s̅t̅i̅n̅g̅")
    print(gh + github)
    print(Fore.LIGHTWHITE_EX + f"Wordlist: \n {args.wordlist}")
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
