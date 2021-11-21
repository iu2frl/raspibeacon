#!/bin/python
# 
# Copyright 2010 Tom Hayward IU2FRL <iu2frl.mn@gmail.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from socket import *
from datetime import datetime
import psutil
from gpiozero import CPUTemperature

# APRS-IS login info
serverHost = 'rotate.aprs2.net'
serverPort = 14580
aprsUser = 'IU2FRL-M1'
aprsPass = '23229'
aprsLongitude = '4510.35N'
aprsLatitude = '01047.11E'
symbol = '?'

# Get current time and date
dateTimeObj = datetime.now()
aprsTime = dateTimeObj.strftime("%H%M%S")

# Get CPU usage
cpuUsage = str(psutil.cpu_percent(4))

# Get CPU Temperature
cpuTemp = CPUTemperature()

# APRS packet
callsign = 'IU2FRL'
payload = '@' + aprsTime + 'z' + aprsLongitude + '/' + aprsLatitude + symbol + 'test python script ' + 'CPU: ' + cpuUsage + '%' + 'Temp: ' + cpuTemp + '°C'

# create socket & connect to server
sSock = socket(AF_INET, SOCK_STREAM)
sSock.connect((serverHost, serverPort))
# logon
logonString = 'user ' + aprsUser + ' pass ' + aprsPass + ' vers KD7LXL-Python 0.1\n' 
sSock.sendall(logonString.encode('utf-8'))
# send packet
packetString = aprsUser + '>APRS,TCPIP*:' + payload + '\n'
sSock.sendall(packetString.encode('utf-8'))
# close socket
sSock.shutdown(0)
sSock.close()
