  1. [Zensor Installation](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation)
  2. [Choose your OS & architecture](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture)


# Debian
**Steps to install zensor in Debian :**
Run the terminal of your system using `Ctrl+Alt+T`
Run the Install via CLI command starting with **[curl -so]** that is for installation of Zensor 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FY8MUDXl51S59FtvhPkC7%252Fimage-9.jpg%3Falt%3Dmedia%26token%3D8ff5262e-7729-440b-8b3b-7efce07f0ca2&width=768&dpr=4&quality=100&sign=e0fd15c6&sv=2)
**Then run the following commands one after the other :**
  * `sudo systemctl daemon-reload`
  * `sudo systemctl enable zensor-agent`
  * `sudo systemctl start zensor-agent`


## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/debian#troubleshooting)
Troubleshooting
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/debian#installation-alerts)
Installation alerts
**⚠ Error - The results are not shown after the installation**
Use the `sudo systemctl status zensor-agent` command to check for the status 
If the status shows failed, run this command `sudo cat /var/ossec/etc/ossec.conf`
Go to _address_ under the _ossec-config_ to check for manager IP. If the value in it is invalid or different than the CLI command, correct it accordingly, using the `nano /var/ossec/etc/ossec.conf` command 
**If the above steps don’t work and issue persists, follow the commands given below in order to check the logs and solve the error :**
`tail -f /var/ossec/log/ossec.log`
**Removing and reinstalling zensor agent :**
(i) `apt-get remove –purge zensor-agent`
(ii) `systemctl disable zensor-agent`
(iii) `systemctl daemon-reload`
Last step, repeat the installation process as given in the Zensor Installation Documentation
Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject
