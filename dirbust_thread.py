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
    print(G + "𝟐𝟎𝟎 𝐄𝐧𝐝𝐩𝐨𝐢𝐧𝐭𝐬 𝐢𝐧 𝐆𝐫𝐞𝐞𝐧")
    print(B + "ℚ𝕦𝕖𝕤𝕥𝕚𝕠𝕟𝕒𝕓𝕝𝕖 𝕖𝕟𝕕𝕡𝕠𝕚𝕟𝕥𝕤 𝕚𝕟 𝔹𝕝𝕦𝕖")
    print(Y + "Rᴇᴅɪʀᴇᴄᴛ Eɴᴅᴘᴏɪɴᴛs ɪɴ Yᴇʟʟᴏᴡ")
    print(R + "𝓥𝓮𝓻𝓫𝓸𝓼𝓮 𝓸𝓹𝓽𝓲𝓸𝓷𝓼 𝓲𝓷 𝓡𝓮𝓭")
    print(G + '  ')
    print(G + '  ')

real_endpoints = []
failed_endpoints = []
redirect_endpoints = []
questionable_endpoints = []


def send_request(url, i, headers):
    response = requests.get(url, headers=headers)
    if response.ok:
        real_endpoints.append(
            f"Endpoint: {url} \n Status Code: {response.status_code} \n Wordlist Line {i} \n")
        print(
            G + '[✅] Definite endpoint found: ' + ' URL 👉 {1}'.format(i, url) + '\n' +
            f'  Status Code: {response.status_code}' + '   [wordlist line {0}]:'.format(i) +
            Style.RESET_ALL)
    elif response.status_code in [201, 204, 202, 206, 301, 302, 304, 400, 401, 403, 407, 423, 429]:
        questionable_endpoints.append(
            f"Endpoint: {url} \n Status Code: {response.status_code} \n Wordlist Line {i} \n")
        print(
            B + '[🤔] Questionable endpoint:' + ' URL 👉 {1}'.format(i, url) + '\n' +
            f'  Status Code: {response.status_code}' +
            '   [wordlist line {0}]:'.format(i) +
            Style.RESET_ALL)
    elif response.is_permanent_redirect:
        redirect_endpoints.append(
            f"Endpoint: {url} \n Status Code: {response.status_code} \n Wordlist Line {i} \n")
        print(
            Y + '[🏴‍☠️] Redirect Endpoint:' + ' URL 👉 {1}'.format(i, url) + '\n' +
            f'  Status Code: {response.status_code}' +
            '   [wordlist line {0}]:'.format(i) +
            Style.RESET_ALL)
    elif not response.ok:
        if args.verbose:
            failed_endpoints.append(
                f"Endpoint: {url} \n Status Code: {response.status_code} \n  Wordlist Line {i} \n")
            print(
                R + '[🚫] Failed endpoint found:  ' +
                    ' URL 👉 {1}'.format(i, url) + '\n'
                f'  Status Code: {response.status_code}' +
                '   [wordlist line {0}]:'.format(i) +
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


    # Create a new thread for each request and start it
    t = threading.Thread(target=send_request, args=(url, i+1, headers))
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
        f.write('[✅] Real Endpoints:\n')
        f.write("\n")
        f.write('\n'.join(real_endpoints))
        f.write("\n")
        f.write('[🤔] Questionable Endpoints:\n')
        f.write("\n")
        f.write('\n'.join(questionable_endpoints))
        f.write("\n")
        if redirect_endpoints:
            f.write('\n\n[🏴‍☠️] Redirected Endpoints:\n')
            f.write("\n")
            f.write('\n'.join(redirect_endpoints))
            f.write("\n")
        if args.verbose:
            f.write('\n\n[X] Failed Endpoints:\n')
            f.write("\n")
            f.write('\n'.join(failed_endpoints))
            f.write("\n")
        print(Y + f'[✍] Results written to output file: {args.output}')