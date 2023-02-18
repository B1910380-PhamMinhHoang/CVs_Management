# CVs Management Application
A small application using the microservices architecture and Natural Language Processing field manages interviewees' CVs more efficient.
#
Technologies: VueJs, Flask, Docker.

Architecture: Microservices.

Special knowledge: Natural Language Processing, Machine Learning.
#
Architecture of the application:

![image](https://user-images.githubusercontent.com/101157957/219721141-7e7c17a6-3cbb-4db5-884d-63f0b2e7cc3b.png)

#
Folder structure:
+ Frontend-microservice: contains source code of the user interface (UI) for interviewer to access and manage interviewees' CVs.
+ Folder-microservice: contains source code of the folder service managing folder information.
+ CV-microservice: contains source code of the CV service managing CV information.
+ Preprocessing-microservice: contains source code of the service preprocessing text before using the text in a CV.
+ Inverted-index-microservice: contains source code of the inverted index dictionary service managing words/terms and information about CVs contain words.
+ Search-engine-microservice: contains source code of the search engine service providing the searching CVs function.
+ Resume-examples: contains some example CVs for you to test the application.
#
How to run the application: 
1. You can clone this repository to your local computer. 
2. At the folder where the docker-compose.yml file is located, you execute the command "docker-compose up --build" in the terminal to run containers (services) which requires your computer has installed Docker. (Currently running the docker compose file is having an error, you can run each service individually to check)
3. Then you can use the user interface of the application as an employer via the link http://localhost:5173/
#
Current issues:
+ Having communication problems between microservices, between containers in Docker (a service can't send HTTP requests to others service using requests library).
![image](https://user-images.githubusercontent.com/101157957/219746798-e3e0f319-a798-4d66-a121-821ad30fd4e8.png)

+ Can't access the frontend service if I create the container by running the docker-compose file.

+ Can't create the search-engine-service service because it can't install the numpy library if I create the container by running the docker-compose file.
![image](https://user-images.githubusercontent.com/101157957/219756816-8f42147c-a4fa-446a-b3df-51936d9d9540.png)

+ Haven't used a database.

Current results:
+ Each microservices work well when testing each microservice individually.

+ Interviewees can upload CVs and their information to the application via the frontend-microservice.
![image](https://user-images.githubusercontent.com/101157957/219829221-e036e7dd-b069-48fc-a164-eb80530014b4.png)

+ Interviewers can manage CVs and folders by using the user interface.
  - See all folders:
  ![image](https://user-images.githubusercontent.com/101157957/219758011-6dd6bfa1-ecfe-454f-8634-468d752b92b7.png)
  - See all CVs of a folder:
  ![image](https://user-images.githubusercontent.com/101157957/219758113-12f8deb5-2916-4751-b25e-5a0f3a2a4c0b.png)
  - See detail of a CV:
  ![image](https://user-images.githubusercontent.com/101157957/219758181-cce622fc-1c9a-41c7-af19-6c4bb10af1cc.png)
  - After clicking the "More detail" button:
  ![image](https://user-images.githubusercontent.com/101157957/219758411-ca4480d2-2581-4eb0-a9ec-07137bcab8b1.png)
  - See the form that will be sent to Interviewees:
  ![image](https://user-images.githubusercontent.com/101157957/219829217-55ff7e98-0e5a-4314-a27b-89818937338d.png)

+ Interviewers can manage CVs via the cv-microservice.
![image](https://user-images.githubusercontent.com/101157957/219742706-ff727e93-78b7-417b-85c0-19558387f588.png)

+ Interviewers can manage CVs' folder via the folder-microservice.
![image](https://user-images.githubusercontent.com/101157957/219743146-971fcfbd-37c2-4d53-8221-c53a27bc2e97.png)

+ The application can preprocessing text via the preprocessing-microservice.
![image](https://user-images.githubusercontent.com/101157957/219744136-a5100a70-eccc-4902-88d8-f8db311dcb70.png)

+ The application can convert text into a vecto using TF-IDF via the inverted-index-microservice.
![image](https://user-images.githubusercontent.com/101157957/219744480-b2101045-9279-4ab1-baaf-62cec8600136.png)

+ The application can search for CVs with a query via the search-engine-microservice.

Plans for future:
+ Using databases to manage data.
+ Implementing the job recommendation function for CVs.
