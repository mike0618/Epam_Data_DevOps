import requests
from tqdm import tqdm
from os import path
import re


def download_file():
    url = 'http://www.almhuette-raith.at/apache-log/access.log'
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('Content-Length'))
    block_size = 1024
    progressbar = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open('access.log', 'wb') as file:
        for data in response.iter_content(block_size):
            progressbar.update(len(data))
            file.write(data)
    progressbar.close()
    if total_size != 0 and progressbar.n != total_size:
        print('Error, downloading went wrong')
    else:
        print(' The file downloaded successfully\n')


def task8():
    if not path.isfile('access.log'):
        download_file()

    browsers = {}
    browsers_ip = {}
    requests_per_month = {}
    ip_data_amounts = {}
    with open('access.log') as file:
        for strn in tqdm(file):
            lst = strn.split('"')
            if len(lst) < 6:
                continue
            # Part 1
            browser = lst[5]
            ip_n_date = lst[0]
            ipaddr = ip_n_date[:ip_n_date.index(' ')]
            browsers[browser] = browsers.get(browser, 0) + 1
            if browser in browsers_ip:
                browsers_ip.get(browser).add(ipaddr)
            else:
                browsers_ip[browser] = {ipaddr}
            # Part 2
            if ipaddr == '216.244.66.230':
                month_n_year = ip_n_date[ip_n_date.index('/') + 1:ip_n_date.index(':')].replace('/', ' ')
                requests_per_month[month_n_year] = requests_per_month.get(month_n_year, 0) + 1
            # Part 3
            found = re.search(r"\" \d{3} \d* \"", strn)
            if found:
                amount = int(found.group().strip('" ')[4:])
                ip_data_amounts[ipaddr] = ip_data_amounts.get(ipaddr, 0) + amount

        frequent_browser = max(browsers, key=browsers.get)
        print('\n1. What is the most frequent browser?')
        print('The most frequent browser just in file is:', frequent_browser)
        # print('IPs the most frequent browser connected to:', browsers_ip.get(frequent_browser))
        print('The most frequent browser by unique IPs is:', max(browsers_ip, key=browsers_ip.get))
        print('\n2. Show number of requests per month for ip 216.244.66.230')
        for k, v in requests_per_month.items():
            print(f'{k} {v:4.0f} requests')
        print('\n3. Show total amount of data which server has provided for each unique ip')
        ip_data_amounts = sorted(ip_data_amounts.items(), key=lambda item: item[1], reverse=True)
        with open('ip_data_amounts.log', 'w') as f:
            for i, (k, v) in enumerate(ip_data_amounts):
                s = f'{v:12.0f} bytes for {k}'
                f.write(s + '\n')
                if i < 20:  # In order to prevent console overwhelming
                    print(s)


if __name__ == '__main__':
    task8()
