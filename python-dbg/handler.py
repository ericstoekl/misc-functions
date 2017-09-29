from remote_pdb import RemotePdb

def handle(st):
    RemotePdb('0.0.0.0', 4444).set_trace()
    print(st)
