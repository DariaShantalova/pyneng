import re

def get_ip_from_cfg(file):
    result = {}
    with open(file) as src:
        for el in src:
            if el.startswith('interface'):
                interface = (el.split(' ')[1]).split('\n')[0]

            match = re.search(r'ip address (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9])(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9])', el)

            if match:
                ipaddress = match.group(1).split(' ')[0]
                mask = match.group(2).split('\n')[0]
                if interface in result.keys():
                    tmp = list()
                    tmp.append(result[interface])
                    tmp.append((ipaddress, mask))
                    result[interface] = tmp
                else:
                    result[interface] = (ipaddress, mask)
    return result
def parse_sh_ip_int_br(file):



if __name__ == '__main__':
    result = get_ip_from_cfg('/Users/dariashantalova/PycharmProjects/pyneng/venv/exercises/config_r1.txt')
    print(result)


