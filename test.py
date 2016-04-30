import commands

a=commands.getoutput('curl -I  http://127.0.0.1:5000')
if('HTTP/1.0 200 OK' == (a.splitlines()[5])):
	print "OK"
else:
	print "Not OK"
