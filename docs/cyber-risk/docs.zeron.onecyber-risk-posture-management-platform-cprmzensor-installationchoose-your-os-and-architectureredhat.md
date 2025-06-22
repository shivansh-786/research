  1. [Zensor Installation](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation)
  2. [Choose your OS & architecture](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture)


# Redhat
**Steps to install zensor in Redhat :**
Run the terminal of your system using `Ctrl+Alt+T`
Run the Install via CLI command starting with **[curl -so]** that is for installation of Zensor 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FiKPTYwPCr6l9VllIq09C%252Fimage-10.jpg%3Falt%3Dmedia%26token%3D0b5fb571-1599-449e-892e-d988b625816a&width=768&dpr=4&quality=100&sign=1b0ff874&sv=2)
Then run `sudo systemctl daemon-reload`
Then run `sudo systemctl enable zensor-agent`
Then run `sudo systemctl start zensor-agent`
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/redhat#troubleshooting)
Troubleshooting
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/redhat#installation-alerts)
Installation alerts
**Agent is running :**
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FI6pxQ1EpS6mbvm9dwqV4%252Fredhat-1-62e754bb6050d397daca30fb72f0ed21.png%3Falt%3Dmedia%26token%3D1462a33b-cc42-47da-b773-a9c5bf29a88c&width=768&dpr=4&quality=100&sign=fe300988&sv=2)
**Platform Status** _**(active)**_**:**
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FFhlpnx8QUCEdQPLfmwer%252Fredhat-2-1ef62291a80d44089a1121bd144b4452.png%3Falt%3Dmedia%26token%3D708bba65-bde0-4f00-a84e-e1bccd96773b&width=768&dpr=4&quality=100&sign=61bcf31d&sv=2)
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/redhat#deactivation-alerts)
Deactivation alerts
**To stop the agent :**
`sudo systemctl stop zensor-agent`
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FBhThYCaf1dlgG6zYqG6M%252Fredhat-3-9a37bec9b6c9c156b1dc800b527a2c61.png%3Falt%3Dmedia%26token%3D0fa46ece-de8d-4aaa-a086-939125e0405f&width=768&dpr=4&quality=100&sign=b6353171&sv=2)
**Platform Status** _**(disconnected)**_**:**
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FJ5Jg1PEQbnyijESrgO3f%252Fredhat-4-3077f073b8037afcedb9f77f106687da.png%3Falt%3Dmedia%26token%3D2c92eebe-cf8c-46c0-8914-99d91b1da0a4&width=768&dpr=4&quality=100&sign=3d2b54ea&sv=2)
Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject
