import threading
from colorama import Back, Fore, Style
import requests
import os
import argparse
from user_agent import generate_user_agent

# Parse user input
parser = argparse.ArgumentParser(description='PyDirbuster')
parser.add_argument('-w', '--wordlist', type=str,
                    help='Path to wordlist file')
parser.add_argument('-u', '--url', type=str, help='Target URL')
parser.add_argument('-o', '--output', type=str, help='Output file path')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Print all response codes')
parser.add_argument("-ua", "--useragent", action="store_true",
                    help="Randomize User Agent")
args = parser.parse_args()

# Wordlist Checks
if args.wordlist:
    wordlist = args.wordlist
else:
    wordlist = 'assets/default_wordlist.txt'
    # Read wordlist file
wordlist_path = os.path.abspath(wordlist)

# Colors
G = Fore.LIGHTGREEN_EX + Back.BLACK + Style.BRIGHT
Y = Fore.YELLOW + Back.BLACK + Style.BRIGHT
B = Fore.BLUE + Back.BLACK + Style.BRIGHT
R = Fore.LIGHTRED_EX + Back.BLACK + Style.BRIGHT
C = Fore.CYAN + Back.BLACK + Style.BRIGHT
P = Fore.LIGHTMAGENTA_EX + Back.BLACK + Style.BRIGHT
gh = Fore.LIGHTRED_EX + Back.BLACK + Style.BRIGHT

banner = '''
 █▀█ █▄█ █▀▄ █ █▀█ █▄▄ █░█ █▀ ▀█▀ █▀▀ █▀█
 █▀▀ ░█░ █▄▀ █ █▀▄ █▄█ █▄█ ▄█ ░█░ ██▄ █▀▄ 👀👀
 ╚════════════☆═══╝╚════════════☆═══╝
     '''
github = '''
 ᴳⁱᵗʰᵘᵇ⠘ 👉 h̳t̳t̳p̳s̳:̳/̳/̳g̳i̳t̳h̳u̳b̳.̳c̳o̳m̳/̳b̳f̳r̳i̳s̳b̳y̳h̳9̳2̳
    '''
print(R + banner)
print(G +
      "S̅i̅m̅p̅l̅e̅ P̅y̅t̅h̅o̅n̅ D̅i̅r̅e̅c̅t̅o̅r̅y̅ B̅u̅s̅t̅i̅n̅g̅")
print(G + github)
print(Fore.LIGHTWHITE_EX + f"Wordlist: \n {wordlist}")
print(Fore.LIGHTWHITE_EX + f"URL: \n {args.url}")
print(Fore.LIGHTWHITE_EX + f"Output: \n {args.output}")
print(Fore.LIGHTWHITE_EX + f"Verbose: \n {args.verbose}")

# Open the wordlist and do stuff
with open(wordlist_path, 'r') as f:
    wordlist = f.read().splitlines()
    num_lines = len(wordlist)  # Get the number of lines in the wordlist
    print(G + "   ")
    print(C + f"Reading {wordlist_path}")
    # Print the number of lines in the wordlist
    print("Wordlist size:  " + str(num_lines) + " lines")
    print(G + "  ")
    print(G + "𝔻𝕖𝕗𝕚𝕟𝕚𝕥𝕖 𝔼𝕟𝕕𝕡𝕠𝕚𝕟𝕥𝕤 𝕚𝕟 𝔾𝕣𝕖𝕖𝕟")
    print(B + "𝐏𝐨𝐬𝐬𝐢𝐛𝐥𝐞 𝐞𝐧𝐝𝐩𝐨𝐢𝐧𝐭 𝐢𝐧 𝐁𝐥𝐮𝐞")
    print(R + "𝑫𝒐𝒆𝒔 𝒏𝒐𝒕 𝒆𝒙𝒊𝒔𝒕 𝒊𝒏 𝑹𝒆𝒅")
    print(P + "𝔸𝕟𝕪 𝕖𝕣𝕣𝕠𝕣 𝕔𝕠𝕕𝕖 𝕚𝕟 ℙ𝕚𝕟𝕜")
    print(G + '  ')
    print(G + '  ')

real_endpoints = []
possible_endpoints = []


def send_request(url, wordlist_line):
    response = requests.get(url)
    if response.status_code in [200, 201, 203, 204, 205, 206, 208, 226]:
        real_endpoints.append(url)
        print(
            G + '[✅] Definite endpoint found \n ' +
            R + '[wordlist line {0}]:'.format(wordlist_line) +
            G + ' URL 👉 {1}'.format(wordlist_line, url) +
            Style.RESET_ALL)
    elif response.status_code in [300, 301, 302, 303, 307, 308, 401, 402, 403]:
        possible_endpoints.append(url)
        print(
            B + '[🤔] Possible endpoint found \n ' +
            R + '[wordlist line {0}]:'.format(wordlist_line) +
            B + ' URL 👉 {1}'.format(wordlist_line, url) +
            Style.RESET_ALL)
    elif response.status_code in [404]:
        if args.verbose:
            print(
                R + '[🚫] 404 Response, Page does not exist \n ' +
                B + '[wordlist line {0}]:'.format(wordlist_line) +
                R + ' URL 👉 {1}'.format(wordlist_line, url) +
                Style.RESET_ALL)
    elif response.status_code in [400, 405, 406, 408, 410, 411, 412, 413, 414, 415, 416, 417, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 599]:
        if args.verbose:
            print(
                P + '[🏴‍☠️] Non-existent or error \n ' +
                B + '[wordlist line {0}]:'.format(wordlist_line) +
                P + ' URL 👉 {1}'.format(wordlist_line, url) +
                Style.RESET_ALL)


# Use threading to send requests concurrently
threads = []
for i, word in enumerate(wordlist):
    if not args.url:
        args.url = input(B + "Enter URL:  \n")
        print(G + " ")
    if args.url.endswith('/'):
        url = args.url + word
    else:
        url = args.url + "/" + word

    # If -ua arg specified, we randomize the User-Agent
    if args.useragent:
        headers = {'User-Agent': generate_user_agent()}
        # print(headers) to check user agent
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url)

    # Create a new thread for each request and start it
    t = threading.Thread(target=send_request, args=(url, i+1))
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

# Write results to output file
if args.output:
    with open(args.output, 'w') as f:
        f.write(banner)
        f.write(github)
        f.write("\n")
        f.write("\n")
        f.write('[✅] Real endpoints:\n')
        f.write("\n")
        f.write('\n'.join(real_endpoints))
        f.write("\n")
        f.write('\n\n[🤔] Possible endpoints:\n')
        f.write("\n")
        f.write('\n'.join(possible_endpoints))
        f.write("\n")
        print(Y + f'[✍] Results written to output file: {args.output}')
