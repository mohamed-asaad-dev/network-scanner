import subprocess
import csv
import json
import argparse
import ipaddress
from logger import logging_info

logger = logging_info()

#parsing arguements to use them in the CLI and run the script directly
parser = argparse.ArgumentParser(description='Scans network and creates Network files')
parser.add_argument('--target',required=True, help="Network target")
parser.add_argument('--output', default= 'file.csv', help='Output file')

#assigning variables with the parsed arguements
args = parser.parse_args()
target = args.target
output = args.output

#logging variable information
logger.info("Program started")
logger.info(f"Target argument: {target}")
logger.info(f"Output argument: {output}")

# #output files fieldnames
fieldnames = ['Devices','Host State', 'working ports' , 'services']


#verifying that the target network entered has valid data.
try:
    ipaddress.ip_network(target)
    #loggin validated data
    logger.info("Target network validated successfully")
except ValueError:
    #error handling
    logger.error("Invalid IP/network provided")
    print('Enter a valid ip address')
    exit()
    

def connected_devices():
    #function used to get connected devices on the target network and create a csv file 
    
    #creating .csv file using dynamic filenames
    with open('results/{}.csv'.format(target.replace('/','_')), 'w') as pw:
            csv_writer = csv.DictWriter(pw , fieldnames=fieldnames)
            csv_writer.writeheader()
            
            #running nmap command and capturing output as text
            scan_output = subprocess.run(['nmap', '-sn', target],capture_output=True, text=True)
            #logging completion of the command
            logger.info("Nmap scan completed")
            logger.info(f"Return code: {scan_output.returncode}")
            lines1 = scan_output.stdout.splitlines()
            device = ''
            status = ''
           
            #parsing devices and their states
            for index,line in enumerate(lines1):
                
                print(line)
                
                if(index%2 != 0):
                    if(index == len(lines1)-3):
                        device= line.split()[-1]
                    elif(index == len(lines1)-1):
                        continue
                    else:
                        device = line.split()[-1]
                    logger.info(f"Discovered device: {device}")
                elif(index%2 == 0):
                    if(index == 0):
                        continue
                    else:
                        status = line.split()[2]
                        #writing parsed data into csv file in rows
                        csv_writer.writerow({
                    'Devices':device,
                    'Host State' : status
                        })


def current_working_ports():
    #function used to add current working ports of the connected devices
    
    protocol_summary = subprocess.run(['nmap' , '-P' , target],capture_output=True,text=True)
    f_output = protocol_summary.stdout.splitlines()
    rows = []
    ports = []
    tmp_ports = []
    tmp_services = []
    services = []
    
    for index, line in enumerate(f_output,start=2):
        
        if(line[0:4] == 'Nmap' or line[0:4] == 'Host' or line[0:3] == 'Not' or line[0:3] == 'All' or line[0:8] == 'Starting' or line[0:4] == 'PORT'):
            continue 
        elif(line == ''):
            ports.append(tmp_ports)
            tmp_ports = []
            services.append(tmp_services)
            tmp_services = []
        else:
            port, state, service = line.split()
            tmp_ports.append(port)    
            tmp_services.append(service) 
    # Step 1: read
    with open('results/{}.csv'.format(target.replace('/','_')), 'r') as file:
        reader = csv.DictReader(file)
        working_port = reader.fieldnames[2]
        reader.fieldnames[3] = 'services'
        if(working_port != 'working ports'):
            working_port = 'working ports'
        for index,row in enumerate(reader):
            # Step 2: modify
                row['working ports'] = ports[index]
                row['services'] = services[index]
                rows.append(row)   
    # Step 3: rewrite file
        with open('results/{}.csv'.format(target.replace('/','_')), 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

def csv_to_json_converter():
    #function used to create a json file from existing csv file
    csv_path = 'results/{}.csv'.format(target.replace('/','_'))
    json_path = 'results/{}.json'.format(target.replace('/','_'))
    data = []
    
    #opening csv file and storing data in a list
    with open(csv_path ,'r') as rf:
        reader = csv.DictReader(rf)
        for row in reader:
            data.append(row)
        with open(json_path , 'w') as wf:
            #adding data to the json file using dump method
            json.dump(data, wf,indent=4)
        

    
            