#-----------------------------------------------
print ("Added this file for collaboration from Local Machine")
#-----------------------------------------------
print ("Added 2nd line")
#-----------------------------------------------
print ("Added 3rd line")
#-----------------------------------------------
print ("Added 4th line from User2 local system")
#-----------------------------------------------
print ("Added 5th line from User2 local system")
#-----------------------------------------------
print ("Added 6th line from User2 local system")
print ("Added 6th line from User2 local system")
#-----------------------------------------------
print ("Added 7th line from User2 local system")

interface GigabitEthernet1/0/49
 description PTP(IP-ACCESS-PTP-NNEKA-RESIDENCE-10.110.0.223)
 switchport access vlan 21
 switchport trunk allowed vlan 500,738
 switchport mode trunk
 load-interval 30