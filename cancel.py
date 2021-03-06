###############################################################################
#    Author: llamasfSpn 
#    2013 - now
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
##############################################################################
#!/usr/bin/python
# python executable
import tempfile
from smb.SMBConnection import SMBConnection
from nmb.NetBIOS import NetBIOS

def store_smb_file(user,password,cliente_name,server_name,domain,ip_server,fpath_client):
	#init connection
	try:
		conn = SMBConnection(user,
		              password,
		             cliente_name,
		             server_name, domain,
		             use_ntlm_v2 = True,
                         sign_options=SMBConnection.SIGN_WHEN_SUPPORTED,
                         is_direct_tcp=False)
		print('Connected to %s' % server_name)		
		assert conn.connect(ip_server,139)
		#Entry File CANCEL.txt/csv
		#Description The file content must be empty					
		f = open('CANCEL.txt','w')
		f = open('CANCEL.txt','r+')		
		conn.storeFile(fpath_client,"/"+f.name, f)
		f.close()
	
	except Exception, e:
            print('Connect failed. Reason: %s', e)
            return False

	
def getBIOSName(remote_smb_ip, timeout=30):
    try:
        bios = NetBIOS()
        srv_name = bios.queryIPForName(remote_smb_ip, timeout=timeout)
    except:
        print >> sys.stderr, "Looking up timeout, check remote_smb_ip again!!"
    finally:
        bios.close()
        return srv_name

##Data Access send to CashDro
bios_name = getBIOSName('IP')
server_name = bios_name[0]
user = ''
password = ''
cliente_name = ''
domain = ''
ip_server = ''
fpath_client = ''
store_smb_file(user,password,cliente_name,server_name,domain,ip_server,fpath_client)
