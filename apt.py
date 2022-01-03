import os
import sys
#gets packages you want to install
packages = sys.argv
del packages[0]
auto = True
remove = False
num = 0
for x in packages:
    if x == "-a":
        auto = False
        del packages[num]
    if x == "-r":
        remove = True
        del packages[num]
    num = 1 + num

#turns the pakcages into a string with spacing
def pkglist(s):
    str = ""
    for ele in s:
        str += ele
        str += ' '
    return str

#checks to see if to even attepmt to install packages and tell the user if no packages will be installed or to tell them and procide or not
if len(packages) == 0:
    print("there are no packages to be installed")

else:
    if remove == True:
        print("these are the packages to be removed continue?", packages, " y/n:  ",end='')
    else:
        print("these are the packages to be downloaded continue?", packages, " y/n: ",end='')
#checks to proceed or not
    while True:
        ny = input("continue?   :")
        if ny == 'n' or ny == 'N':
            os.system('exit');
            sys.exit()
        elif ny == 'y' or ny == 'Y':
            break
    print(ny)

#updates ,upgrades and if there were packages to be install then it installs them
print("current amount of installed pakcages ", os.system('dpkg --list | wc --lines'))


print("apt update \n\n\n")
os.system('apt update')

print("apt upgrade\n\n\n")
os.system('apt upgrade')

if len(packages) > 0:
    if remove == True:
        print("apt remove\n\n\n")
        os.system('apt remove ' + pkglist(packages))
    else:
        print("apt install\n\n\n ",pkglist(packages))
        os.system('apt install ' + pkglist(packages))
if auto == True:
    print("apt autoremove\n\n\n")
    os.system('apt autoremove')

os.system('exit')
