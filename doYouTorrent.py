from bs4 import BeautifulSoup
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print("                                                                   /$$                                                 ")
print("                                                                  |__/                                                 ")
print(" /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$         /$$$$$$   /$$$$$$  /$$ /$$    /$$ /$$$$$$   /$$$$$$$ /$$   /$$         ")
print("| $$  | $$ /$$__  $$| $$  | $$ /$$__  $$       /$$__  $$ /$$__  $$| $$|  $$  /$$/|____  $$ /$$_____/| $$  | $$         ")
print("| $$  | $$| $$  \\ $$| $$  | $$| $$  \\__/      | $$  \\ $$| $$  \\__/| $$ \\  $$/$$/  /$$$$$$$| $$      | $$  | $$         ")
print("| $$  | $$| $$  | $$| $$  | $$| $$            | $$  | $$| $$      | $$  \\  $$$/  /$$__  $$| $$      | $$  | $$         ")
print("|  $$$$$$$|  $$$$$$/|  $$$$$$/| $$            | $$$$$$$/| $$      | $$   \\  $/  |  $$$$$$$|  $$$$$$$|  $$$$$$$         ")
print(" \\____  $$ \\______/  \\______/ |__/            | $$____/ |__/      |__/    \\_/    \\_______/ \\_______/ \\____  $$         ")
print(" /$$  | $$                                    | $$                                                   /$$  | $$         ")
print("|  $$$$$$/                                    | $$                                                  |  $$$$$$/         ")
print(" \\______/                                     |__/                                                   \\______/          ")


tempAuth = '27eea1cd-e644-4b7b-bebe-38010f55dab3'
def getBlacklist(ip):
    headerss={
    'authority': 'mxtoolbox.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
    'content-type': 'application/json; charset=utf-8',
     'cookie': (
        '_mxt_s=anon; MxVisitorUID=242d8b9d-52a8-4463-a4c4-259bff69d475; '
        '_mx_vtc=AB-634A=Control; _mx_reg_code=prob_blacklist; '
        '_mxt_u={"UserId":"00000000-0000-0000-0000-000000000000","UserName":null,"FirstName":null,'
        '"IsAdmin":false,"IsMasquerade":false,"IsPaidUser":false,"IsLoggedIn":false,'
        '"MxVisitorUid":"242d8b9d-52a8-4463-a4c4-259bff69d475","TempAuthKey":"%s",'
        '"IsPastDue":false,"BouncedEmailOn":null,"NumDomainHealthMonitors":0,"NumDisabledMonitors":0,'
        '"XID":null,"AGID":"00000000-0000-0000-0000-000000000000","Membership":{"MemberType":"Anonymous"},'
        '"CognitoSub":"00000000-0000-0000-0000-000000000000","HasBetaAccess":false,"IsOnTrial":false,'
        '"PermissionType":0}; ki_r=; ki_t=1730089487954%%3B1730089487954%%3B1730089497194%%3B1%%3B2'
        ) % tempAuth,
    'priority': 'u=1, i',
    'referer': 'https://mxtoolbox.com/SuperTool.aspx',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tempauthorization': f'{tempAuth}',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }
    link = f'https://mxtoolbox.com/api/v1/Lookup?command=blacklist&argument={ip}&resultIndex=9&disableRhsbl=true&format=2'
    req = requests.get(link, headers=headerss)
    soup = BeautifulSoup(req.text, 'html.parser')

    table_names = soup.find_all('td', class_='table-column-Name')

    # Extract and print the text content from each 'table-column-Name' <td>
    for name in table_names:
        table_name = name.get_text(strip=True)
        print(f'{bcolors.FAIL}[blackList>] {bcolors.ENDC}{table_name}')

while(True):

    ip = input('[ip >] ')
    link = f'https://iknowwhatyoudownload.com/en/peer/?ip={ip}'
    payload={'ip':ip}

    headerss = {
        'authority': 'iknowwhatyoudownload.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
        'referer': f'https://iknowwhatyoudownload.com/en/peer/?ip={ip}',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }


    req = requests.get(link, headers=headerss)
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')
        rows = soup.select('table.table-striped tbody tr')

        for row in rows:
            category = row.find(class_='category-column').get_text(strip=True) if row.find(class_='category-column') else None
            torrent_div = row.find(class_='torrent_files')
            if torrent_div:
                torrent_text = torrent_div.get_text(strip=True)
                if (category == 'XXX'):
                    print(f'{bcolors.OKGREEN}[>]{bcolors.ENDC}{bcolors.FAIL} {torrent_text} || {category}{bcolors.ENDC}')
                else:
                    print(f'{bcolors.OKGREEN}[>]{bcolors.ENDC}{bcolors.ENDC} {torrent_text} || {category}')
            else:
                print('nothing found')

    else:
        print('couldn\'t connect')

    runScan = input('do you want to run additional ip tests (whois||ipBlackList) [(y/N)>] ')
    if (runScan.lower() == 'y'):
        runScanLink = f'https://freeipapi.com/api/json/{ip}'
        try:
            response = requests.get(runScanLink).json()
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} IP Version: {response['ipVersion']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} IP Address: {response['ipAddress']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Latitude: {response['latitude']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Longitude: {response['longitude']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Country Name: {response['countryName']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Country Code: {response['countryCode']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Time Zone: {response['timeZone']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Zip Code: {response['zipCode']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} City Name: {response['cityName']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Region Name: {response['regionName']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Is Proxy: {response['isProxy']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Continent: {response['continent']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Continent Code: {response['continentCode']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Currency Code: {response['currency']['code']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Currency Name: {response['currency']['name']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Language: {response['language']}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} Time Zones:")
            for tz in response['timeZones']:
                print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC}  - {tz}")
            print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC} TLDs:")
            for tld in response['tlds']:
                print(f"{bcolors.WARNING}[whois>]{bcolors.ENDC}  - {tld}")
        except:
            print('something went wrong')
        
        getBlacklist(ip)