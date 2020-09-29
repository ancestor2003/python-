#url:https://www.jb51.net/article/14305.htm
def telnetdo(host=none,user=none,pass=none,command=none):
  import telnetlib
  import sys
  if not host:
    try:
      host=sys.argv[1]
      user=sys.argv[2]
      pass=sys.argv[3]
      command=sys.argv[4]
    except:
      print('usage:telnetdo.py host user pass command')
      return
msg=['debug messges:\n']
tn=telnetlib.telnet()
try:
  tn.open(host)
  except:
    print('can not open host')
    retrun
msg.append(tn.expect(['login:'],5))
tn.write(user+'\n')
if pass:
  msg.append(tn.expect(['password:'],5))
  tn.write(pass+'\n')
msg.append(tn.expect([user],5))
tn.close()
del tn
return msg[len(msg)-1][2]
if __name__ == 'main'
print telnetdo()
