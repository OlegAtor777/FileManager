# файловый менеджер
import os
import manager_defs
root = manager_defs.r00t
try:
    os.mkdir('root')
except FileExistsError:
    pass
os.chdir(root)

##############################################################################
# Основной цикл программы 
manager_defs.helpp(None)
while True:
    if manager_defs.listen()=='kaboom':
        break
    



    