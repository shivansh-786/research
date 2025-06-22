  1. [Zensor Installation](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation)
  2. [Choose your OS & architecture](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture)


# Windows
**Steps to install Zensor in Windows :**
Press the `Windows + R` keys together to bring up the Run dialog box 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FeuITz419iHoR182ck3AF%252Fimage-3-c469285f8e4a5c94b6c65dc69328d5b5.png%3Falt%3Dmedia%26token%3D12eaae81-ad38-46cf-96ef-30729ac4a422&width=768&dpr=4&quality=100&sign=1357e6d3&sv=2)
Type the PowerShell in the box and click the _'OK'_ button. A normal Windows PowerShell will launch as a current user 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FH7J6fTMm2CCdgnyBSyXn%252Fimage-4-52fda2551911c0395befea522c36a701.png%3Falt%3Dmedia%26token%3D2f59dd6b-05d9-42f0-8b6c-53713a5f1a7e&width=768&dpr=4&quality=100&sign=f2ff88ac&sv=2)
Type the command start-process PowerShell -verb runas and press the _'Enter'_ key 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FglYq5EJXfDjqGPimYKrz%252Fimage-5.png%3Falt%3Dmedia%26token%3Dbfac61fb-16ff-43aa-a847-e6826d9ab91e&width=768&dpr=4&quality=100&sign=84a0e314&sv=2)
The above command will bring up an elevated Windows PowerShell as an administrator 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FixCJqFENxXLeNWYAVAlL%252Fimage-6.png%3Falt%3Dmedia%26token%3Deb4a3fef-e433-4c55-9c3b-a1ccbb802314&width=768&dpr=4&quality=100&sign=b93badaf&sv=2)
Run the command copied from Install via CLI Window of Zeron management platform 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FKjcVFoXzmrW0rUEqZyNf%252Fimage-7.jpg%3Falt%3Dmedia%26token%3Deeec4f81-72cc-45a8-851d-0406d408e902&width=768&dpr=4&quality=100&sign=900ec29f&sv=2)
Click continue button and next step is Initialize and run zensors 
Run this command starting with [start-service]
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FDdP8WwbgmzKqQlxtv4ez%252Fimage-8.jpg%3Falt%3Dmedia%26token%3D4a021b4f-b198-4645-ab8c-0e1b91c5b4ab&width=768&dpr=4&quality=100&sign=e3eb1c9b&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/windows#windows-without-powershell)
Windows (Without PowerShell)
**Steps to install zensor in Windows (without powershell) :**
Click Continue after choosing you OS and download the installer file for Zeron for Windows (.msi file) 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FdB5QBUlU5ib7myD7rTsq%252Fmsi-file.png%3Falt%3Dmedia%26token%3D461ba285-0e45-460e-bb23-52d018d23441&width=768&dpr=4&quality=100&sign=1caa5736&sv=2)
Run the downloaded _.msi_ file and follow the installations steps.
Once the agent is installed,
  * In the start menu, search for manage agent app and open it
  * Or, go to `C:\Program Files (x86)\ossec-agent` and click on win32ui


![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FfCYDDlcDa7o0YGMGTxOF%252FAgent-manager-5aac61504547483282a20b3abdde4be3.png%3Falt%3Dmedia%26token%3D945cf40b-a5c7-4077-9d3c-421977903afa&width=768&dpr=4&quality=100&sign=4d40bbdb&sv=2)
Add your Manager IP and click on _'Save'_
Click on 'Restart' from the _Manage tab_ as shown below 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FXEopoa2RhIOzbVc5YWmx%252FRestart-26cd9d02f45ff327bd8413124af1ece5.png%3Falt%3Dmedia%26token%3D705a67d0-592d-4706-9c14-b812e033b7a2&width=768&dpr=4&quality=100&sign=fbbb565c&sv=2)
Click refresh to generate an Authentication Key automatically
### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/windows#troubleshooting)
Troubleshooting
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/windows#installation-alerts)
Installation alerts
**⚠ Error 1 - No new agent(s) were found**
If the Zensor Installation is taking a lot of time to load the results, click on finish and check for the name/host IP in the zensor list 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FDyRC3IwBaMSWMAoDEWGW%252Fwindows-1-0e94d6727d3ac075eb9bb70d0a5e2b7d.png%3Falt%3Dmedia%26token%3D1ea7551f-9186-4517-bc2f-23472a9110be&width=768&dpr=4&quality=100&sign=92adc449&sv=2)
**If the user is still not seen, follow the next steps :**
Open Manage Agent(app) and check for Authentication key, if it is not there, restart the agent 
Next, the agent should start running
**⚠ Error 2 - Authentication key is not produced automatically**
While installing without powershell, if the changes are not reflected after refreshing, please wait for a while and click on refresh once again 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FPS13u9ljmmFSDxs2TYQS%252FScreenshot%25202025-02-06%2520at%25208.05.03%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D21badaca-1871-4368-b077-8255477d5e42&width=768&dpr=4&quality=100&sign=4308b9b&sv=2)
If the problem persists, then click on _'View Logs'_ from the _View tab_ and send the logs to the Zeron Team 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FdSIcJfcXXUhtUuYLUJKv%252FScreenshot%25202025-02-06%2520at%25208.06.00%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D1ba35232-b14b-4ad4-83ab-81522b83ee9e&width=768&dpr=4&quality=100&sign=4e3b541a&sv=2)
#### 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/zensor-installation/choose-your-os-and-architecture/windows#deactivation-alertsto-stop-agent)
Deactivation alerts**To Stop Agent :**
Open Manage Agent (app) or go to the file location e.g. `C:\Program Files (x86)\ossec-agent\win32ui` (the key has been blurred for privacy reasons, while conducting the process you will be able to see a generated key) 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FkIaLluRdN9xb6ppErgVC%252Fwindows-3.png%3Falt%3Dmedia%26token%3D80a07e72-3675-4c09-9f72-4922b45ae03c&width=768&dpr=4&quality=100&sign=5c11ac53&sv=2)
Click _Manage > Stop_ to stop the agent 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FMWxoyAceYBipZ2Ds3jk5%252Fwindows-4-d0117e8733c02deb6f1904c69fcdd02e.png%3Falt%3Dmedia%26token%3D9f1074d5-2e8a-44a9-a1c6-673bf60141b6&width=768&dpr=4&quality=100&sign=71932397&sv=2)
Agent has been stopped 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fdtzq3F2OzxBrnB4rfJSX%252Fwindows-5-5e13fd77707d28b71c46ceb76026f07e.png%3Falt%3Dmedia%26token%3Dcb6b8d88-a2a3-4ee1-9c35-41436fb1c2c4&width=768&dpr=4&quality=100&sign=d66ab6d5&sv=2)
Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject
