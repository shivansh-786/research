
# Master Data
The Master Data Page provides a centralized view of templates used for vendor assessments. These templates consist of questions aligned with compliance standards to evaluate risks within a domain
Templates are structured question sets designed to assess compliance with standards such as ISO 27001, NIST, or GDPR. They determine whether a domain has risks or vulnerabilities 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FL6y1oAvoI9bUC5mEfkk3%252FScreenshot%25202025-02-18%2520at%252012.05.21%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D5087f073-8e37-442f-9cd8-22f62a3871b1&width=768&dpr=4&quality=100&sign=e781b2c7&sv=2)
Types of Templates [](https://docs.zeron.one/master-data#types-of-templates)
**Standard Templates -** Universally recognized templates based on established compliance frameworks like ISO 27001, NIST, or GDP 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252F7R85sssJ6JCBqk4wVKLm%252FScreenshot%25202025-02-18%2520at%252012.08.01%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3De058cdae-c480-4c28-8036-d1101caa835e&width=300&dpr=4&quality=100&sign=e3775fa1&sv=2)
**Custom -** Vendor-specific templates tailored to assess risks unique to individual vendors. These templates can vary based on specific requirements 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FdaU3F0uoeLfIsHoA9Pwl%252FScreenshot%25202025-02-18%2520at%252012.08.29%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D67979957-3c7a-42aa-91d4-d2ef917836f6&width=300&dpr=4&quality=100&sign=15385d1d&sv=2)
Filter [](https://docs.zeron.one/master-data#filter)
A filter is available to view all templates or filters by standard or custom templates for focused management
**Below the template filter, detailed information about each template is displayed, including :**
**Template Name -** The name of the template
**Tags -** Tags assigned to the template for easier categorization, access, and searchability
**Total Categories -** The number of categories included in the template
**Total Questions -** The total number of questions across all categories in the template
**Last Edit Date -** The most recent date when the template was edited and saved
**Edited By -** The name of the individual who made and saved the edits
**Action -** Additional functionalities, such as the option to delete a specific template if required
Creating a Custom Template [](https://docs.zeron.one/master-data#creating-a-custom-template)
**Users can create their custom templates by providing the following information :**
**Template Name -** Provide a unique name for this template to identify it easily when selecting or searching among templates 
**Tag -** Add relevant tags to classify this template by purpose or department (e.g., Compliance, Finance, IT Security). Tags make it easier to locate templates through search and filtering options 
Users need to download the Sample Template provided add their details to it and upload it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FVYiu8s3Zwwzc13lhsVX5%252FScreenshot%25202025-02-18%2520at%252012.09.39%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Ddd8f472c-e52d-44eb-a280-349b542f068c&width=300&dpr=4&quality=100&sign=cd52a3c1&sv=2)
This sample template gives you the flexibility to upload the questions with proper well-defined categories straight from your sheets to the platform. It also includes instructions for the user 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FqxoHWMmQ9vZJZTWt6TK1%252FScreenshot%25202025-02-26%2520at%252012.43.53%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Def53a17d-1731-4f15-9fa0-1337a808de98&width=300&dpr=4&quality=100&sign=211957f3&sv=2)
**It includes the following attributes :**
**Question -** This is the title of the questions that you want to ask the vendors 
**Type -** The type of question it is, either single choice or text-based
**Mandatory/Optional -** This tells if the question is Mandatory or Optional 
**Weightage -** The weightage of the question. If not provided then "0" means no risk 
**Options (Comma Separated Options) -** If the question type is a single choice, then the list of options is separated by commas 
**Evidence Required On Question -** If the question requires evidence, then either "yes" or "no." Default value "No" if nothing is selected 
**Options Required Evidence (Use same option Value From Option Column) -** If the question type is a single choice, specify which options you want the vendor to provide the evidence 
**High-Risk Options (Use same option Value From Option Column) -** Comma-separated options from the "Options" column that indicate high risk (e.g., "No Training Conducted" for employee security training). Leave blank if none 
**Medium Risk Options (Use same option Value From Option Column) -** Comma-separated options from the "Options" column that indicate medium risk (e.g., "Training Conducted Once a Year" for employee security training). Leave blank if none 
**Low-Risk Options (Use same option Value From Option Column) -** Comma-separated options from the "Options" column that indicate low risk (e.g., "Training Conducted Quarterly" for employee security training). Leave blank if none 
**Organization Remark Required On Vendor Answer -** If set to "Yes," the organization can provide remarks for each vendor's answer. These remarks can be marked as Compliant, Partially-Compliant, Non-Compliant, or Not-Applicable. If not selected then the default value is No
**Evidence Name -** The prompt used for showcasing the evidence on text-based questions with the default "Please enter evidence" 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FevQ5j962os4G9yYlBLBa%252FScreenshot%25202025-02-26%2520at%252012.31.15%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D5c31ada5-5a59-484f-aae0-f922a0b3542b&width=300&dpr=4&quality=100&sign=16eb8bf2&sv=2)
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FyfE70aNinQlcoNAVpWTI%252FScreenshot%25202025-02-26%2520at%252012.31.20%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Dcfe3ab2e-a31f-4132-a066-7af8af53edfa&width=300&dpr=4&quality=100&sign=1fc40248&sv=2)
While filling out the sample template, the user has the decision to choose the type of question between either Text or Single Choice. In Text, the user can fill in answers for the assessment in texts using their own words in a text field. In Single Choice, the user can only choose one option from the multiple options available 
Furthermore, the user has the freedom to choose whether a question is Mandatory or Optional. If it is Mandatory, it must be answered. If it is Optional, it can be skipped. The user also decides which options would be High, Medium, or Low severity, if they were to occur to an organization in real time. Additionally, the user also can add weightage to a question to create a risk
The user also mentions the options that are viable for the question, and these options need to be separated using commas to distinguish them. The user can also choose whether evidence is needed for the question. To further smoothen the experience, the user can also decide on which options the evidence is required, as not every option might need justification in the form of evidence. The user also has the authority to choose the severity of the options, i.e., High, Medium, or Low. Through this, we get a more apt understanding of how critical of a risk it potentially could be
Additionally, if the question type is free text, the user can enable an option that mandates vendors to upload evidence for that question. If there is a weightage assigned to the question, the organization can select “Organization Remark Required On Vendor Answer.” After reviewing the answer and uploading evidence, the organization can determine whether a risk should be created based on the response 
**For a Text-based question, consider the following example :**
The organization asks vendors to “Describe your data encryption policies.” This question is of Text type, meaning vendors must provide a free-text response instead of selecting from predefined options. Since encryption policies are critical for security compliance, this question is marked as Mandatory and has a Weightage of 10, indicating its importance in the risk assessment. As a free-text response, the Options column is marked as N/A (not applicable) 
Additionally, evidence is required for this question, ensuring that vendors submit supporting documents such as encryption policy files. The Organization Review is enabled, meaning the organization’s risk team will evaluate the response and uploaded evidence before determining whether a risk should be created. The required evidence document for submission is labeled as “Encryption_Policy_Document”
**For a Single Choice question, consider the following example :**
The organization asks vendors, “Does your company have an incident response plan?” This question is of Single Choice type, meaning vendors must select one option from the given choices: Yes, No, or In Progress. Since incident response plans are essential for risk management, the question is Mandatory and has a Weightage of 5.
**To ensure proper documentation, vendors are required to upload evidence only if they select “Yes” or “In Progress” as their answer. The risk severity is classified as follows :**
“No” is considered High Risk, as lacking an incident response plan could severely impact the organization
“In Progress” is classified as Medium Risk, since the company is working on implementing a plan but has not yet finalized it
“Yes” is categorized as Low Risk, as the company already has a response plan in place 
Unlike the text-based question, the Organization Review is not required for this question, meaning the risk assessment is based on predefined severity levels. The required document for evidence submission is labeled as “Incident_Response_Document”
Template - Specific Information [](https://docs.zeron.one/master-data#template-specific-information)
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252Fo3GSTOjimbrgCDv5PvfD%252FScreenshot%25202025-02-12%2520at%25201.05.19%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3De5e47bfa-8026-4b3c-8c8c-897783d519f5&width=300&dpr=4&quality=100&sign=1a4f9398&sv=2)
Users can view detailed information about a specific question within a template. **The following attributes are provided :**
**Weightage -** Indicates the significance of the question within the overall questionnaire. Higher weightage contributes more to the overall assessment score
**Mandatory -** Specifies whether answering the question is required for the assessment to be considered complete
**Answer Type - Defines the response format for the question :**
**Single Select -** Allows the selection of one option from a predefined list
**Text -** Enables open-ended responses for more detailed input 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FYYiFVi0TF84k69Km5w5h%252FScreenshot%25202025-02-12%2520at%25201.05.43%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D517a826b-2f60-4476-accc-6ddc731f15d1&width=300&dpr=4&quality=100&sign=b7fe5d61&sv=2)
Adding Categories and Questions in Custom Templates[](https://docs.zeron.one/master-data#adding-categories-and-questions-in-custom-templates)
In custom templates, user can add categories to cater to their needs 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FCkgg9LJKTlbRaocKlpcR%252FScreenshot%25202025-02-12%2520at%25201.06.23%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D409a06d7-a188-42e4-a44b-d1da73e1bdaf&width=300&dpr=4&quality=100&sign=7bf143a8&sv=2)
The user just needs to enter the Category Name. The user can also add questions to the category created or existing categories 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FgNq3kUez5UmzSVeSPdZV%252FScreenshot%25202025-02-12%2520at%25201.06.55%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D8d7a4ac4-7654-4666-a773-f8f2382ee095&width=300&dpr=4&quality=100&sign=58a08453&sv=2)
Deleting or Editing a Question in Master Data [](https://docs.zeron.one/master-data#deleting-or-editing-a-question-in-master-data)
A user can choose to delete or edit a specific question from a custom template, by clicking on the three dots on the Action tab choosing "Delete" or "Edit" and then confirming it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FtfGKz1voV6eTc6BRsGkJ%252FScreenshot%25202025-02-20%2520at%25203.56.30%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D22f01837-3c26-4e52-9716-6c3a03f64171&width=300&dpr=4&quality=100&sign=5eab6661&sv=2)
If the user chooses to "Edit" 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FoUo7HSCEgEMSZechJOtk%252FScreenshot%25202025-02-20%2520at%25204.00.40%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Ddd489f7d-bfd6-4e4e-98cf-d5f5b29c38d8&width=300&dpr=4&quality=100&sign=61fd0a70&sv=2)
if the user chooses to "Delete" 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FsNCZcV8tkxthYdSexuYM%252FScreenshot%25202025-02-20%2520at%25204.01.18%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Df953fd11-c8e2-431d-8546-0f1575ed212f&width=300&dpr=4&quality=100&sign=8c40d176&sv=2)
Deleting or Editing a Category in Master Data [](https://docs.zeron.one/master-data#deleting-or-editing-a-category-in-master-data)
A user can choose to delete or edit a specific category from a custom template, by clicking on the three dots on the Action tab choosing "Delete" or "Edit" and then confirming it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FNu4tu09vvZU5fhsdNI8h%252FScreenshot%25202025-02-20%2520at%25204.02.05%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Dc1b56669-21a0-4b05-9f4c-8cf9beb76618&width=300&dpr=4&quality=100&sign=2be78648&sv=2)
If the user chooses to "Edit" 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FrejjIVw71JWLkHGiz2cN%252FScreenshot%25202025-02-20%2520at%25204.02.51%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Dbe8101b2-36f9-4ae3-87d2-ec4650fbffdd&width=300&dpr=4&quality=100&sign=ff5263a0&sv=2)
If the user chooses to "Delete" 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FN9I144MnsqQIXRDmI6L5%252FScreenshot%25202025-02-20%2520at%25204.03.27%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Df9d80501-36d0-4ce6-9a6e-aeefb01b5a07&width=300&dpr=4&quality=100&sign=1605f175&sv=2)
Deleting or Editing a Template in Master Data [](https://docs.zeron.one/master-data#deleting-or-editing-a-template-in-master-data)
A user can choose to delete or edit a Template, by clicking on the three dots on the Action tab choosing "Delete" or "Edit" and then confirming it 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FU87ydbXcATojm1icEh8U%252FScreenshot%25202025-02-20%2520at%25204.14.24%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D8e641ba3-233a-47c5-827c-7c252dd24c8b&width=300&dpr=4&quality=100&sign=63fad073&sv=2)
If the user chooses to "Edit" 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FYxjx3hpft3wigy6ItRAR%252FScreenshot%25202025-02-20%2520at%25204.14.32%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D7c12ae33-a8f4-40a3-b62f-6b417a7cb911&width=300&dpr=4&quality=100&sign=f7cae1db&sv=2)
If the user chooses to "Delete" 
![](https://docs.zeron.one/~gitbook/image?url=https%3A%2F%2F1956480574-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FUuBdNVlAow8f9cZKicFF%252Fuploads%252FoMXSzk8q1oweicqDQAE6%252FScreenshot%25202025-02-20%2520at%25204.14.39%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3Deac2fa82-9859-4956-89a0-f9fe9017214b&width=300&dpr=4&quality=100&sign=2bc36a8f&sv=2)
Last updated 1 month ago
Was this helpful?
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://zeron.one/privacy-policy/).
AcceptReject
