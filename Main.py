## http://pymssql.org/en/latest/index.html
import pymssql

server = '10.10.20.25'
user = 'sa'
password = '!Soyut8745'

pf = 0.9  # power factor
pfave = 0.82  # power factor for averages

sqr3 = 1.732050808  # squareroot of 3

conn = pymssql.connect(server, user, password, 'WINDTURBINE')
cursor = conn.cursor()

cursor.execute('select * from WTPLCTAGS where PACALTERNATORCURRENTL2 > 0.0 and LOWSPEEDRPM < 30.0;')
row = cursor.fetchone()

while row:
    V1 = row[24]
    V2 = row[25]
    V3 = row[26]
    VAVE = (V1 + V2 + V3) / 3

    I1 = row[27]
    I2 = row[28]
    I3 = row[29]
    IAVE = (I1 + I2 + I3) / 3

    kWave = 0.0
    kWave = VAVE * IAVE * pf * sqr3 / 1000.0

    kwCum = 0.0
    kwCum = (V1 * I1 * pf / 1000) + (V2 * I2 * pf / 1000) + (V3 * I3 * pf / 1000)

    print("ID=%s, kW average=%f, kW cumulative=%f" % (row[0], kWave, kwCum))
    row = cursor.fetchone()

conn.close()
