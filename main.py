from open_request import *
from mask_functions import *
from get_input import *

#wb = load_workbook(template.xlsx)   #open template workbook
#main_sheet = wb[wb.sheetnames[0]]   #open sheet to write
my_input = get_input()              #get input from keyboard
src, dst = open_request('template1.xlsm')
source = []
destination = []
for ip_address in src:
    ip_address = ip_address.split("/")
    net_id = ip_address[0]
    mask = ip_address[1]
    mask = check_mask(mask)
    n_or_h = "n"
    if mask == 32:
        n_or_h = "h"
    source_object = my_input["src_brand"]+my_input["src_env"]+n_or_h+"_"+my_input["src_location"]+my_input["src_function"]+net_id+"_"+str(mask)
    source.append(source_object)
for ip_address in dst:
    ip_address = ip_address.split("/")
    net_id = ip_address[0]
    mask = ip_address[1]
    mask = check_mask(mask)
    n_or_h = "n"
    if mask == 32:
        n_or_h = "h"
    destination_object = my_input["dst_brand"]+my_input["dst_env"]+n_or_h+"_"+my_input["dst_location"]+my_input["dst_function"]+net_id+"_"+str(mask)
    destination.append(destination_object)
s = "\n"
source = s.join(source)
destination = s.join(destination)
print(source)
print(destination)

















""""
for network in column
	network = network.split()
	net_if = network[0]
	mask = network[1]
	mask = check_mask(mask)
	network = brand_env_h/n_location-function-netid_mask


brand =
env =
location =
function =
"""