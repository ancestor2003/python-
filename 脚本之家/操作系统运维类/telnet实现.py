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
   
  msg.append(tn.expect(['login:'],5))
  tn.write(user+'\n')
