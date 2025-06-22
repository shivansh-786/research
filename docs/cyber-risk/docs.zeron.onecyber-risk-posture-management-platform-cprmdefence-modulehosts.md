  1. [Defence Module](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module)


# Hosts
**This page records the details about the hosts integrated with Zeron and provides the following details about each of them :**
  * Host details
  * Mitre Att&ck tactics risks detected
  * Endpoint Compliance mapping
  * Configuration Assessment (CIS-CAT Audit) Score
  * Risk count evolution graph
  * CIA Triad Percentage
  * Vulnerabilities detected
  * Risks detected
  * Sysmon risks detected


![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FPEO6BT13SxNT0hDErYpg%252FHosts-c2202b257816cc8c4830fb79c9d083b0.png%3Falt%3Dmedia%26token%3D49adebea-cefb-4e92-af2a-5101b6c8dc64&width=768&dpr=4&quality=100&sign=d1154b1e&sv=2)
The top section of the page allows the user to select a host integrated with Zeron and provides the above-given details for the chosen host 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F5NZovZWLXEj03evGrkTY%252FSelect-host-ccd21f7d84ebc209eaac65263059d700.png%3Falt%3Dmedia%26token%3D1259711d-2ca1-40b8-96c8-3bd1c18c5032&width=768&dpr=4&quality=100&sign=a8d53068&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#host-details)
Host details
This block shows the IP address, name, status, version, group, OS, registration date, and last activity of the selected host 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FNTdrZ8ewBBCERTOdaAB1%252FHost-details-af0033c7fcb72e0f217af29826a2eadd-2.png%3Falt%3Dmedia%26token%3Db516d540-7c6d-47ee-b35e-b05a7295cf38&width=768&dpr=4&quality=100&sign=d36824bb&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#mitre-att-and-ck-tactics-risks-detected)
Mitre Att&ck tactics risks detected
This block contains a pie chart that visually categorizes the various MITRE ATT&CK Tactics risks detected for the selected host. Each MITRE ATT&CK Technique discovered has its own unique color assigned to it. Hovering over a particular color of the chart provides the user with the name of the technique and the number of tactics found under it for this host. Clicking on the full-screen icon on the bottom right of this block provides the user with an enlarged chart view and a tabular view of the same 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FwYWv5cpEPCZXFKNU2Mnv%252FMitre-small-47ec2abb62cd63d74be02f72170b7cac.png%3Falt%3Dmedia%26token%3Db25f71f3-41b9-49c9-809e-b0cda51357cc&width=768&dpr=4&quality=100&sign=242f3b10&sv=2)
The key/legend of the chart is provided in the full-screen view, using which the user can map the techniques to their respective colors. Similar to the preview, hovering over a particular color of the chart provides the user with the name of the technique and the number of risks detected for it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FRhmo5yUcUwQuHjrdSlPa%252FMitre-big-d93a146157bd4b5672c26c4f4f56f77b.png%3Falt%3Dmedia%26token%3D072c6601-8519-444b-8508-662f01f3da09&width=768&dpr=4&quality=100&sign=7fe3975d&sv=2)
**The tabular view provides the following info about the events through which the risks were detected :**
  * Date and time of occurrence
  * Host
  * MITRE ATT&CK type
  * Security level (low/medium/high)
  * Rule
  * Description of the detected risk


The user can search for a particular event based on the Att&ck type, Rule, or severity level by clicking on the filter icon in the top right corner. A list of the events can be downloaded as a _.csv_ file by clicking on the download button and then selecting the _'export as .csv'_ option, and the total number of events is given at the bottom of the table
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fjn53JYn8JieWA6kDyt1s%252FMitre-table-df32aab1b3e34f62ac0a4eb79b086c63.png%3Falt%3Dmedia%26token%3Dd3320785-708d-4069-b3cf-80dfa1047040&width=768&dpr=4&quality=100&sign=5cf37471&sv=2)
Clicking on the date of a particular event would provide the user with further details about it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FJK2tQMLSyPmVQZjoUFxt%252FMitre-Details.png%3Falt%3Dmedia%26token%3D681b9763-0834-4456-8248-8ab0d9012b75&width=768&dpr=4&quality=100&sign=d5b60213&sv=2)
Clicking on the MITRE ATT&CK type of a particular event would redirect the user to the Risk Mitigation page, where he/she is provided with the details about that risk and can create cybersecurity initiatives corresponding to that particular risk
You can read more about the Risk Mitigation page here 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F4mS8FT5I6cL21Z87MzX6%252FMitre-attack-bad8209a40face13e72aa9c57ce5126a.png%3Falt%3Dmedia%26token%3D17de3001-2343-456e-a925-c021f9b74e69&width=768&dpr=4&quality=100&sign=28806fd7&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#endpoint-compliance-mapping)
Endpoint Compliance mapping
This block contains a donut chart depicting the number of risks detected that violate the compliance for that particular host. Hovering over a particular color will display which control the risk is related to and how many such risks have been found for that particular control 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FwLEOhvFqbewkNqObnXWb%252FCompliance-small-b0227486dd8c9dec63b16207800d31a8.png%3Falt%3Dmedia%26token%3Df231f42e-4c1b-44f1-ae62-f9e3d51706bb&width=768&dpr=4&quality=100&sign=af353cb4&sv=2)
The user can choose to get a chart for any of the 7 compliances supported by Zeron (GDPR, HIPAA, ISO 27001, NIST, PCI DSS, and SOC2). Clicking on the full-screen icon on the bottom right of this block provides the user with an enlarged chart view and a tabular view of the same
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FHMGsuLhBgZiBCpP2ypgP%252FCompliance-list-1f1a91ab1a29ccfcf2f9e53d84d44aaa.png%3Falt%3Dmedia%26token%3Df7bdf14b-ee0d-4809-a032-efa1a816326f&width=768&dpr=4&quality=100&sign=c4a5881d&sv=2)
The key/legend of the chart is provided in the full-screen view, using which the user can map the controls to their respective colors. Similar to the preview, hovering over a particular color of the chart provides the user with the name of the control and the number of risks found for it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FJelizVrtqXqi0hdkNraE%252FCompliance-big-52aa27c4d20bf4dbf24e1140eec401e3.png%3Falt%3Dmedia%26token%3D69eecfcf-ab53-44dd-bafc-de43f528aa5d&width=768&dpr=4&quality=100&sign=8584e730&sv=2)
**The tabular view provides the following info about the events through which the risks were detected :**
  * Date and time of occurrence
  * Host
  * MITRE ATT&CK type
  * Security level (low/medium/high)
  * Rule
  * Description of the detected risk


The user can search for a particular event based on the Date, rule, or severity level by clicking on the filter icon in the top right corner. A list of the events can be downloaded as a _.csv_ file by clicking on the download button and then selecting the _'export as .csv'_ option, and the total number of events is given at the bottom of the table
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FLyXOssytparWELD2528W%252FCompliance-table.png%3Falt%3Dmedia%26token%3Daf2ae698-e946-4228-8c8c-5f35842881d7&width=768&dpr=4&quality=100&sign=5618cbc4&sv=2)
Clicking on the date of a particular event would provide the user with further details about it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FspSSFSckBhdQ8Ce8DBPk%252FCompliance-Details-4b5dfe49fcbe6efcc70239c75454e357.png%3Falt%3Dmedia%26token%3D6f15c548-4143-481e-93cf-546e40b5886e&width=768&dpr=4&quality=100&sign=9dd1c49e&sv=2)
Clicking on the MITRE ATT&CK type of a particular event would redirect the user to the Risk Mitigation page, where he/she is provided with the details about that risk and can create cybersecurity initiatives corresponding to that particular risk
You can read more about the Risk Mitigation page [here](https://docs.zeron.one/docs/Defence-Module/Risk-Mitigation)
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F8S9od6OgzdETMw50wUf0%252FCompliance-attack.png%3Falt%3Dmedia%26token%3Db2ab29f7-efe4-4f75-9b82-f547741a62c0&width=768&dpr=4&quality=100&sign=7168fe0&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#cis-cat-audit-score)
CIS-CAT Audit Score
This section shows the Configuration Assessment Score done on the host. **It consists of 3 parts :**
  * **Pass** – The total number of machines that passed the security configuration
  * **Fail** – The total number of machines that failed the security configuration
  * **Invalid** – The total number of machines that are not valid for this security configuration 


The CIS-CAT Audit Score is calculated based on the above information obtained from the security configuration audit 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FNWFMpxiaBu7dVhlyhrlm%252FAudit-score-5b95881dbfe8bcc9ccc4db9dc4264c83.png%3Falt%3Dmedia%26token%3D4fb27b6f-6d37-4917-94d8-b23606dbde32&width=768&dpr=4&quality=100&sign=aed559f3&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#risk-count-evolution)
Risk count evolution
Shows the evolution (increase or decrease) of risks over the chosen time period by rendering a graph, which contains the event count plotted against the timestamp. This graph is produced using the data collected by Zensors for the selected host. Hovering over the graph gives the event count and when it has occurred 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FCK18hw3t3qg9vuu7fTgm%252FRisk-count-evolution-small.png%3Falt%3Dmedia%26token%3D5e44b014-3d44-497a-b549-32e2c4f02038&width=768&dpr=4&quality=100&sign=cc408245&sv=2)
Clicking on the full-screen icon on the bottom right of this block provides the user with an enlarged chart view and a tabular view of the same. Similar to the preview, the user can also hover over this chart to get the event count and its timestamp 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FZz1mhb2spMSfdZ3BgZFM%252FRisk-count-evolution-big-c519b342bddfa4fa148474e99a8a24ea.png%3Falt%3Dmedia%26token%3D928c71f5-e336-4ac8-bb2b-d709cafa3923&width=768&dpr=4&quality=100&sign=f7bde7a&sv=2)
**The tabular view provides the following info about the events through which the risks were detected :**
  * Date and time of occurrence
  * Host
  * MITRE ATT&CK type
  * Security level (low/medium/high)
  * Rule
  * Description of the detected risk


The user can search for a particular event based on the Att&ck type, Description, or Rule by clicking on the filter icon in the top right corner. A list of the events can be downloaded as a _.csv_ file by clicking on the download button and then selecting the _'export as .csv'_ option, and the total number of events is given at the bottom of the table
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F89YDhMR3Kqp7hP1EGaaa%252FRisk-count-evolution-table-d461b2be1e5d25b52546b69ddb717929.png%3Falt%3Dmedia%26token%3Da5852589-e6e1-4193-9938-c9c3de1b19a3&width=768&dpr=4&quality=100&sign=f6480577&sv=2)
Clicking on the date of a particular event would provide the user with further details about it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FnncJMicL321msIzqleUO%252FRisk-count-evolution-details-427de572372e91e762a001592614b759.png%3Falt%3Dmedia%26token%3Dafa4ef1b-e087-4378-b43b-770ea0164d32&width=768&dpr=4&quality=100&sign=382c366b&sv=2)
Clicking on the MITRE ATT&CK type of a particular event would redirect the user to the Risk Mitigation page, where he/she is provided with the details about that risk and can create cybersecurity initiatives corresponding to that particular risk
You can read more about the Risk Mitigation page [here](https://docs.zeron.one/docs/Defence-Module/Risk-Mitigation)
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fg74Xqi03eKPMvHrbr9yB%252FRisk-count-evolution-attack-282048e71289df6c1fd8c9e30fc58475.png%3Falt%3Dmedia%26token%3De4b1409d-4653-4e0c-a5f2-63c7d536058d&width=768&dpr=4&quality=100&sign=1b003535&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#cia-triad-percentage)
CIA Triad Percentage
This block gives the CIA triad score based on the confidentiality, integrity, and availability of the data 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FD42mM0GkkABZPGqG1QtX%252FCIA-score.png%3Falt%3Dmedia%26token%3D62275aa9-9f00-4971-987d-9f0e5c96d1c0&width=768&dpr=4&quality=100&sign=d1493926&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#vulnerabilities-detected)
Vulnerabilities detected
**This block consists of the list of detected vulnerabilities and provides the following info about the events through which they were detected :**
  * Name of the vulnerability
  * CVE associated with the vulnerability
  * Version of the service
  * CVSS3 Score
  * Security level (low/medium/high)
  * Status
  * Description


A list of the vulnerabilities can be downloaded as a _.csv_ file by clicking on the download button and then selecting the _'export as .csv'_ option, and the total number of events is given at the bottom of the table 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252F5jFAN6UvROhg9mmDmJpq%252FVulnerabilities.png%3Falt%3Dmedia%26token%3De85581b3-a977-49ea-a52d-2e8f41aba2ed&width=768&dpr=4&quality=100&sign=e2384628&sv=2)
Clicking on the date of a particular event would provide the user with further details about it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FG8oWYyMPqbrxa95H5AvP%252FVulnerability-details-1f50f38b7b639209363a2442c87140ed.png%3Falt%3Dmedia%26token%3D4fecbbd2-7562-4bcc-9f06-ab497752f504&width=768&dpr=4&quality=100&sign=7182174c&sv=2)
**Note -** A CVSS3 score is the summation of three metric groups, being your Base, Temporal, and Environmental levels. A high CVSS3 score indicates a critical vulnerability 
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#risks-detected)
Risks detected
**This section consists of the list of detected risks and provides the following info about the events through which they were detected :**
  * Date and time of occurrence
  * Host
  * MITRE ATT&CK type
  * Security level (low/medium/high)
  * Rule
  * Description of the detected risk


A list of the risks can be downloaded as a _.csv_ file by clicking on the download button and then selecting the _'export as .csv'_ option, and the total number of events is given at the bottom of the table 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252FWz2PsfteE86OgPorQ8qS%252FRisks.png%3Falt%3Dmedia%26token%3D509fd200-4c65-43f2-aeac-9bc9ede55f04&width=768&dpr=4&quality=100&sign=993d62e1&sv=2)
Clicking on the date of a particular event would provide the user with further details about it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Ficl0bDvvU4Mw8yBVca0w%252FRisk-details-619baa0f90f0eb28f6923c6472d5cc7b.png%3Falt%3Dmedia%26token%3D436ab132-6d18-4aaf-8f00-152cc0f70021&width=768&dpr=4&quality=100&sign=8e8ff556&sv=2)
## 
[](https://docs.zeron.one/cyber-risk-posture-management-platform-cprm/defence-module/hosts#sysmon-risks-detected)
Sysmon risks detected 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F2854935529-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FvyU3NMiz2Rw6Y9PJdkUQ%252Fuploads%252Fn6kIZlmbJKeBfK7NBmQO%252FSysmon-risks-0439043328126fa40286d66dd14c2582.png%3Falt%3Dmedia%26token%3D28a5205e-0c68-4f8e-984d-e860f248d2f8&width=768&dpr=4&quality=100&sign=423d7343&sv=2)
Last updated 4 months ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject
