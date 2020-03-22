# Example:
# Input: 1592551013
# Output: ['159.255.101.3', '159.255.10.13']
def ip_addresses(s, ip_parts=[]):
  # Fill this in.
    ip_parts = []
    ip_parts.append(get_address(s))

    return ip_parts


def get_address(add):
    output = ""
    value = ""
    for i in range(len(add)):
        value = value + add[i]
        if int(value) > 255 or len(value) > 3 :
            output = output + "."
            output = output + add[i]
            value = add[i]
        else :
            output = output + add[i]
    return output

print(ip_addresses('1592551013'))
# ['159.255.101.3', '159.255.10.13']
