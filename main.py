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
    result = list()
    with open(file) as src:
        for el in src:
            interface_name = re.search(r'(([A-Za-z]+[0-9]+/[0-9]+/[0-9]+/[0-9]+)|([A-Za-z]+[0-9]+/[0-9]+/[0-9]+)|([A-Za-z]+[0-9]+/[0-9]+)|([A-Za-z]+[0-9]+))', el)
            ipaddress = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]|([u][n][a][s][s][i][g][n][e][d]))', el)
            status_protocol = re.search(r'(up|down|administratively down|err-disabled) +'r'(up|down)', el)

            if interface_name and ipaddress and status_protocol:
               result.append((interface_name.group(0), ipaddress.group(0), status_protocol.group(1),status_protocol.group(2)))
    return result



if __name__ == '__main__':
    # result = get_ip_from_cfg('/Users/dariashantalova/PycharmProjects/pyneng/venv/exercises/config_r1.txt')
    # print(result)
    res = parse_sh_ip_int_br('/Users/dariashantalova/PycharmProjects/pyneng/venv/exercises/show_ip_int_br.txt')



