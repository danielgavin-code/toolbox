#!/usr/bin/python

#
#     Title    : toolbox_Backup.py 
#     Version  : 1.0
#     Date     : 11 October 2024 
#     Author   : Daniel Gavin
#
#     Function : Archives inputed file to bacxkup directory. 
#
#     Modification History
#
#     Date     : 11 October 2024 
#     Author   : Daniel Gavin
#     Changes  : New file.
#
#     Date     : 7 June 2025
#     Author   : Daniel Gavin
#     Changes  : Ported to python3.
#
#     Date     :
#     Author   :
#     Changes  :
#

import os
import sys
import datetime

BACKUP_PATH = '/Users/dgavin/Backup/'

###############################################################################
#
# Procedure   : CheckPath() 
#
# Description : Checks if backup path exists.
#             : Creates path if it does not exist. 
#
# Input       : path - diretory path of backup directory 
#
# Returns     : -none- 
#
###############################################################################

def CheckPath(path):

    if not os.path.isdir(path):
        print("[INFO] Creating path: " + path)
        os.system('mkdir ' + path)


###############################################################################
#
# Procedure   : Main
#
# Description : Entry point. 
#
# Input       : -none-
#
# Returns     : -none- 
#
###############################################################################

def Main():

    if len(sys.argv) < 2:
        print("[ERROR] No file provided.")
        sys.exit(1)

    backupFile = sys.argv[1]
    CheckPath(BACKUP_PATH)

    today     = datetime.datetime.today()
    timestamp = today.strftime('%Y%m%d.%H%M%S')

    backupName     = os.path.basename(backupFile) + "." + timestamp
    fullBackupPath = os.path.join(BACKUP_PATH, backupName)

    cmd = 'cp -p "{}" "{}"'.format(backupFile, fullBackupPath)
    os.system(cmd)


if __name__ == "__main__":
    Main()
