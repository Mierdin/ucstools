
def ucsHousekeeping(ucs_ipaddr, ucs_username, ucs_passwd):

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/compute-pool-default"})
	handle.RemoveManagedObject(obj)

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/iqn-pool-default"})
	handle.RemoveManagedObject(obj)

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/uuid-pool-default"})
	handle.RemoveManagedObject(obj)

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/mac-pool-default"})
	handle.RemoveManagedObject(obj)

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/wwn-pool-node-default"})
	handle.RemoveManagedObject(obj)

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/wwn-pool-default"})
	handle.RemoveManagedObject(obj)

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/ip-pool-iscsi-initiator-pool"})
	handle.AddManagedObject(obj, "ippoolBlock", {"To":"1.1.1.1", "From":"1.1.1.1", "Dn":"org-root/ip-pool-iscsi-initiator-pool/block-1.1.1.1-1.1.1.1"})

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root"})
	handle.AddManagedObject(obj, "lsmaintMaintPolicy", {"UptimeDisr":"user-ack", "SchedName":"", "PolicyOwner":"local", "Descr":"", "Dn":"org-root/maint-default"}, True)

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root"})
	handle.AddManagedObject(obj, "orgOrg", {"Dn":"org-root/org-ORG_TEST", "Name":"ORG_TEST", "Descr":""})


def createVLANsandVSANs(ucs_ipaddr, ucs_username, ucs_passwd):

	obj = handle.GetManagedObject(None, None, {"Dn":"fabric/lan"})
	handle.AddManagedObject(obj, "fabricVlan", {"DefaultNet":"no", "PubNwName":"", "Dn":"fabric/lan/net-VLAN123", "PolicyOwner":"local", "CompressionType":"included", "Name":"VLAN123", "Sharing":"none", "McastPolicyName":"", "Id":"123"})

	obj = handle.GetManagedObject(None, None, {"Dn":"fabric/san/A"})
	handle.AddManagedObject(obj, "fabricVsan", {"FcZoneSharingMode":"coalesce", "ZoningState":"disabled", "FcoeVlan":"10","PolicyOwner":"local", "Dn":"fabric/san/A/", "Name":"VSAN_10", "Id":"10"})

	obj = handle.GetManagedObject(None, None, {"Dn":"fabric/san/B"})
	handle.AddManagedObject(obj, "fabricVsan", {"FcZoneSharingMode":"coalesce", "ZoningState":"disabled", "FcoeVlan":"20","PolicyOwner":"local", "Dn":"fabric/san/B/", "Name":"VSAN_20", "Id":"20"})


def createPools(ucs_ipaddr, ucs_username, ucs_passwd):

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/ip-pool-ext-mgmt"})
	handle.SetManagedObject(obj, None, {"AssignmentOrder":"sequential", "PolicyOwner":"local", "Descr":"Management IP Pool"})

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/ip-pool-ext-mgmt"})
	handle.AddManagedObject(obj, "ippoolBlock", {"To":"10.12.0.149", "Dn":"org-root/ip-pool-ext-mgmt/block-10.12.0.100-10.12.0.149", "From":"10.12.0.100", "DefGw":"10.12.0.1"})


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "uuidpoolPool", {"Descr":"UUID Pool - ESXi", "Prefix":"derived", "AssignmentOrder":"sequential", "Dn":"org-root/org-ORG_TEST/uuid-pool-UUID-ESX", "PolicyOwner":"local", "Name":"UUID-ESX"})
	mo_1 = handle.AddManagedObject(mo, "uuidpoolBlock", {"To":"0000-25B521EE00FF", "From":"0000-25B521EE0000", "Dn":"org-root/org-ORG_TEST/uuid-pool-UUID-ESX/block-from-0000-25B521EE0000-to-0000-25B521EE00FF"})
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "macpoolPool", {"PolicyOwner":"local", "AssignmentOrder":"sequential", "Dn":"org-root/org-ORG_TEST/mac-pool-MAC-ESX-A", "Name":"MAC-ESX-A", "Descr":"ESXi Fabric A"})
	mo_1 = handle.AddManagedObject(mo, "macpoolBlock", {"To":"00:25:B5:21:A0:FF", "From":"00:25:B5:21:A0:00", "Dn":"org-root/org-ORG_TEST/mac-pool-MAC-ESX-A/block-00:25:B5:21:A0:00-00:25:B5:21:A0:FF"})
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "macpoolPool", {"PolicyOwner":"local", "AssignmentOrder":"sequential", "Dn":"org-root/org-ORG_TEST/mac-pool-MAC-ESX-B", "Name":"MAC-ESX-B", "Descr":"ESXi Fabric B"})
	mo_1 = handle.AddManagedObject(mo, "macpoolBlock", {"To":"00:25:B5:21:B0:FF", "From":"00:25:B5:21:B0:00", "Dn":"org-root/org-ORG_TEST/mac-pool-MAC-ESX-B/block-00:25:B5:21:B0:00-00:25:B5:21:B0:FF"})
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "fcpoolInitiators", {"Descr":"ESXi WWNNs", "PolicyOwner":"local", "AssignmentOrder":"sequential", "Purpose":"node-wwn-assignment", "Dn":"org-root/org-ORG_TEST/wwn-pool-WWNN-ESX", "Name":"WWNN-ESX"})
	mo_1 = handle.AddManagedObject(mo, "fcpoolBlock", {"To":"20:00:00:25:B5:21:F0:FF", "From":"20:00:00:25:B5:21:F0:00", "Dn":"org-root/org-ORG_TEST/wwn-pool-WWNN-ESX/block-20:00:00:25:B5:21:F0:00-20:00:00:25:B5:21:F0:FF"})
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "fcpoolInitiators", {"Descr":"ESXi Fabric A", "PolicyOwner":"local", "AssignmentOrder":"sequential", "Purpose":"port-wwn-assignment", "Dn":"org-root/org-ORG_TEST/wwn-pool-WWPN-ESX-A", "Name":"WWPN-ESX-A"})
	mo_1 = handle.AddManagedObject(mo, "fcpoolBlock", {"To":"20:00:00:25:B5:21:A0:FF", "From":"20:00:00:25:B5:21:A0:00", "Dn":"org-root/org-ORG_TEST/wwn-pool-WWPN-ESX-A/block-20:00:00:25:B5:21:A0:00-20:00:00:25:B5:21:A0:FF"})
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "fcpoolInitiators", {"Descr":"ESXi Fabric B", "PolicyOwner":"local", "AssignmentOrder":"sequential", "Purpose":"port-wwn-assignment", "Dn":"org-root/org-ORG_TEST/wwn-pool-WWPN-ESX-B", "Name":"WWPN-ESX-B"})
	mo_1 = handle.AddManagedObject(mo, "fcpoolBlock", {"To":"20:00:00:25:B5:21:B0:FF", "From":"20:00:00:25:B5:21:B0:00", "Dn":"org-root/org-ORG_TEST/wwn-pool-WWPN-ESX-B/block-20:00:00:25:B5:21:B0:00-20:00:00:25:B5:21:B0:FF"})
	handle.CompleteTransaction()

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	handle.AddManagedObject(obj, "computePool", {"PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/compute-pool-B200-M3-POOL", "Name":"B200-M3-POOL", "Descr":"B200M3 Servers (VMware)"})

def createStaticPolicies(ucs_ipaddr, ucs_username, ucs_passwd):

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root"})
	handle.AddManagedObject(obj, "computeChassisDiscPolicy", {"Descr":"", "PolicyOwner":"local", "LinkAggregationPref":"port-channel", "Action":"4-link", "Dn":"org-root/chassis-discovery", "Name":"", "Rebalance":"user-acknowledged"}, True)


	obj = handle.GetManagedObject(None, None, {"Dn":"org-root"})
	handle.AddManagedObject(obj, "computePsuPolicy", {"Dn":"org-root/psu-policy", "PolicyOwner":"local", "Descr":"", "Redundancy":"grid"}, True)


	obj = handle.GetManagedObject(None, None, {"Dn":"fabric"})
	handle.AddManagedObject(obj, "fabricLanCloud", {"MacAging":"never", "Mode":"end-host", "VlanCompression":"disabled", "Dn":"fabric/lan"}, True)


	obj = handle.GetManagedObject(None, None, {"Dn":"fabric"})
	handle.AddManagedObject(obj, "fabricLanCloud", {"MacAging":"mode-default", "Mode":"end-host", "VlanCompression":"disabled", "Dn":"fabric/lan"}, True)


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"fabric/lan/classes"})
	mo = handle.SetManagedObject(obj, None, {"PolicyOwner":"local", "Descr":""})
	mo_1 = handle.AddManagedObject(mo, "qosclassEthClassified", {"Cos":"1", "Weight":"7", "Dn":"fabric/lan/classes/class-bronze", "MulticastOptimize":"no", "AdminState":"enabled", "Mtu":"9216", "Drop":"drop", "Name":""}, True)
	mo_2 = handle.AddManagedObject(mo, "qosclassEthClassified", {"Cos":"4", "Weight":"9", "Dn":"fabric/lan/classes/class-gold", "MulticastOptimize":"no", "AdminState":"enabled", "Mtu":"normal", "Drop":"drop", "Name":""}, True)
	mo_3 = handle.AddManagedObject(mo, "qosclassEthClassified", {"Cos":"5", "Weight":"10", "Dn":"fabric/lan/classes/class-platinum", "MulticastOptimize":"no", "AdminState":"enabled", "Mtu":"normal", "Drop":"drop", "Name":""}, True)
	mo_4 = handle.AddManagedObject(mo, "qosclassEthClassified", {"Cos":"2", "Weight":"8", "Dn":"fabric/lan/classes/class-silver", "MulticastOptimize":"no", "AdminState":"enabled", "Mtu":"9216", "Drop":"drop", "Name":""}, True)
	handle.CompleteTransaction()


	obj = handle.GetManagedObject(None, None, {"Dn":"sys/svc-ext/datetime-svc"})
	handle.AddManagedObject(obj, "commNtpProvider", {"Dn":"sys/svc-ext/datetime-svc/ntp-123.123.123.1", "Name":"123.123.123.1", "Descr":""})


	obj = handle.GetManagedObject(None, None, {"Dn":"sys/svc-ext/datetime-svc"})
	handle.SetManagedObject(obj, None, {"AdminState":"enabled", "Port":"0", "PolicyOwner":"local", "Descr":"", "Timezone":"America/New_York (Eastern Time)"})


	obj = handle.GetManagedObject(None, None, {"Dn":"sys/svc-ext/snmp-svc"})
	handle.AddManagedObject(obj, "commSnmpTrap", {"Dn":"sys/svc-ext/snmp-svc/snmp-trap2.2.2.2", "Hostname":"2.2.2.2", "NotificationType":"traps", "Port":"162", "Community":"snmpcommunitystring", "V3Privilege":"noauth", "Version":"v2c"})


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"sys"})
	mo = handle.AddManagedObject(obj, "commSvcEp", {"Dn":"sys/svc-ext", "PolicyOwner":"local", "Descr":""}, True)
	mo_1 = handle.AddManagedObject(mo, "commSnmp", {"SysLocation":"CustomerLocation", "IsSetSnmpSecure":"no", "Descr":"SNMP Service", "SysContact":"CustomerName", "PolicyOwner":"local", "AdminState":"enabled", "Community":"snmpcommunitystring", "Dn":"sys/svc-ext/snmp-svc"}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "epqosDefinition", {"PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/ep-qos-BE", "Name":"BE", "Descr":""})
	mo_1 = handle.AddManagedObject(mo, "epqosEgress", {"Burst":"10240", "HostControl":"full", "Rate":"line-rate", "Prio":"best-effort", "Dn":"org-root/org-ORG_TEST/ep-qos-BE/egress", "Name":""}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "epqosDefinition", {"PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/ep-qos-Bronze", "Name":"Bronze", "Descr":""})
	mo_1 = handle.AddManagedObject(mo, "epqosEgress", {"Burst":"10240", "HostControl":"none", "Rate":"line-rate", "Prio":"best-effort", "Dn":"org-root/org-ORG_TEST/ep-qos-Bronze/egress", "Name":""}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "epqosDefinition", {"PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/ep-qos-Silver", "Name":"Silver", "Descr":""})
	mo_1 = handle.AddManagedObject(mo, "epqosEgress", {"Burst":"10240", "HostControl":"none", "Rate":"line-rate", "Prio":"best-effort", "Dn":"org-root/org-ORG_TEST/ep-qos-Silver/egress", "Name":""}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "epqosDefinition", {"PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/ep-qos-Gold","Name":"Gold", "Descr":""})
	mo_1 = handle.AddManagedObject(mo, "epqosEgress", {"Burst":"10240", "HostControl":"none", "Rate":"line-rate", "Prio":"best-effort", "Dn":"org-root/org-ORG_TEST/ep-qos-Gold/egress", "Name":""}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "epqosDefinition", {"PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/ep-qos-Platinum", "Name":"Platinum", "Descr":""})
	mo_1 = handle.AddManagedObject(mo, "epqosEgress", {"Burst":"10240", "HostControl":"none", "Rate":"line-rate", "Prio":"best-effort", "Dn":"org-root/org-ORG_TEST/ep-qos-Platinum/egress", "Name":""}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "computeQual", {"PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/blade-qualifier-B200-M3-POOL", "Name":"B200-M3-POOL", "Descr":"Matches against the B200 M3 PID"})
	mo_1 = handle.AddManagedObject(mo, "computePhysicalQual", {"Dn":"org-root/org-ORG_TEST/blade-qualifier-B200-M3-POOL/physical", "Model":"UCSB-B200-M3"})
	handle.CompleteTransaction()

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	handle.AddManagedObject(obj, "computePoolingPolicy", {"Qualifier":"B200-M3-POOL", "Descr":"Pool Policy for B200 M3", "PolicyOwner":"local", "PoolDn":"org-root/org-ORG_TEST/compute-pool-B200-M3-POOL", "Dn":"org-root/org-ORG_TEST/pooling-policy-B200-M3-POOLPLCY", "Name":"B200-M3-POOLPLCY"})

	#TODO: Need to flush out the host firmware policy creation, or consider what it would take to initiate auto install for server FW
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	handle.AddManagedObject(obj, "firmwareComputeHostPack", {"StageSize":"0", "Mode":"staged", "PolicyOwner":"local", "Descr":"Host Firmware Policy for B200 M3 Servers", "IgnoreCompCheck":"yes", "RackBundleVersion":"", "UpdateTrigger":"immediate", "Dn":"org-root/org-ORG_TEST/fw-host-pack-B200M3-FW-PLCY", "BladeBundleVersion":"", "Name":"B200M3-FW-PLCY"})

	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	handle.AddManagedObject(obj, "lsmaintMaintPolicy", {"UptimeDisr":"user-ack", "Descr":"Maintenance Policy for User-Ack", "PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/maint-MAINT-USER-ACK", "Name":"MAINT-USER-ACK", "SchedName":""})


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "nwctrlDefinition", {"UplinkFailAction":"link-down", "Descr":"", "MacRegisterMode":"only-native-vlan", "PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/nwctrl-ESX_NETCTRL", "Name":"ESX_NETCTRL", "Cdp":"enabled"})
	mo_1 = handle.AddManagedObject(mo, "dpsecMac", {"PolicyOwner":"local", "Dn":"org-root/org-ORG_TEST/nwctrl-ESX_NETCTRL/mac-sec", "Name":"", "Descr":"", "Forge":"allow"}, True)
	handle.CompleteTransaction()

	#Rarely use local disks, so commenting this out for now.
	#obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	#handle.AddManagedObject(obj, "storageLocalDiskConfigPolicy", {"Mode":"raid-mirrored", "Dn":"org-root/org-ORG_TEST/local-disk-config-LOCALDISK_RAID1", "Descr":"", "PolicyOwner":"local", "FlexFlashRAIDReportingState":"disable", "ProtectConfig":"yes", "FlexFlashState":"disable", "Name":"LOCALDISK_RAID1"})



def createBootPolicy(ucs_ipaddr, ucs_username, ucs_passwd):

	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "lsbootPolicy", {"RebootOnUpdate":"no", "Descr":"Boot from SAN - ESXi", "PolicyOwner":"local", "EnforceVnicName":"yes", "Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX", "Name":"BFS-ESX"})
	mo_1 = handle.AddManagedObject(mo, "lsbootVirtualMedia", {"Access":"read-only", "Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX/read-only-vm", "Order":"1"})
	mo_2 = handle.AddManagedObject(mo, "lsbootStorage", {"Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX/storage", "Order":"2"}, True)
	mo_2_1 = handle.AddManagedObject(mo_2, "lsbootSanImage", {"Type":"primary", "Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX/storage/san-primary", "VnicName":"ESX-VHBA-A"})
	mo_2_1_1 = handle.AddManagedObject(mo_2_1, "lsbootSanImagePath", {"Type":"primary", "Wwn":"50:00:00:00:00:00:00:01", "Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX/storage/san-primary/path-primary", "Lun":"0"})
	mo_2_1_2 = handle.AddManagedObject(mo_2_1, "lsbootSanImagePath", {"Type":"secondary", "Wwn":"50:00:00:00:00:00:00:02","Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX/storage/san-primary/path-secondary", "Lun":"0"})
	mo_2_2 = handle.AddManagedObject(mo_2, "lsbootSanImage", {"Type":"secondary", "Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX/storage/san-secondary", "VnicName":"ESX-VHBA-B"})
	mo_2_2_1 = handle.AddManagedObject(mo_2_2, "lsbootSanImagePath", {"Type":"primary", "Wwn":"50:00:00:00:00:00:00:03", "Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX/storage/san-secondary/path-primary", "Lun":"0"})
	mo_2_2_2 = handle.AddManagedObject(mo_2_2, "lsbootSanImagePath", {"Type":"secondary", "Wwn":"50:00:00:00:00:00:00:04","Dn":"org-root/org-ORG_TEST/boot-policy-BFS-ESX/storage/san-secondary/path-secondary", "Lun":"0"})
	handle.CompleteTransaction()


def createTemplates(ucs_ipaddr, ucs_username, ucs_passwd):

	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "vnicLanConnTempl", {"IdentPoolName":"MAC-ESX-A", "Dn":"org-root/org-ORG_TEST/lan-conn-templ-ESX-MGMT-A", "QosPolicyName":"BE", "Descr":"ESXi Management - Fabric A", "PolicyOwner":"local", "NwCtrlPolicyName":"ESX_NETCTRL", "TemplType":"updating-template", "StatsPolicyName":"default", "Mtu":"1500", "PinToGroupName":"", "Name":"ESX-MGMT-A", "SwitchId":"A"})
	mo_1 = handle.AddManagedObject(mo, "vnicEtherIf", {"DefaultNet":"no", "Name":"VLAN123", "Dn":"org-root/org-ORG_TEST/lan-conn-templ-ESX-MGMT-A/if-VLAN123"}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "vnicLanConnTempl", {"IdentPoolName":"MAC-ESX-B", "Dn":"org-root/org-ORG_TEST/lan-conn-templ-ESX-MGMT-B", "QosPolicyName":"BE", "Descr":"ESXi Management - Fabric B", "PolicyOwner":"local", "NwCtrlPolicyName":"ESX_NETCTRL", "TemplType":"updating-template", "StatsPolicyName":"default", "Mtu":"1500", "PinToGroupName":"", "Name":"ESX-MGMT-B", "SwitchId":"B"})
	mo_1 = handle.AddManagedObject(mo, "vnicEtherIf", {"DefaultNet":"no", "Name":"VLAN123", "Dn":"org-root/org-ORG_TEST/lan-conn-templ-ESX-MGMT-B/if-VLAN123"}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "vnicSanConnTempl", {"StatsPolicyName":"default", "QosPolicyName":"", "Descr":"ESX vHBA - Fabric A", "PolicyOwner":"local", "IdentPoolName":"WWPN-ESX-A", "MaxDataFieldSize":"2048", "TemplType":"updating-template", "Dn":"org-root/org-ORG_TEST/san-conn-templ-ESX-VHBA-A", "PinToGroupName":"", "Name":"ESX-VHBA-A", "SwitchId":"A"})
	mo_1 = handle.AddManagedObject(mo, "vnicFcIf", {"Name":"VSAN_10", "Dn":"org-root/org-ORG_TEST/san-conn-templ-ESX-VHBA-A/if-default"}, True)
	handle.CompleteTransaction()


	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "vnicSanConnTempl", {"StatsPolicyName":"default", "QosPolicyName":"", "Descr":"ESX vHBA - Fabric B", "PolicyOwner":"local", "IdentPoolName":"WWPN-ESX-B", "MaxDataFieldSize":"2048", "TemplType":"updating-template", "Dn":"org-root/org-ORG_TEST/san-conn-templ-ESX-VHBA-B", "PinToGroupName":"", "Name":"ESX-VHBA-B", "SwitchId":"B"})
	mo_1 = handle.AddManagedObject(mo, "vnicFcIf", {"Name":"VSAN_20", "Dn":"org-root/org-ORG_TEST/san-conn-templ-ESX-VHBA-B/if-default"}, True)
	handle.CompleteTransaction()


	#TODO: Need to build in a function that properly orders vHBAs/vNICs on this template
	handle.StartTransaction()
	obj = handle.GetManagedObject(None, None, {"Dn":"org-root/org-ORG_TEST"})
	mo = handle.AddManagedObject(obj, "lsServer", {"PowerPolicyName":"default", "Uuid":"0", "SrcTemplName":"", "MgmtFwPolicyName":"", "AgentPolicyName":"", "Name":"SPT-ESX", "VconProfileName":"", "IdentPoolName":"UUID-ESX", "UsrLbl":"", "Type":"updating-template", "BiosProfileName":"", "Descr":"Service Profile Template for ESXi Servers", "MgmtAccessPolicyName":"", "SolPolicyName":"", "PolicyOwner":"local", "MaintPolicyName":"MAINT-USER-ACK", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX", "LocalDiskPolicyName":"default", "HostFwPolicyName":"B200M3-FW-PLCY", "ScrubPolicyName":"", "DynamicConPolicyName":"", "BootPolicyName":"BFS-ESX", "ExtIPPoolName":"ext-mgmt", "ExtIPState":"pooled", "StatsPolicyName":"default"})
	mo_1 = handle.AddManagedObject(mo, "lsVConAssign", {"Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/assign-ethernet-vnic-ESX-MGMT-A", "VnicName":"ESX-MGMT-A", "Transport":"ethernet", "AdminVcon":"any", "Order":"1"}, True)
	mo_2 = handle.AddManagedObject(mo, "lsVConAssign", {"Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/assign-ethernet-vnic-ESX-MGMT-B", "VnicName":"ESX-MGMT-B", "Transport":"ethernet", "AdminVcon":"any", "Order":"2"}, True)
	mo_3 = handle.AddManagedObject(mo, "lsVConAssign", {"Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/assign-fc-vnic-ESX-VHBA-A","VnicName":"ESX-VHBA-A", "Transport":"fc", "AdminVcon":"any", "Order":"3"}, True)
	mo_4 = handle.AddManagedObject(mo, "lsVConAssign", {"Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/assign-fc-vnic-ESX-VHBA-B","VnicName":"ESX-VHBA-B", "Transport":"fc", "AdminVcon":"any", "Order":"4"}, True)
	mo_5 = handle.AddManagedObject(mo, "vnicEther", {"Order":"1", "Name":"ESX-MGMT-A", "NwTemplName":"ESX-MGMT-A", "IdentPoolName":"", "AdaptorProfileName":"VMWare", "SwitchId":"A", "AdminVcon":"any", "Addr":"derived", "QosPolicyName":"", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/ether-ESX-MGMT-A", "Mtu":"1500", "NwCtrlPolicyName":"", "PinToGroupName":"", "StatsPolicyName":"default"})
	mo_6 = handle.AddManagedObject(mo, "vnicEther", {"Order":"2", "Name":"ESX-MGMT-B", "NwTemplName":"ESX-MGMT-B", "IdentPoolName":"", "AdaptorProfileName":"VMWare", "SwitchId":"A", "AdminVcon":"any", "Addr":"derived", "QosPolicyName":"", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/ether-ESX-MGMT-B", "Mtu":"1500", "NwCtrlPolicyName":"", "PinToGroupName":"", "StatsPolicyName":"default"})
	mo_7 = handle.AddManagedObject(mo, "vnicFc", {"Order":"3", "Name":"ESX-VHBA-A", "MaxDataFieldSize":"2048", "IdentPoolName":"", "AdaptorProfileName":"VMWare", "SwitchId":"A", "AdminVcon":"any", "Addr":"derived", "QosPolicyName":"", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/fc-ESX-VHBA-A", "PersBind":"disabled", "StatsPolicyName":"default", "PersBindClear":"no", "PinToGroupName":"", "NwTemplName":"ESX-VHBA-A"})
	mo_7_1 = handle.AddManagedObject(mo_7, "vnicFcIf", {"Name":"", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/fc-ESX-VHBA-A/if-default"}, True)
	mo_8 = handle.AddManagedObject(mo, "vnicFc", {"Order":"4", "Name":"ESX-VHBA-B", "MaxDataFieldSize":"2048", "IdentPoolName":"", "AdaptorProfileName":"VMWare", "SwitchId":"A", "AdminVcon":"any", "Addr":"derived", "QosPolicyName":"", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/fc-ESX-VHBA-B", "PersBind":"disabled", "StatsPolicyName":"default", "PersBindClear":"no", "PinToGroupName":"", "NwTemplName":"ESX-VHBA-B"})
	mo_8_1 = handle.AddManagedObject(mo_8, "vnicFcIf", {"Name":"", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/fc-ESX-VHBA-B/if-default"}, True)
	mo_9 = handle.AddManagedObject(mo, "vnicFcNode", {"IdentPoolName":"WWNN-ESX", "Addr":"pool-derived", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/fc-node"}, True)
	mo_10 = handle.AddManagedObject(mo, "lsRequirement", {"Qualifier":"B200-M3-POOL", "Name":"B200-M3-POOL", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/pn-req", "RestrictMigration":"no"}, True)
	mo_11 = handle.AddManagedObject(mo, "lsPower", {"State":"admin-up", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/power"}, True)
	mo_12 = handle.AddManagedObject(mo, "fabricVCon", {"Transport":"ethernet,fc", "Placement":"physical", "Select":"all", "Fabric":"NONE", "InstType":"auto", "Share":"shared", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/vcon-1", "Id":"1"}, True)
	mo_13 = handle.AddManagedObject(mo, "fabricVCon", {"Transport":"ethernet,fc", "Placement":"physical", "Select":"all", "Fabric":"NONE", "InstType":"auto", "Share":"shared", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/vcon-2", "Id":"2"}, True)
	mo_14 = handle.AddManagedObject(mo, "fabricVCon", {"Transport":"ethernet,fc", "Placement":"physical", "Select":"all", "Fabric":"NONE", "InstType":"auto", "Share":"shared", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/vcon-3", "Id":"3"}, True)
	mo_15 = handle.AddManagedObject(mo, "fabricVCon", {"Transport":"ethernet,fc", "Placement":"physical", "Select":"all", "Fabric":"NONE", "InstType":"auto", "Share":"shared", "Dn":"org-root/org-ORG_TEST/ls-SPT-ESX/vcon-4", "Id":"4"}, True)
	handle.CompleteTransaction()

def createSPsfromTemplate():

	dnSet = DnSet()
	dn = Dn()
	dn.setattr("Value","ESXi-01")
	dnSet.AddChild(dn)
	handle.LsInstantiateNNamedTemplate("org-root/org-ORG_TEST/ls-SPT-ESX", dnSet, "org-root/org-ORG_TEST", YesOrNo.FALSE)








