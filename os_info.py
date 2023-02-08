import os
from sys import platform
def os_info():
    if platform == "linux" or platform == "linux2":   # linux
        pc_item = ('sysname', 'nodename', 'release', 'version', 'machine')
        for i in range(len(pc_item)):
            print('{:<8}: {:}'.format(pc_item[i], os.uname()[i]))
        #print('{:<8}: {:}'.format('CUDA ver.', os.environ['CUDA_VERSION']))
        #print('{:<8}: {:}'.format('NV_CUDNN', os.environ['NV_CUDNN_PACKAGE']))
    elif platform == "darwin":  # OS X
        print(f'\nПлатформа MacOS [{platform}]')
    elif platform == "win32":   # Windows...
        print(f'\nПлатформа MS Windows [{platform}]')

