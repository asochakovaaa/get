import pathlib
import shutil
import os
import requests
path = str(pathlib.Path().absolute()) + "\\ocean"
print(path)

try:
     shutil.rmtree(path)
except OSError:
    print("Deletion of the directory %s failed" % path)
else:
    print("Successfully deleted the directory %s" % path)

try:
    os.mkdir(path)
except OSError:
    print (" Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)
    
for date in range(246, 261, 1):
        name = str(date) + '.4km.png'
        r = requests.get('https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/CHL/L3/2020/' + str(date) + '/' + 'A2020' + str(date) + '.L3m_DAY_CHL_chlor_a_' + '4km.nc.png' , allow_redirects=True)
        open(path + '/' + name, 'wb').write(r.content)