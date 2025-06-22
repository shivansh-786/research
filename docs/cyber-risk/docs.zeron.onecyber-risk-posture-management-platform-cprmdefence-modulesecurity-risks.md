  1. [Defence Module](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module)


# Security Risks
This page records the information regarding the Security risks linked to each host. **It consists of the following blocks :**
  * Mitre Attack Techniques
  * Threat Evolution
  * Top Attack Hotspots
  * File Integrity Monitoring


![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F9UBBtZDAUZLkDpw1wGjf%252FSecurity-risks-08e05855bbaeba71d13304c8b372b2d6.png%3Falt%3Dmedia%26token%3D20d06b25-7450-41e5-bb7a-b02140611964&width=768&dpr=4&quality=100&sign=9374d55d&sv=2)
**The top section of this page displays the following information regarding the detected risks :**
  * **Total -** Shows the total number of risks detected by Zensors in a certain timeframe 
  * **Critical alerts -** Shows the number of risks with a severity level more than 12
  * **Failed authentication -** Shows the number of risks detected resulting in failed authentication
  * **Passed authentication -** Shows the number of risks detected resulting in successful authentication


![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FSlE07s53W0rRkUFPrf92%252FSecurity-risks-top.png%3Falt%3Dmedia%26token%3D14d90ea5-bbbd-493a-ae25-a0278cd7eb7a&width=768&dpr=4&quality=100&sign=1984d2e6&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/security-risks#mitre-attack-techniques)
Mitre Attack Techniques
This block contains a pie chart which shows the different MITRE ATT&CK tactics risks detected across the organization. Each MITRE ATT&CK Technique has its own unique color assigned to it. Hovering over a particular color of the chart provides the user with the name of the technique and the number of tactics found under it. Clicking on the full-screen icon on the bottom right of this block provides the user with an enlarged chart view and a tabular view of the same
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FPL9aeCm9PNY902eQhDql%252FMitre-small-0ae211537936c149d8ffa73ebbd4c3a9.png%3Falt%3Dmedia%26token%3Da6419e60-0782-48eb-afbc-aa8038d1a0bd&width=768&dpr=4&quality=100&sign=229e79f&sv=2)
The key/legend of the chart is provided in the full-screen view, using which the user can map the techniques to their respective colors. Similar to the preview, hovering over a particular color of the chart provides the user with the name of the technique and the number of risks detected for it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fc26Ck8KSLwILs4u5rX6d%252FMitre-big-44ed89dbd60d4fbc9a3830092121223f.png%3Falt%3Dmedia%26token%3D9b750e34-0bf3-46eb-8526-616cb28d5c0e&width=768&dpr=4&quality=100&sign=b00c8062&sv=2)
**The tabular view provides the following info about the events through which the risks were detected :**
  * Date and time of occurrence
  * Host
  * MITRE ATT&CK type
  * Security level (low/medium/high)
  * Rule
  * Description of the detected risk


The user can search for a particular event based on the host or severity level by clicking on the filter icon in the top right corner. A list of the events can be downloaded as a _.csv_ file by clicking on the download button and then selecting the _'export as .csv'_ option, and the total number of events is given at the bottom of the table 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FAUGP7UHY7lyFoJK9C0aB%252FThreat-evolution-table.png%3Falt%3Dmedia%26token%3Defdab70c-0e0e-43a8-b951-429d13289467&width=768&dpr=4&quality=100&sign=79371ec5&sv=2)
Clicking on a particular event would provide the user with further details about it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FK54Ghfy8iIV5kBd9Rujc%252FMitre-details-e0a856f8928dfcd7d49aab8c69930f47.png%3Falt%3Dmedia%26token%3Df7b32cc7-da42-484e-a8b1-85640b5f5663&width=768&dpr=4&quality=100&sign=73ac7406&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/security-risks#threat-evolution)
Threat Evolution
This block depicts the evolution of the threat landscape over time by giving a graphical representation of the risks detected. The graph is produced by plotting the event count of each host against its timestamp. Hovering over a particular color in the graph will display the number of events occurred at that time for each host, assort them, and color code them according to the IP address of the host. Clicking on the full-screen icon on the bottom right of this block provides the user with an enlarged view and a tabular view of the same 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FH3l1jCqfkKoSk85NRuKd%252FHotspot-small.png%3Falt%3Dmedia%26token%3D2fab5901-f703-4bfd-aab9-edcd5fb3837a&width=768&dpr=4&quality=100&sign=e40443cc&sv=2)
Similar to the preview, hovering over a particular color of the graph provides the user with the timestamp at that point and the number of events that occurred for each host at that time. The host IP addresses are color-coded 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FKNvcsmUqX6g9ioOd1DMZ%252FThreat-evolution-big-b8d76e77cf14483a59bd42431aeb5c43.png%3Falt%3Dmedia%26token%3De48b3083-54e2-43bd-a0b9-6bb6e6b886b7&width=768&dpr=4&quality=100&sign=9aae083&sv=2)
**The tabular view provides the following info about the events through which the risks were detected for each host :**
  * Date and time of occurrence
  * Host
  * MITRE ATT&CK type
  * Security level (low/medium/high)
  * Rule
  * Description of the detected risk


The user can search for a particular event based on the host or severity level by clicking on the filter icon in the top right corner. A list of the events can be downloaded as a _.csv_ file by clicking on the download button and then selecting the _'export as .csv'_ option, and the total number of events is given at the bottom of the table
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2Fdocs.zeron.one%2Fassets%2Fimages%2FThreat-evolution-table-f09be42e168c7011ba49ce6297946550.png&width=768&dpr=4&quality=100&sign=445587a4&sv=2)
Clicking on the date of a particular event would provide the user with further details about it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fe2lRtkP2AuDoyjdQ4SQZ%252FHotspot-details.png%3Falt%3Dmedia%26token%3Db68986cc-a4e2-49c9-a7f9-5b6168a9b3fc&width=768&dpr=4&quality=100&sign=9c618853&sv=2)
Clicking on the MITRE ATT&CK type of a particular event would redirect the user to the Risk Mitigation page, where he/she is provided with the details about that risk and can create cybersecurity initiatives corresponding to that particular risk 
You can read more about the Risk Mitigation page [here](https://docs.zeron.one/docs/Defence-Module/Risk-Mitigation)
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FZLF4RBlf1POeikTTuc2x%252FThreat-evolution-attack.png%3Falt%3Dmedia%26token%3D1f217198-72bf-4dd2-9b9a-3d9c1cdea683&width=768&dpr=4&quality=100&sign=1e87a8a8&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/security-risks#top-attack-hotspots)
Top Attack Hotspots
This block consists of a web chart that shows how exposed the hosts in the organization are to an attack. Each host is color-coded, and hovering over a particular section of the chart will display the top attack hotspot (most targeted host) in that section, and also show its event count. Clicking on the full-screen icon on the bottom right of this block provides the user with an enlarged chart view and a tabular view of the same. Two of the most exposed hosts are given at the bottom 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FXeB3e6sAqW6KIwVDrA54%252FHotspot-small-33831638d6605251c4fb89997929ebcc.png%3Falt%3Dmedia%26token%3Df6585f18-5799-4a4e-9c5a-b6985e9984bc&width=768&dpr=4&quality=100&sign=16260c86&sv=2)
The key/legend of the chart is provided in the full-screen view, using which the user can map the hosts to their respective colors. Similar to the preview, hovering over a particular section of the chart provides the user with the top attack hotspot and its event count 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FZ1FKAQr73subrHtmTd68%252FHotspot-big-ff7a487e6db43a82ffa34739cd54309f.png%3Falt%3Dmedia%26token%3D5624886f-3d88-4f1c-9211-dbda80408cb3&width=768&dpr=4&quality=100&sign=ca96857c&sv=2)
**The tabular view provides the following info about the events through which the risks were detected for each host :**
  * Date and time of occurrence
  * Host
  * MITRE ATT&CK type
  * Security level (low/medium/high)
  * Rule
  * Description of the detected risk


The user can search for a particular event based on the host or severity level by clicking on the filter icon in the top right corner. A list of the events can be downloaded as a _.csv_ file by clicking on the download button and then selecting the _'export as .csv'_ option, and the total number of events is given at the bottom of the table 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fl27gUJtxXJgxUZm22jZF%252FHotspot-table-b2c6eaedbd4ebef90fdec2be91626699.png%3Falt%3Dmedia%26token%3D84120167-01c3-491c-b628-1038ab1c6260&width=768&dpr=4&quality=100&sign=3ef79ac8&sv=2)
Clicking on the date of a particular event would provide the user with further details about it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FcF5P2LI8k9fK9JJANLxM%252FHotspot-details-d5bd4bb9fa8030dd1b09cb5bf7e36b4d.png%3Falt%3Dmedia%26token%3D0e5f8324-43b9-4d2b-b461-139761a6f83b&width=768&dpr=4&quality=100&sign=d970b523&sv=2)
Clicking on the MITRE ATT&CK type of a particular event would redirect the user to the Risk Mitigation page, where he/she is provided with the details about that risk and can create cybersecurity initiatives corresponding to that particular risk 
You can read more about the Risk Mitigation page [here](https://docs.zeron.one/docs/Defence-Module/Risk-Mitigation)
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FLc6J2aecNRku5LgYW5SG%252FHotspot-attack.png%3Falt%3Dmedia%26token%3D95aceae2-c320-4319-9778-1e6532e0a0f4&width=768&dpr=4&quality=100&sign=12f5eaf1&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/security-risks#file-integrity-monitoring)
File Integrity Monitoring
This block displays the integrity of files in the system by recording the number of times they have been modified, added, or deleted 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FsSztAZl8ST8UF4EvCTMt%252FFile-integrity-43c24f6fabaa9ab901677c21f1a93ffd.png%3Falt%3Dmedia%26token%3D02611e03-651b-4e78-84bb-9eef7ee1ee01&width=768&dpr=4&quality=100&sign=b7d28379&sv=2)
Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject
