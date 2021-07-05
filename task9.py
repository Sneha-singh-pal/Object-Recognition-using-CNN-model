#!/usr/bin/python3 


import cgi
import subprocess as sb

print("content-type: text/html")
print()

print('''<style>
pre{
    color: black;
    font-weight: bold;
    font-size: 20px;
}
</style>''')


fs = cgi.FieldStorage()

cmd = fs.getvalue("commands")
name = fs.getvalue("name") 
replica = fs.getvalue("replica")
port = fs.getvalue("port")

#cmd = input("enter req...")
#name = input("pod name : ")
#replica = input("replica : ")
#port = input("port : ")

if("all" in cmd ) and ("pods" in cmd):
    output = sb.getoutput("kubectl get pods --kubeconfig admin.conf")    
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")
    
elif("all" in cmd) and ("deployments" in cmd) :
    output = sb.getoutput("kubectl get deployment --kubeconfig admin.conf")
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif(("create" in cmd) or ("launch" in cmd )) and ("pod" in cmd ):
    output = sb.getoutput("kubectl run {} --image=centos:latest --kubeconfig admin.conf".format(name))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("deployment" in cmd) and ("create" in cmd ):
    output = sb.getoutput("kubectl create deployment {} --image=centos:latest --kubeconfig admin.conf ".format(name))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("deployment" in cmd) and ("expose") and ("port number"):
    output = sb.getoutput("kubectl expose deployment {} --port={} --type=NodePort --kubeconfig admin.conf ".format(name,port))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("create" in cmd ) or ("scale" in cmd ) and (("replica" in cmd ) or ("deployment" in cmd )):
    output = sb.getoutput("kubectl scale deployment  {} --replicas={} --kubeconfig admin.conf ".format(name,replica))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif ("delete" in cmd ) and ("pod" in cmd):
    output = sb.getoutput("kubectl delete pods {} --kubeconfig admin.conf".format(name))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("delete" in cmd ) and ("deployment" in cmd ):
    output = sb.getoutput("kubectl delete deployment {}  --kubeconfig admin.conf" .format(name))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>Invelid Input...</pre>")
    print("</body>")









#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print()

f=cgi.FieldStorage()
cmd=f.getvalue("x")

if (("hey" in cmd)or("please" in cmd))and(("create"in cmd)or("run"in cmd))and(("pod" in cmd)):
	print(sp.getoutput("sudo kubectl run web-test --image=httpd --kubeconfig admin.conf"))


elif (("can" in cmd))and(("you" in cmd))and(("create" in cmd)or("deploy" in cmd)or("launch" in cmd)or("run" in cmd)) and (("deployment" in cmd)):
	print(sp.getoutput("sudo kubectl create deployment web-test-79c7d95567-ncdsw --image=httpd --kubeconfig admin.conf"))


elif (("describe"in cmd)or("show"in cmd))and(("info"in cmd))and(("pod" in cmd)):
	print(sp.getoutput("sudo kubectl describe pod web-test --kubeconfig admin.conf"))


elif (("please"in cmd)or("can" in cmd))and(("expose"in cmd))and(("deployment" in cmd)or("pod" in cmd)):
	print(sp.getoutput("sudo kubectl expose deployment web-test-79c7d95567-ncdsw  --type=NodePort --port=80 --kubeconfig admin.conf"))


elif (("hey" in cmd)or("i" in cmd))and(("want" in cmd)or("please" in cmd))and(("scale"in cmd)or("increase" in cmd))and(("replica"in cmd)or("pods" in cmd)):
	print(sp.getoutput("sudo kubectl scale deployment web-test-79c7d95567-ncdsw --replicas=5 --kubeconfig admin.conf"))


elif (("i" in cmd)and("want" in cmd))and(("remove" in cmd)or("delete"in cmd))and(("envirnoment" in cmd)or("deployments" in cmd)):
	print(sp.getoutput("sudo kubectl delete all --all --kubeconfig admin.conf")



elif (("hey" in cmd)or("please" in cmd))and(("show" in cmd)or("display" in cmd))and(("pods"in cmd)or("pod" in cmd)or("containers" in cmd)):
	print(sp.getoutput("sudo kubectl get pod --kubeconfig admin.conf")



elif(("please" in cmd))and(("delete"in cmd)or("remove"in cmd))and(("deployment"in cmd)):
 	print(sp.getoutput("sudo kubectl delete deployment web-test-79c7d95567-ncdsw --kubeconfig admin.conf"))



elif (("please" in cmd))and(("delete"in cmd)or("remove"in cmd))and(("pod"in cmd)):
	print(sp.getoutput("sudo kubectl delete pod web-test --kubeconfig admin.conf"))


else:
	print("something went wrong , Please try again")
