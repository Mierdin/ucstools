# Copyright 2014 Matt Oswalt
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#Tested with UCS Platform Emulator 2.2(1bPE1) and Cisco's UCS Python SDK 0.8

from UcsSdk import *

#TODO: figure out how to specific arguments as optional or required
def getUcsWWPNs(ucs_ipaddr, ucs_username, ucs_passwd):

	handle = UcsHandle()  
	handle.Login(ucs_ipaddr, username=ucs_username, password=ucs_passwd)

	vHBADict = {}

	#TODO: Statically defining sub-organization for now, will make more dynamic later

	#Need to make a generic function (probably place in central "general functions" file that finds an org at any nest level, and retrieves ful DN for things like what you're doing below. Allows for org filtering at any level
	ucsOrg = "org-ORG_ROOT"

	#TODO: For some reason, if the specified org does not exist, this still returns all orgs, rather than erroring out or providing a null value. Need to handle this better
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/" + ucsOrg + "/"})
	moArr = handle.GetManagedObject(obj, "vnicFc")
	for mo in moArr:
		#Pull only actual vHBAs (not templates) and on the desired fabric (A/B)
		if str(mo.Addr) != 'derived' and mo.SwitchId == 'A':

			#We're retrieving Dn here so we can include the service profile in the name
			origDn = str(mo.Dn)
			
			#Need to do a little string surgery to transform the Dn of the vHBA into a proper zone name.
			origDn = origDn.replace('org-root/org-TPAC_1/','')
			origDn = origDn.replace('/','_')
			origDn = origDn.replace('ls-','')
			origDn = origDn.replace('fc-','')

			#using the WWPN address as key since more likely to be unique
			vHBADict[mo.Addr] = origDn

	return vHBADict
