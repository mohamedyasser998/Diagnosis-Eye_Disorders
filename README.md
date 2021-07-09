# Diagnosis-Eye_Disorders

## Business Goals
When people are sick, they must make critical decisions about when and where they should receive healthcare. Unfortunately, most people lack the medical knowledge needed to make these decisions safely. So, the goal of this project is to provide a system that helps people investigate a diagnosis of eye diseases using form to check symptoms to collect the patients’ symptoms and predict which disorder it might have and the common treatments, and let doctors decide which one is it using posts like consult with comments.

The information that will be stored in the system is the most common eye disorders, their symptoms, and common treatments for each disorder.

## Business Objective
* Creating a website that is perfect for those who cannot or do not have enough time to visit a doctor for any minor symptom.
* Help patients gain medical information about the disorder they have or how to prevent themselves from having it.
* System that helps doctors to make faster diagnosis based on symptoms.
* Provide any possible treatment for each disorder to give patients better knowledge about how sever those symptoms are and probably help doctors as reference for common ways to treat this illness.

## Business Rules
* Users are divided into two types (patient and doctor, both have email, first name and last name.
* Patients can have zero or more illness and one or more symptoms.
* Doctors have bio, profile picture, social media sites (like Facebook), academic title, specialty, employment history, experience, phone number and clinic location
* Illness has name, severity, treatment and one or more symptoms
* Consults has one or more symptoms. Consults have two foreign keys: patients id and illness name.
* Consults have one or more comment. Comment has body and two foreign keys : user id and consult id
* Appointment has time, date, status and two foreign keys: patient id and user id

## Use Case
A user feels sick in his eyes but is not sure what it could be. Patients can submit their symptoms in the check-symptoms form and it will output the possible illness giving him the option to create post (consult to get opinions from doctors in comment) or not. If Patient chose to post the consult he can read/write comments as a way to communicate with doctors (patient can only comment in his own post/consult). Users can open view the doctors signed up in the website and the specialty by going to doctors page and visit any doctor profile page to find more info about him and how to reach him with provided social media accounts.

Doctor can see the posted consults (symptoms and the generated illness) and comment his opinion if the illness is one of the listed or something else. Doctors can edit their profiles to provide more info about themselves to help patients find exactly what they are looking for easier.

## Scope of Work
* Developing the Front-End which has a form in which user login and go to a form filling his symptoms in a checkbox.
* Page to list doctors signed up in the application.
* Page to list consults posted and each consults detailed view with comment section.
* Profile page for doctors that shows information about them.
* Page to make appointment with specific doctor.
* Developing the Back-End to determine the possibility of have any disorder according to the symptoms collected. And post the checked symptoms with the disorder and user’s name.
* Back-End to give permissions for users in each page (like patient cannot comment on other patient consults).
* Back-End to check which appointment was taken by another patient to remove it from the list for other patients.
* Designing the Database to store all the famous eye diseases, their symptoms, and their treatments. 
