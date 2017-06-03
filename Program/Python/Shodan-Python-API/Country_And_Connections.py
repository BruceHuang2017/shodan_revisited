#!/usr/bin/env python
#
# dis.py
# Search shodan, to use it in our research:
# python dis.py A850+Telemetry+Gateway ABB+Webmodule Allen-Bradley /BroadWeb/ Cimetrics+Eplus+Web+Server CIMPLICITY CitectSCADA EIG+Embedded+Web+Server eiPortal EnergyICT HMS+AnyBus-S+WebServer i.LON ioLogik Modbus+Bridge ModbusGW Modicon+M340+CPU Niagara+Web+Server NovaTech+HTTPD Powerlink Reliance+4+Control+Server RTS+Scada RTU560 Simatic+HMI SIMATIC+NET Simatic+S7 SoftPLC TAC/Xenta WAGO webSCADA-Modbus
#

'''
queries = ['A850+Telemetry+Gateway',
 'ABB+Webmodule',
 'Allen-Bradley',
 '/BroadWeb/',
 'Cimetrics+Eplus+Web+Server',
 'CIMPLICITY',
 'CitectSCADA',
 'EIG+Embedded+Web+Server',
 'eiPortal',
 'EnergyICT',
 'HMS+AnyBus-S+WebServer',
 'i.LON',
 'ioLogik',
 'Modbus+Bridge',
 'ModbusGW',
 'Modicon+M340+CPU',
 'Niagara+Web+Server',
 'NovaTech+HTTPD',
 'Powerlink',
 'Reliance+4+Control+Server',
 'RTS+Scada',
 'RTU560',
 'Simatic+HMI',
 'SIMATIC+NET',
 'Simatic+S7',
 'SoftPLC',
 'TAC/Xenta',
 'WAGO',
 'webSCADA-Modbus']

'''

import shodan
import sys
import csv

# Configuration
API_KEY = "sy3UmXUvE16OjS49q9VmKO8b5gzZOPCl"

# Input validation
if len(sys.argv) == 1:
    print 'Usage: %s <search query>' % sys.argv[0]
    sys.exit(1)

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)
    # Perform the search
    results = {}
    cdict={}
    asndic={}
    for i in sys.argv[1:]:
# not allow me to search unless upgrade
#        result = api.search(i, page = 280)
        results[i] =  api.search(i) # result
        cdict[i] = api.count(i,[('country', 300)])
        #asndic[i] = api.count(i,['asn'])
    # Show the results
    for j in results:
        print "query name: %s" %j, "Connections: ",results[j]['total']

    # Save csv
    with open('results.csv', 'w') as csvresult:
        fields = ['Shodan Query', 'Connections']
        writer = csv.DictWriter(csvresult, fieldnames = fields)
        for k in results:
            writer.writerow({'Shodan Query': k, 'Connections': results[k]['total'] })

    # More work for country
    '''
    with open('total.csv', 'w') as total:
        flds = ['Shodan Query', 'Country Name', 'Latitude', 'Longitude', 'OS', 'Data', 'IP_str']
        wtr = csv.DictWriter(total, fieldnames = flds)
        for a in results:
            for b in results[a]['matches']:
                cn = b['location']['country_name']
                la = b['location']['latitude']
                lg = b['location']['latitude']
                os = b['os']
                data = b['data']
                ipstr = b['ip_str']
                wtr.writerow({
                    'Shodan Query':a,
                    'Country Name':cn,
                    'Latitude':la,
                    'Longitude':lg,
                    'OS':os,
                    'Data':data,
                    'IP_str':ipstr
                })
'''
    # Count country number

    cresult = {}
    for cc in cdict:
    # cc is queries name
        for lst in cdict[cc]['facets']['country']:
            if lst['value'] in cresult:
                cresult[lst['value']] = lst['count'] + cresult[lst['value']]
            else:
                cresult[lst['value']] = lst['count']

    with open('country.csv', 'w') as csvc:
        fields = ['Country', 'Count']
        writer = csv.DictWriter(csvc, fieldnames = fields)
        for k in cresult:
            writer.writerow({'Country': k, 'Count': cresult[k] })


except Exception as e:
    print 'Error: %s' % e
    sys.exit(1)

