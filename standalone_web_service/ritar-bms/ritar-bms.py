#!/usr/bin/env python3

# by Oleh Mamont (C) 2025
# 
# Ritar BAT-5KWH-51.2V (10kWh model may work too)
#
# free for use and modifications

import time
import binascii
import socket
import xml.etree.ElementTree as ET

###########################################
########## network RS485 gateway ##########
###########################################

# ethernet rs485 device
# IP
TCP_IP = '192.168.5.29'
# port
TCP_PORT = 50500

# work buffer size
BUFFER_SIZE = 1024

#################################
########## QUERY HACKS ##########
#################################

# SOC query hack. battery #1 by dip switch - 1000
bat_1_get_block_voltage = b'\x01\x03\x00\x00\x00\x10\x44\x06'

# cells query hack. battery #1 by dip switch - 1000
bat_1_get_cells_voltage = b'\x01\x03\x00\x28\x00\x10\xc4\x0e'

# SOC query hack. battery #2 by dip switch - 0100
bat_2_get_block_voltage = b'\x02\x03\x00\x00\x00\x10\x44\x35'

# cells query hack. battery #2 by dip switch - 0100
bat_2_get_cells_voltage = b'\x02\x03\x00\x28\x00\x10\xc4\x3d'

##########################################
########## open stream to RS485 ##########
##########################################

# open stream to rs485 device
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# sending query hack to battery #1
s.send(bat_1_get_block_voltage)

# getting ascii string with SOC voltage from battery 1
bat_1_block_voltage = s.recv(BUFFER_SIZE)

time.sleep(1)

# sending query hack to battery #1
s.send(bat_1_get_cells_voltage)

# getting ascii string with cells voltages from battery 1
bat_1_cells_voltage = s.recv(BUFFER_SIZE)

time.sleep(1)

# sending query hack to battery #2
s.send(bat_2_get_block_voltage)

# getting ascii string with cells voltages from battery 1
bat_2_block_voltage = s.recv(BUFFER_SIZE)

time.sleep (1)

# sending query hack to battery #2
s.send(bat_2_get_cells_voltage)

# getting ascii string with cells voltages from battery 2
bat_2_cells_voltage = s.recv(BUFFER_SIZE)

# close stream to rs485 device
s.close()

###################################
########## battery 1 SOC ##########
###################################

# converting battery #1 response to hex for future operations
bat_1_block_voltage_hex = binascii.hexlify(bat_1_block_voltage)

# connection test, get hex string response print to console
#print ("received data:", bat_1_block_voltage_hex)

bat_1_voltage_hex = bat_1_block_voltage_hex[10:-60]
bat_1_charged_hex = bat_1_block_voltage_hex[14:-56]
bat_1__cycle__hex = bat_1_block_voltage_hex[34:-36]

# calculate from hex response

bat_1_voltage_dec = int(bat_1_voltage_hex, 16)
bat_1_charged_dec = int(bat_1_charged_hex, 16)
bat_1__cycle__dec = int(bat_1__cycle__hex, 16)

#####################################
########## battery 1 cells ##########
#####################################

# converting battery #1 response to hex for future operations
bat_1_cells_voltage_hex = binascii.hexlify(bat_1_cells_voltage)

# connection test, get hex string response print to console
#print ("received data:", bat_1_cells_voltage_hex)

# split hex string by cells

bat_1_cell_1_hex = bat_1_cells_voltage_hex[6:-64]
bat_1_cell_2_hex = bat_1_cells_voltage_hex[10:-60]
bat_1_cell_3_hex = bat_1_cells_voltage_hex[14:-56]
bat_1_cell_4_hex = bat_1_cells_voltage_hex[18:-52]
bat_1_cell_5_hex = bat_1_cells_voltage_hex[22:-48]
bat_1_cell_6_hex = bat_1_cells_voltage_hex[26:-44]
bat_1_cell_7_hex = bat_1_cells_voltage_hex[30:-40]
bat_1_cell_8_hex = bat_1_cells_voltage_hex[34:-36]
bat_1_cell_9_hex = bat_1_cells_voltage_hex[38:-32]
bat_1_cell_10_hex = bat_1_cells_voltage_hex[42:-28]
bat_1_cell_11_hex = bat_1_cells_voltage_hex[46:-24]
bat_1_cell_12_hex = bat_1_cells_voltage_hex[50:-20]
bat_1_cell_13_hex = bat_1_cells_voltage_hex[54:-16]
bat_1_cell_14_hex = bat_1_cells_voltage_hex[58:-12]
bat_1_cell_15_hex = bat_1_cells_voltage_hex[62:-8]
bat_1_cell_16_hex = bat_1_cells_voltage_hex[66:-4]

# calculate voltage from hex response

bat_1_cell_1_dec = int(bat_1_cell_1_hex, 16)
bat_1_cell_2_dec = int(bat_1_cell_2_hex, 16)
bat_1_cell_3_dec = int(bat_1_cell_3_hex, 16)
bat_1_cell_4_dec = int(bat_1_cell_4_hex, 16)
bat_1_cell_5_dec = int(bat_1_cell_5_hex, 16)
bat_1_cell_6_dec = int(bat_1_cell_6_hex, 16)
bat_1_cell_7_dec = int(bat_1_cell_7_hex, 16)
bat_1_cell_8_dec = int(bat_1_cell_8_hex, 16)
bat_1_cell_9_dec = int(bat_1_cell_9_hex, 16)
bat_1_cell_10_dec = int(bat_1_cell_10_hex, 16)
bat_1_cell_11_dec = int(bat_1_cell_11_hex, 16)
bat_1_cell_12_dec = int(bat_1_cell_12_hex, 16)
bat_1_cell_13_dec = int(bat_1_cell_13_hex, 16)
bat_1_cell_14_dec = int(bat_1_cell_14_hex, 16)
bat_1_cell_15_dec = int(bat_1_cell_15_hex, 16)
bat_1_cell_16_dec = int(bat_1_cell_16_hex, 16)


###################################
########## battery 2 SOC ##########
###################################

# converting battery #2 response to hex for future operations
bat_2_block_voltage_hex = binascii.hexlify(bat_2_block_voltage)

# connection test, get hex string response print to console
#print ("received data:", bat_2_block_voltage_hex)

# split hex string

bat_2_voltage_hex = bat_2_block_voltage_hex[10:-60]
bat_2_charged_hex = bat_2_block_voltage_hex[14:-56]
bat_2__cycle__hex = bat_2_block_voltage_hex[34:-36]

# calculate from hex response

bat_2_voltage_dec = int(bat_2_voltage_hex, 16)
bat_2_charged_dec = int(bat_2_charged_hex, 16)
bat_2__cycle__dec = int(bat_2__cycle__hex, 16)

#####################################
########## battery 2 cells ##########
#####################################

# converting battery #2 response to hex for future operations
bat_2_cells_voltage_hex = binascii.hexlify(bat_2_cells_voltage)

# connection test, get hex string response print to console
#print ("received data:", bat_2_cells_voltage_hex)

# split hex string by cells

bat_2_cell_1_hex = bat_2_cells_voltage_hex[6:-64]
bat_2_cell_2_hex = bat_2_cells_voltage_hex[10:-60]
bat_2_cell_3_hex = bat_2_cells_voltage_hex[14:-56]
bat_2_cell_4_hex = bat_2_cells_voltage_hex[18:-52]
bat_2_cell_5_hex = bat_2_cells_voltage_hex[22:-48]
bat_2_cell_6_hex = bat_2_cells_voltage_hex[26:-44]
bat_2_cell_7_hex = bat_2_cells_voltage_hex[30:-40]
bat_2_cell_8_hex = bat_2_cells_voltage_hex[34:-36]
bat_2_cell_9_hex = bat_2_cells_voltage_hex[38:-32]
bat_2_cell_10_hex = bat_2_cells_voltage_hex[42:-28]
bat_2_cell_11_hex = bat_2_cells_voltage_hex[46:-24]
bat_2_cell_12_hex = bat_2_cells_voltage_hex[50:-20]
bat_2_cell_13_hex = bat_2_cells_voltage_hex[54:-16]
bat_2_cell_14_hex = bat_2_cells_voltage_hex[58:-12]
bat_2_cell_15_hex = bat_2_cells_voltage_hex[62:-8]
bat_2_cell_16_hex = bat_2_cells_voltage_hex[66:-4]

# calculate voltage from hex response

bat_2_cell_1_dec = int(bat_2_cell_1_hex, 16)
bat_2_cell_2_dec = int(bat_2_cell_2_hex, 16)
bat_2_cell_3_dec = int(bat_2_cell_3_hex, 16)
bat_2_cell_4_dec = int(bat_2_cell_4_hex, 16)
bat_2_cell_5_dec = int(bat_2_cell_5_hex, 16)
bat_2_cell_6_dec = int(bat_2_cell_6_hex, 16)
bat_2_cell_7_dec = int(bat_2_cell_7_hex, 16)
bat_2_cell_8_dec = int(bat_2_cell_8_hex, 16)
bat_2_cell_9_dec = int(bat_2_cell_9_hex, 16)
bat_2_cell_10_dec = int(bat_2_cell_10_hex, 16)
bat_2_cell_11_dec = int(bat_2_cell_11_hex, 16)
bat_2_cell_12_dec = int(bat_2_cell_12_hex, 16)
bat_2_cell_13_dec = int(bat_2_cell_13_hex, 16)
bat_2_cell_14_dec = int(bat_2_cell_14_hex, 16)
bat_2_cell_15_dec = int(bat_2_cell_15_hex, 16)
bat_2_cell_16_dec = int(bat_2_cell_16_hex, 16)


###################################
######## API output ###############
###################################


# data array to save in API file
ritar_bms = {
# battery 1 soc
    'b1volt': bat_1_voltage_dec,
    'b1soc': bat_1_charged_dec,
    'b1cycl': bat_1__cycle__dec,
# battery 1 cells
    'b1c1': bat_1_cell_1_dec,
    'b1c2': bat_1_cell_2_dec,
    'b1c3': bat_1_cell_3_dec,
    'b1c4': bat_1_cell_4_dec,
    'b1c5': bat_1_cell_5_dec,
    'b1c6': bat_1_cell_6_dec,
    'b1c7': bat_1_cell_7_dec,
    'b1c8': bat_1_cell_8_dec,
    'b1c9': bat_1_cell_9_dec,
    'b1c10': bat_1_cell_10_dec,
    'b1c11': bat_1_cell_11_dec,
    'b1c12': bat_1_cell_12_dec,
    'b1c13': bat_1_cell_13_dec,
    'b1c14': bat_1_cell_14_dec,
    'b1c15': bat_1_cell_15_dec,
    'b1c16': bat_1_cell_16_dec
}

# Create the root element
root = ET.Element('response')
# Add data to the XML structure
for key, value in ritar_bms.items():
    child = ET.SubElement(root, key)
    child.text = str(value)
# Create a tree from the root element
tree = ET.ElementTree(root)
# Write the tree to an XML file
with open('/ritar-bms/web_ui/api/ritar-bat-1.xml', 'wb') as file:
    tree.write(file, encoding="utf-8", xml_declaration=False)

time.sleep (2)

# data array to save in API file
ritar_bms2 = {
# battery 2 soc
    'b2volt': bat_2_voltage_dec,
    'b2soc': bat_2_charged_dec,
    'b2cycl': bat_2__cycle__dec,
# battery 2 cells
    'b2c1': bat_2_cell_1_dec,
    'b2c2': bat_2_cell_2_dec,
    'b2c3': bat_2_cell_3_dec,
    'b2c4': bat_2_cell_4_dec,
    'b2c5': bat_2_cell_5_dec,
    'b2c6': bat_2_cell_6_dec,
    'b2c7': bat_2_cell_7_dec,
    'b2c8': bat_2_cell_8_dec,
    'b2c9': bat_2_cell_9_dec,
    'b2c10': bat_2_cell_10_dec,
    'b2c11': bat_2_cell_11_dec,
    'b2c12': bat_2_cell_12_dec,
    'b2c13': bat_2_cell_13_dec,
    'b2c14': bat_2_cell_14_dec,
    'b2c15': bat_2_cell_15_dec,
    'b2c16': bat_2_cell_16_dec
}

# Create the root element
root = ET.Element('response')
# Add data to the XML structure
for key, value in ritar_bms2.items():
    child = ET.SubElement(root, key)
    child.text = str(value)
# Create a tree from the root element
tree = ET.ElementTree(root)
# Write the tree to an XML file
with open('/ritar-bms/web_ui/api/ritar-bat-2.xml', 'wb') as file:
    tree.write(file, encoding="utf-8", xml_declaration=False)

