# cd to directory with data, in terminal, type in: python pyAnalysis.py
# for research purpose, open python intepreter and import those functions.
import pandas as pd
import csv
'''
    # read all csv data frames
q = ['A850+Telemetry+Gateway',
 'ABB+Webmodule',
 ### 'Allen-Bradley', # latin_1 encoding europe
 'BroadWeb',
 'Cimetrics+Eplus+Web+Server',
 'CIMPLICITY',
 # 'CitectSCADA', not exist
 'EIG+Embedded+Web+Server',
 'eiPortal',
 ### 'EnergyICT', # cp1252 encoding, western europe
 'HMS+AnyBus-S+WebServer',
 'i.LON',
 # 'ioLogik', # latin_1 encoding europe
 'Modbus+Bridge',
 'ModbusGW',
 'Modicon+M340+CPU',
 'Niagara+Web+Server',
 # 'NovaTech+HTTPD', not exist
 'Powerlink',
 'Reliance+4+Control+Server',
 'RTS+Scada',
 'RTU560',
 # 'Simatic+HMI', not exist
 'SIMATIC+NET',
 'Simatic+S7',
 'SoftPLC',
 # 'TAC/Xenta', n ex
 'WAGO',]
 # 'webSCADA-Modbus'] not exist
qq = [a+'.csv' for a in q]
p={}
for i in range(len(qq)):
    print('Read file number: '+str(i))
    p[i]=pd.read_csv(qq[i])
p[21] = pd.read_csv('Allen-Bradley.csv', encoding='latin_1')
p[22] = pd.read_csv('EnergyICT.csv', encoding='cp1252')
p[23] = pd.read_csv('ioLogik.csv', encoding='latin_1')
print('Finish import data.')
'''

# some user defined functions:
def disBanner(qq0):
    # for research purpose, check each banner for more informationi,
    # some interesting information like: email addresses, host key algorithm in WAGO.csv
    bd ={}#counter
    bds={}#string spliter
    r={}
    for a in set(qq0['Banner']):
        # string
        bds[a] = (a.split())
        # count
        for b in qq0['Banner']:
            if a == b:
                if a in bd:
                    bd[a] = bd[a] + 1
                else:
                    bd[a] = 1
    for a in bd:
        r[a] = {'Banner_Counter':bd[a] , 'Splited_Banner':bds[a]}
    return r

def combine(qq0, n=3):
    # selected length of banner and counter
    r = disBanner(qq0)
    com={}
    for a in r:
        b=''
        if len(r[a]['Splited_Banner'])<=n:
            b = a
        else:
            for c in range(n):
                b =b+' '+r[a]['Splited_Banner'][c]
        if b in com:
            com[b] = r[a]['Banner_Counter'] + com[b]
        else:
            com[b] = r[a]['Banner_Counter']
    return com

# return {server name : count}, but still need some manual sorting.
# EnergyICT.csv server have unique id which is not intertesd in this research. after checked search results: search term n=2
def findServer(qq0, n=3):
    r = disBanner(qq0)
    ser={'NA':0}
    for k,v in r.items():
        if 'Server:' in v['Splited_Banner']:
            idx = v['Splited_Banner'].index('Server:')
            sn=''
            for i in range(n):
                sn = sn + ' ' + v['Splited_Banner'][idx+i+1]
            if sn in ser:
                ser[sn] = ser[sn]+v['Banner_Counter']
            else:
                ser[sn] = v['Banner_Counter']
        else:
            ser['NA']=ser['NA']+v['Banner_Counter']
    return ser

# get header of each banner and the # of it.
def bannerSum(p={'happy':1}, n=3):
    #try:
    #    import pandas as pd
    #    import csv
    #except:
    #    raise
    if 'happy' in p:
        q = ['A850+Telemetry+Gateway','ABB+Webmodule','BroadWeb','Cimetrics+Eplus+Web+Server','CIMPLICITY','EIG+Embedded+Web+Server','eiPortal','HMS+AnyBus-S+WebServer','i.LON','Modbus+Bridge','ModbusGW','Modicon+M340+CPU','Niagara+Web+Server','Powerlink','Reliance+4+Control+Server','RTS+Scada','RTU560','SIMATIC+NET','Simatic+S7','SoftPLC','WAGO',]
        qq = [a+'.csv' for a in q]
        p={}
        for i in range(len(qq)):
            print('Read file number: '+str(i))
            p[i]=pd.read_csv(qq[i])
        p[21] = pd.read_csv('Allen-Bradley.csv', encoding='latin_1')
        p[22] = pd.read_csv('EnergyICT.csv', encoding='cp1252')
        p[23] = pd.read_csv('ioLogik.csv', encoding='latin_1')
        print('Finish import data.')

    print('Start Iteration and count banner.')
    final={}
    for i in p:
        final[i] =combine(p[i], n)
    x={}
    for k,v in final.items():
        for qk,qv in v.items():
            if qk in x:
                x[qk]=x[qk]+qv
            else:
                x[qk]=qv

    # nd is index for length of server name
    print('Solving Server Counting problem.')
    nd = {0:3, 1:3, 2:1, 3:3, 4:1, 5:3, 6:1, 7:3, 8:1, 9:3, 10:3, 11:3, 12:3, 13:2, 14:1, 15:4, 16:3, 17:3, 18:3, 19:3, 20:1, 21:2, 22:2,23:3}
    serverx = {}
    for k,v in p.items():
        n=nd[k]
        for kd, vd in findServer(v, n).items():
            if kd in serverx:
                serverx[kd] = serverx[kd] + vd
            else:
                serverx[kd] = vd

    print('Creating csv file.')
    # save to csv file
    with open('Banner_Summary.csv', 'w') as okay:
        f = ['Banner', 'Count']
        w = csv.DictWriter(okay, fieldnames=f)
        for k,v in x.items():
            w.writerow({'Banner':k, 'Count':v})

    with open('Server_Summary.csv', 'w') as okay:
        f=['Server_Tag', 'Count']
        w=csv.DictWriter(okay, fieldnames=f)
        for k,v in serverx.items():
            w.writerow({'Server_Tag':k, 'Count':v})

    return [x, serverx]

bannerSum()
# server search notes:
# conclusion:
# nd = {0:3, 1:3, 2:1, 3:3, 4:1, 5:3, 6:1, 7:3, 8:1, 9:3, 10:3, 11:3, 12:3, 13:2, 14:1, 15:4, 16:3, 17:3, 18:3, 19:3, 20:1, 21:2, 22:2,23:3}


'''
In [606]: findServer(p[0])
Out[606]: {' addUPI Server 1.2': 16, 'NA': 30}

In [607]: findServer(p[1])
Out[607]: {' HMS AnyBus-S WebServer': 4, 'NA': 0}

In [608]: findServer(p[2])
Out[608]:
{' Microsoft-IIS/5.1 Date: Mon,': 1,
 ' Microsoft-IIS/6.0 MicrosoftOfficeWebServer: 5.0_Pub': 1,
 ' Microsoft-IIS/6.0 X-UA-Compatible: IE=EmulateIE7': 1,
 ' Microsoft-IIS/7.5 Set-Cookie: ASPSESSIONIDCGBQDABT=GFCFJHGDBHHMNJDPCKDJHKFM;': 1,
 ' Microsoft-IIS/8.5 Set-Cookie: ASPSESSIONIDQCTQSSBB=HCCDDLHBDBBMEMLEOFOCFBAP;': 1,
 'NA': 1}

In [609]: findServer(p[2], n=1)
Out[609]:
{' Microsoft-IIS/5.1': 1,
 ' Microsoft-IIS/6.0': 2,
 ' Microsoft-IIS/7.5': 1,
 ' Microsoft-IIS/8.5': 1,
 'NA': 1}

In [610]: findServer(p[3])
Out[610]: {' Cimetrics Eplus Web': 11, 'NA': 0}

In [611]: findServer(p[4])
Out[611]:
{' CIMPLICITY-HttpSvr/1.0 Date: Fri,': 5,
 ' CIMPLICITY-HttpSvr/1.0 Date: Mon,': 6,
 ' CIMPLICITY-HttpSvr/1.0 Date: Sat,': 5,
 ' CIMPLICITY-HttpSvr/1.0 Date: Sun,': 4,
 ' CIMPLICITY-HttpSvr/1.0 Date: Thu,': 3,
 ' CIMPLICITY-HttpSvr/1.0 Date: Tue,': 5,
 ' CIMPLICITY-HttpSvr/1.0 Date: Wed,': 3,
 'NA': 2}

In [612]: findServer(p[4], n=1)
Out[612]: {' CIMPLICITY-HttpSvr/1.0': 31, 'NA': 2}

In [613]: findServer(p[5])
Out[613]: {' EIG Embedded Web': 122, 'NA': 0}

In [614]: findServer(p[6])
Out[614]:
{' Apache Location: https://EMCS.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://Mitie.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://SAUR.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://WML.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://aspus.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://bourne-leisure.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://danone.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://dol.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://elster-it-gm.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://enactocofely.energyict.com/eiportal/index.html': 2,
 ' Apache Location: https://enexis.energyict.com/eiportal/index.html': 2,
 ' Apache Location: https://espnz.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://heidelberg.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://hm.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://metering.cofelyservices-gdfsuez.be/eiportal/index.html': 1,
 ' Apache Location: https://netrail.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://odmwatervalrow.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://rossmann.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://sedac.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://sgead-demo.energyict.com/eiportal/index.html': 2,
 ' Apache Location: https://strukton.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://t4m.energyict.com/eiportal/index.html': 1,
 ' Apache Location: https://upl.energyict.com/eiportal/index.html': 1,
 ' Microsoft-IIS/7.5 X-AspNet-Version: 4.0.30319': 1,
 'NA': 0}

In [615]: findServer(p[6], n=1)
Out[615]: {' Apache': 26, ' Microsoft-IIS/7.5': 1, 'NA': 0}

In [616]: findServer(p[7])
Out[616]: {' HMS AnyBus-S WebServer': 34, ' HMS Anybus-S WebServer': 2, 'NA': 0}

In [617]: findServer(p[8])
Out[617]:
{' WindRiver-WebServer/4.4 Cache-Control: max-age=86400,': 33,
 ' WindRiver-WebServer/4.4 Cache-Control: no-cache,': 1491,
 ' WindRiver-WebServer/4.4 Connection: Keep-Alive': 11,
 ' WindWeb/1.0.3 Date: FRI': 21,
 ' WindWeb/1.0.3 Date: FRI,': 113,
 ' WindWeb/1.0.3 Date: MON': 29,
 ' WindWeb/1.0.3 Date: MON,': 123,
 ' WindWeb/1.0.3 Date: SAT': 16,
 ' WindWeb/1.0.3 Date: SAT,': 133,
 ' WindWeb/1.0.3 Date: SUN': 15,
 ' WindWeb/1.0.3 Date: SUN,': 133,
 ' WindWeb/1.0.3 Date: THU': 22,
 ' WindWeb/1.0.3 Date: THU,': 150,
 ' WindWeb/1.0.3 Date: TUE': 16,
 ' WindWeb/1.0.3 Date: TUE,': 91,
 ' WindWeb/1.0.3 Date: WED': 21,
 ' WindWeb/1.0.3 Date: WED,': 116,
 ' microHttpd/2.0 Echelon Corporation': 3,
 'NA': 417}

In [618]: findServer(p[8], n=1)
Out[618]:
{' WindRiver-WebServer/4.4': 1535,
 ' WindWeb/1.0.3': 999,
 ' microHttpd/2.0': 3,
 'NA': 417}

In [619]: findServer(p[9])
Out[619]: {' OnyxxWebServer 1ec0 <!DOCTYPE': 1, 'NA': 60}

In [620]: findServer(p[10])
Out[620]: {' Boa/0.93.15 Connection: close': 54, 'NA': 0}

In [621]: findServer(p[11])
Out[621]: {'NA': 49}

In [622]: findServer(p[12])
Out[622]:
{' Apache Last-Modified: Tue,': 1,
 ' Niagara Web Server/1.1': 885,
 ' Niagara Web Server/3.0': 46,
 ' Niagara Web Server/3.7.106.11': 1,
 ' Niagara Web Server/3.7.106.15': 1,
 ' Niagara Web Server/3.8.111': 1,
 ' Niagara Web Server/4.1.27.20': 1,
 'NA': 9063}

In [623]: findServer(p[13])
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-623-3fd79189166c> in <module>()
----> 1 findServer(p[13])

<ipython-input-605-ab24833d9744> in findServer(qq0, n)
      7             sn=''
      8             for i in range(n):
----> 9                 sn = sn + ' ' + v['Splited_Banner'][idx+i+1]
     10             if sn in ser:
     11                 ser[sn] = ser[sn]+v['Banner_Counter']

IndexError: list index out of range

In [624]: findServer(p[13], n=2)
Out[624]:
{' Apache/1.3.31 (Unix)': 1655,
 ' Bba2.0 (Linux)': 17,
 ' Boa/0.93.15 Connection:': 3,
 ' lighttpd/1.4.25 (Linux)': 1,
 'NA': 109}

In [627]: findServer(p[14], n=1)
Out[627]: {' Indy/9.00.10': 12, ' Jetty(9.2.z-SNAPSHOT)': 1, 'NA': 0}

In [630]: findServer(p[15], n=4)
Out[630]:
{' Apache/2.0.63 (FreeBSD) mod_python/3.3.1 Python/2.5.1': 1,
 ' Apache/2.2.17 (FreeBSD) mod_ssl/2.2.17 OpenSSL/0.9.8q': 4,
 'NA': 0}

In [631]: findServer(p[16])
Out[631]: {' ABB RTU560 Connection:': 6, 'NA': 0}

In [632]: findServer(p[17])
Out[632]: {'NA': 164}

In [633]: findServer(p[18])
Out[633]: {' Apache Last-Modified: Wed,': 1, 'NA': 632}

In [634]: findServer(p[19])
Out[634]: {' Mono.WebServer/1.0.0.0 Win32NT X-AspNet-Version:': 2, 'NA': 785}

In [637]: findServer(p[20], n=1)
Out[637]:
{' -': 5,
 ' Content-Security-Policy:': 3,
 ' Microsoft-IIS/8.5': 2,
 ' lighttpd': 2,
 ' lighttpd/1.4.15': 27,
 'NA': 127}


In [639]: findServer(p[21], n=2)
Out[639]: {' Apache/2.4.7 (Ubuntu)': 1, ' TornadoServer/4.4 Etag:': 1, 'NA': 4527}

In [641]: findServer(p[22], n=2)
Out[641]: {' EnergyICT RTU': 766, 'NA': 0}

In [642]: findServer(p[23])
Out[642]: {' ioLogik Web Server/1.0': 225, 'NA': 5}


'''

# http search note


# import data
'''
# read all datas
q = ['A850+Telemetry+Gateway',
 'ABB+Webmodule',
 ### 'Allen-Bradley', # latin_1 encoding europe
 'BroadWeb',
 'Cimetrics+Eplus+Web+Server',
 'CIMPLICITY',
 # 'CitectSCADA', not exist
 'EIG+Embedded+Web+Server',
 'eiPortal',
 ### 'EnergyICT', # cp1252 encoding, western europe
 'HMS+AnyBus-S+WebServer',
 'i.LON',
 # 'ioLogik', # latin_1 encoding europe
 'Modbus+Bridge',
 'ModbusGW',
 'Modicon+M340+CPU',
 'Niagara+Web+Server',
 # 'NovaTech+HTTPD', not exist
 'Powerlink',
 'Reliance+4+Control+Server',
 'RTS+Scada',
 'RTU560',
 # 'Simatic+HMI', not exist
 'SIMATIC+NET',
 'Simatic+S7',
 'SoftPLC',
 # 'TAC/Xenta', n ex
 'WAGO',]
 # 'webSCADA-Modbus'] not exist

qq = [a+'.csv' for a in q]
p={}
for i in range(len(qq)):
    print(i)
    p[i]=pd.read_csv(qq[i])
p[21] = pd.read_csv('Allen-Bradley.csv', encoding='latin_1')
p[22] = pd.read_csv('EnergyICT.csv', encoding='cp1252')
p[23] = pd.read_csv('ioLogik.csv', encoding='latin_1')
'''



# some old scripts. for memory
'''
# start iteration:
sortedbds = {}
banner=[]
i=0
for qqq in qq:
    i=i+1
    print(str(i)+' times')
    qq0 = pd.read_csv(qqq)
# qq0s = qq0['Banner'].to_string()
# qq0s.split()
# qq0swords = qq0s.split()
# qq0swS = pd.Series(qq0swords, name = 'have_HTTP/1.0')
# qq0swD = pd.DataFrame(qq0swords)
# qq0swD.append(qq0swS.str.contains('HTTP/1.0'))
# create dict to sort banner
# pgm
    bd ={}
    bds={}
    for a in set(qq0['Banner']):
        bds[a] = (a.split())
        for b in qq0['Banner']:
            banner=banner+[b]
            if a == b:
                if a in bd:
                    bd[a] = bd[a] + 1
                else:
                    bd[a] = 1
# manually check keys
# this is for test:
#    for a in bd:
#        print('***************************\nkey name:\n'+a+
#              '\ncount number:\n' +str(bd[a]) +'\n')
# use two dicts and get count number
    # this is for test:
#    for a in bds:
#        if (bds[a][0]=='HTTP/1.0') & (bds[a][1] == '404'):
#            print((bd[a])) # print out the number of heep/1.0 404 in this query
# this is pgm:
    for a in bd:
        if len(bds[a])>4:
            b = bds[a][0] +' ' + bds[a][1]+' ' + bds[a][2]+' ' + bds[a][3]+' ' + bds[a][4]
        elif len(bds[a])==4:
            b = bds[a][0] +' ' + bds[a][1]+' ' + bds[a][2]+' ' + bds[a][3]
        elif len(bds[a])==3:
            b = bds[a][0] +' ' + bds[a][1]+' ' + bds[a][2]
        elif len(bds[a])==2:
            b = bds[a][0] +' ' + bds[a][1]
        elif len(bds[a])==1:
            b = bds[a][0]
        if b in sortedbds:
            sortedbds[b] = bd[a] + sortedbds[b]
        else:
            sortedbds[b] = bd[a]

# show results
for a in sortedbds:
    print('\nkeys:\n'+a + '\ncounter: \n'+str(sortedbds[a]))
'''

