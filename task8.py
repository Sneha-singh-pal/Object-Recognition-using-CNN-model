#!/usr/bin/python3
print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("x")


if plate_no == "EER.1500":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Priya Gupta 
    License No : 5283961008
    Make / Model : Range Rover
    Registration Date : 4/12/2007
    Registering Authority : Maharashtra , INDIA
    Fuel Type : CNG
    Engine No : IVL3K1734544
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 6/13/2020
    Fitness Upto : 4/12/2028
    </pre>''')
    print("</body>")

elif plate_no == "BL 6339":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Mohak khare
    License No : 178363357802
    Make / Model : Maruti Suzuki
    Registration Date : 1/12/2014
    Registering Authority : Andhra Pradesh, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 3/10/2021
    Fitness Upto : 8/12/2029
    </pre>''')
    print("</body>")

elif plate_no == "MH13 BN8454":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Shanya Saxena
    License No : 735382528936
    Make / Model : Audi A3
    Registration Date : 1/12/2014
    Registering Authority : MANDSAUR-Solapur, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "MH.12FK.7368":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : Rohan Shukla
    License No : 735382528936
    Make / Model : HYUNDAI
    Registration Date : 8/12/2001
    Registering Authority : Maharashtra-Mumbai, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 6/13/2010
    Fitness Upto : 11/8/2020
    </pre>''')
    print("</body>")


else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
