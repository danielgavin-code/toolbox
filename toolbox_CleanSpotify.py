#!/usr/bin/python3

#           
#     Title    : toolbox_CleanSpotify.py 
#     Version  : 1.0
#     Date     : 22 April 2022 
#     Author   : Daniel Gavin
#
#     Function : Fix Spotify not loading on a Mac. 
#              : - Kill all Spotify PIDs. 
#              : - Remove Library caches. 
#              : - Forces rebuild of deleted areas on startup. 
#
#     Modification History
#
#     Date     : 22 April 2022 
#     Author   : Daniel Gavin
#     Changes  : New file.
# 
#     Date     :
#     Author   :
#     Changes  :
# 

import os

print("[INFO] Starting.\n")

print("[INFO] Getting spotify PIDs.")
cmd  = "ps -eaf | grep -i spotify | grep -v grep | grep -v CleanSpotify | awk '{print $2}' | tr '\n' ' '"
pids = os.popen(cmd).readline().rstrip()

if pids:
    print("[INFO] Killing Spotify PIDs (" + pids + ").\n")
    cmd = "kill -9 " + pids
    cmdOut = os.popen(cmd)

else:
    print("[INFO] No PIDs\n")

print("[INFO] Deleting .com.spotify.*\n")
cmd = 'rm -rf /Users/dgavin/Library/Caches/com.spotify.*'
cmd_out = os.popen(cmd)

print("[INFO] Deleting Application Support files.\n")
cmd = "rm -rf '/Users/dgavin/Library/Application Support/Spotify'"
cmd_out = os.popen(cmd)

print("[INFO] Finished")
