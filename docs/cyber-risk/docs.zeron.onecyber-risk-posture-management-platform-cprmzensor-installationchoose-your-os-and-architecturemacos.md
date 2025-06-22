  1. [Zensor Installation](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation)
  2. [Choose your OS & architecture](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture)


# MacOS
**Steps to install zensor in Mac :**
**On your Mac, do one of the following :**
  * Click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal 
  * In the Finder , open the `/Applications/Utilities` folder, then double-click Terminal 


Run the Install via CLI command starting with [curl -so] that is for installation of Zensor 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F7pcaHUc4LFvjhUhw9CDa%252Fimage-11-b4a6b20b763d70d002afdeca65ad5922.jpg%3Falt%3Dmedia%26token%3D21881f7e-e59d-4873-acdf-eab9f4170b84&width=768&dpr=4&quality=100&sign=88885390&sv=2)
Then run `sudo /Library/Ossec/bin/zensor-control start`
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/macos#mac-intel-based)
Mac (intel based)
**Steps to install zensor in Mac (intel based) :**
Run the command `sudo su`
Then run `echo "ZENSOR_MANAGER='IPADDRESS'" > /tmp/zensor_envs && curl -so zensor-agent.pkg https://package.zeron.one/newpackage/zensor-agent-1.0.0-1.pkg && sudo installer -pkg zensor-agent.pkg -target `
**NOTE -** In `"ZENSOR_MANAGER='IPADDRESS'"`, replace _**IPADDRESS**_ with your IP address
Finally, run `/Library/Ossec/bin/zensor-control start`
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/macos#uninstallation)
Uninstallation
**Steps to uninstall zensor in Mac :**
Copy```
1. sudo su
2. /Library/Ossec/bin/zensor-control stop
3. /bin/rm -r /Library/Ossec
4. /bin/launchctl unload /Library/LaunchDaemons/com.zensor.agent.plist
5. /bin/rm -f /Library/LaunchDaemons/com.zensor.agent.plist
6. /bin/rm -rf /Library/StartupItems/ZENSOR
7. /usr/bin/dscl . -delete "/Users/zensor
8. /usr/bin/dscl . -delete "/Groups/zensor
9. /usr/sbin/pkgutil --forget com.zensor.pkg.zensor-agent 
```

Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject
