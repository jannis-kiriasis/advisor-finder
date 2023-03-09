# Project 4 - The Advice Found

[Advice Found live demo](https://advisor-finder.herokuapp.com/)\
[Advice Found repository](https://github.com/jannis-kiriasis/advisor-finder)

## Table of contents
-  [Introduction](#introduction)
-  [Ecommerce business model](#ecommerce-business-model)
-   [User Experience (UX)](#user-experience-ux---user-stories)
-	[Features](#features)
-	[Where user stories meet features](#where-user-stories-meet-features)
-	[Wireframes](#wireframes)
-  [Features left to implement](#features-left-to-implement)
-	[Designs](#design)
-  [Accessibility](#accessibility)
-  [SEO](#seo)
-  [Planning](#planning)
-  [Data model](#data-model)
-	[Technologies and tools used](#technologies-and-tools-used)
-	[Testing](#testing)
-	[Issues fixed](#issues-fixed)
-	[Known bugs](#known-bugs)
-	[Deployment](#deployment)
-  [Acknowledgements](#acknowledgements)

## Introduction

Advice Found is a platform that matches financial advisors to financial advice seekers. 

Advice seekers can find financial advivors and meet them online through the platform.

Many people don't even know who financial advisors are and what they do.

Someone may thing they are for wealthy people.

The reality is that a financial advisor can help us decide whether we should start a private pension or an investment plan.

Whether we need a savings fund or an income protection.

Those who know they need a financial advisor, may struggle finding a good one.

Advice Found is for both those categories. 

If you know you need financial advice, use Advice Found to find the best solution for you.

If you don't know you need one, our resources may help you figure it out.

Let me tell you, you'll need financial advice at some point in your life. 

If you are not part of the thousands of people looking for financial advice in Ireland, you will, soon.

![queries about financial advice](./media/README-files/financial-advice-keywords.png)

This is what you can do with Advice Found:
1. Register as an advice seeker / financial advisor.
2. Match a financial advisor that suits you / find new clients.
3. Buy a consultation with an advisor / generate more income.

### Who is Advice Found for?
Advice Found is for advice seeker and financial advisor.

### What Advice Found offer:
- A simple registrtion form for Advice Seekers and Financial Advisor.
- An algorithm that matches the advice seeker's need with the financial advisor's specialisation.
- A chat to connect the two parties.
- A consultation scheduling system.
- A checkout system.
- An online consultation platform.
- A dashboard for financial advisors to see all of their clients and consultations scheduled.

![Advice Found responsive design](./media/README-files/I-am-responsive.png)  


## Business model

Advice Found put together financial advisers and financial advice seekers. It offers them a platform to meet and communicate.

It is an opportunity for advisors to find new clients online without having to worry about managing payment 
and marketing their business. That is what Advice Found do.

It is also an opportunity for seekers to to be matched with an advisor that knows what do to.
Every situation is different and many seekers don't know where to start from when looking for financial advice.
It's their money we are talking about so they want to be carefull. From here the idea of a 'best match'.

## Where does Advice found revenue come from?

At the moment Advice Found adds a 5% fee on the transactions. So everytime a consultation is confirmed,
Advice Found makes 5% of it. The fee is on the seekers. To grow the revenue it is also possible to apply a fee to the advisors.

The idea is that seekers and advisors can build a long lasting relationship on the platform. The risk is that once the 2 parties get to know each other, they make the conversation off the platform. For this reason it's important to keep the payment on the platform and keep building features and tools that advisor and seekers would use manage their finances. The likes of tax calculators, budget calculators, savings and investment growth calculatorsl, financial health check etc.

The more tools we can build to keep the engagement on the platform and the more seekers and advisors will come back to use it.

In order to onboard brokers, there will be a mix of offline and online channels. 

To onboard seekeres, digital channels will be the favourites with a mix of organic and paid search and social media.

More on SEO and marketing in the following paragraphs.

## User Experience (UX) – The needs
Now that we are familiar with Advice Found target audience and offering, we are looking at the needs the app users may have. 

I have identified 3 main stakeholders (you guessed them by now):

### The advice seeker (AS)
The advice seeker is looking for a financial advisor and doens't know how to choose one or where to find one.

The advice seeker wants a financial advisor close to its location and that can best solve their issue.

The advice seeker wants to be guided in the choice. This is because the market is full of advisors it is often not clear 
what advisors do and how they can help.

### The financial advisor (FA)

The financial advisor wants to find new leads. An online platform can extend their reach to the entire country. They will
not be limited to local clients as it is more common for brick and mortar businesses.

The financial advisor nees to be able to talk to their clients from remote and keep track of all the appointments.

### The Advice found (AF)

The company needs to make sure that the advisors are legit businesses.

They also need to guarantee an afflux of possible clients to the platform so that advisors will also join.

## Epics and User Stories

Following, you can find the epics and the user stories breakdown used to plan the development of the app.


### Epic 1 - The profiles: The Advisers and the Seekers need to be able to create profiles that they can cancel and update.


#### USER STORY 1: Advisor profile creation

As a financial adviser,
I want to register to the platform by creating my advisor profile,
so that I can market my specialisations to potential clients.

**Acceptance criteria:**
- The adviser's required information is a business name, business address, email, phone, business description, advisor photo/logo, location and specialisations, and registration number.
- Log-in details and user profile are created simultaneously
- Use defensive design to avoid mistakes
- Implement real-time feedback on the action taken

**Subtasks:**
1. Create model AdviserUserProfile
2. Create model Specialisation
3. Create model Location
4. Create basic HTML navigation with sign-in / out, create adviser profile
5. Create add adviser profile form (template, view and URLs)
6. Add on-page notification of profile created
7. Add defensive design: Are you sure you want to submit your profile for approval?
8. Create an adviser profile page (template, view and URLs)


#### USER STORY 2: Advisor edit profile

As a financial adviser,
I want to edit and cancel my profile
so that if I don’t work with this app anymore or make changes to my business profile, those changes are visible to potential customers.

**Acceptance criteria:**
- All the Adviser information can be edited
- Use defensive design to avoid mistakes
- Implement real-time feedback on the action taken
- The adviser can pause their account not to get other clients and not be shown

**Subtasks:**
1. Create an edit button in the Adviser profile template with views and URLs
2. Create an edit adviser form template with views and URLs
3. Add on-page notification of profile updated request sent
4. Add defensive design: Are you sure you want to submit your profile update request for approval?
5. Add a button to make advisor active /inactive
6. Add active/inactive defensive design

Dependency US 1


#### USER STORY 3: Admin registration approval

As an admin,
I want to approve the adviser registration request and edit requests so that
I can validate the quality and legitimacy of the information declared.

**Acceptance criteria:**
- Admin needs to approve new profiles and edit requests before the updates are published
- Approved or not approved status needs to be reflected on the adviser profile page

**Subtasks:**
1. Create admin panel
2. Create approve new profile button in the admin panel
3. Create approve edit request in the admin panel
4. Add pending approval status in the Adviser profile page (template and views)
5. Add visual feedback in the Adviser template when the profile is approved
6. Add visual feedback in the Adviser template when the profile is not approved
7. Add visual feedback in the Adviser template when the edit request is approved
8. Add visual feedback in the Adviser template when the edit request is not approved


#### USER STORY 4: Seeker profile creation

As an Advice Seeker,
I want to register for the app and find the best financial advisor so that
I can find an advisor.

**Acceptance criteria:**
- Give a Seeker the ability to register 
- The Seeker required information are: name, address, email, phone, location and need.
- The Seeker must log in in order to create a profile
- Implement real-time feedback on the action taken
- Log-in details and user profile are created simultaneously

**Subtasks:**
1. Create model SeekerUserProfile
2. Create add seeker profile form (template, view and URLs)
3. Add on-page notification of profile created
4. Create a Seeker profile page (template, view and URLs)


#### USER STORY 5: Seeker profile edit and cancel 

As a Seeker,
I want to edit and cancel my profile so that
if I don’t work with this app anymore or make changes to my profile, those changes are visible.

**Acceptance criteria:**
- All the Seeker information can be edited
- The profile can be cancelled
- Use defensive design to avoid mistakes
- Implement real-time feedback of the action taken

**Subtasks:**
1. Create an edit button in the Seeker profile template with views and URLs
2. Create an edit seeker form template with views and URLs
3. Add on-page notification of profile updated request sent
4. Add defensive design: Are you sure you want to submit your profile update request for approval?
5. Create a delete button in the Seeker profile template with views and URLs
6. Add on-page notification of profile deleted
7. Add defensive design: Are you sure you want to delete your profile 

Dependency US 1, US 4


### Epic 2 - The Matcher: The matcher connects Seekers and Advisers and shows the best match and the other results based on the algorithm criteria (specified in user stories).


#### USER STORY 6: Matching logic

As an advice seeker,
I want to be matched with a financial advisor
that best suits my need.

**Acceptance criteria:** 
- One main option must be given to the Seeker
- The Seeker can still see other possible good options
- The match must be based at least on location and specialisation/need
- Add other relevant advisors after the best match
- Notify the advisor when there is a new match

**Subtasks:**
1. Create a few Adviser profiles
2. Create a few Seekers profiles
3. Create a match template (HTML + CSS)
4. Create a view to filter Advisers by the Seeker’s location, need
5. Create URLs
6. Create queryset to add to the template other possible advisors


#### USER STORY 7: Clients and matches view

As an Adviser,
I want to see all the Seekers I matched and the seekers who are already clients so that
I can follow up on conversations easily.

**Acceptance criteria:** 
- See a list of the Seekers matched and their profile information (Name, need, location)
- See a list of the clients and their profile information (Name, need, location)
- See the individual conversations with the Seekers

**Subtasks:**
1. Create clients  and matches template
2. Create views
3. Create URLs


### Epic 3 - The chat: Creation of the app that will facilitate the Seeker and the Adviser conversations.


#### USER STORY 8: The chat - Seeker

As an advice seeker,
I want to message the advisor I matched with so that
we can schedule a consultation.

**Acceptance criteria:** 
- On the advisor’s page, the seeker must find a button to message the advisor
- I want to be notified when I have a message to read

**Subtasks:**
1. Create a chat template on the seeker’s advisor page
2. Create chat view and URL
3. Create message template
4. Create message form
5. Create model message
6. Email advisor when there is a new message


#### USER STORY 9: The chat - Advisor

As an advisor,
I want to message the seeker I matched with so that
we can schedule a consultation.

**Acceptance criteria:**
- On the client's page, there is a button to open the client’s profile whit the chat
- On the client profile, there is a message form to message the client
- On the client profile, the advisor can see the client’s details and chat
- The client must be notified when there is a message to read

**Subtasks:**
1. Create a button to open the chat or client page
2. Create a client profile template page
3. Create client profile view and URL
4. Create conversation logic on the client profile page
5. Send an email to the client when the advisor adds a message


#### USER STORY 10: Advisor view

As an Advice seeker,
I want to see all the Information of the advisor I matched with and our conversation so that
I can find our information easily.

**Acceptance criteria:** 
- On the advisor page, I have to find his business info and the chat to contact them easily

**Subtasks:**
1. Create advisor template
2. Create views
3. Create URLs
4. Epic 4 - The order: Creation of the checkout and payment processes.


#### USER STORY 11: Schedule consultation

As a financial advisor,
I want to schedule a consultation,
so that I can meet the Seeker.

**Acceptance criteria:**
- The advisor can send an appointment with a link to a video chat
- The advisor received an on-screen notification on consultation sent
- The appointment appears in the chat
- The Seeker receives an email with the appointment details and a link to pay
- The Seeker receives the appointment by a chat with a button to confirm
- When the first consultation is scheduled, the adviser becomes the Seeker’s adviser and it will be visible in the seeker's profile

**Subtasks:**
1. Create consultation form
2. Create consultation message view and template
3. Create a message output template
4. Create consultation model
5. The seeker receives an email with consultation details
6. Seeker sees the appointment in the chat with the advisor


### USER STORY 12: Appointments

As an advisor,
I want to see all the appointments I have scheduled,
so that I can keep up with every client.

**Acceptance Criteria:**
- Appointments need to be ordered by the closest one
- Appointments need to be labelled confirmed or not confirmed

**Subtasks:**
1. Create template and URLs for appointment page
2. Create appointment view
3. Create a view to mark the appointment confirmed after payment 	
4. Change consultation status
5. Disable cancel button
6. Seeker seeks link to the meeting instead of to confirm the consultation


### USER STORY 13: The checkout

As a seeker,
I want to pay for the consultation
so that I can talk to an Adviser.

**Acceptance Criteria**
- The Seeker needs to go through the checkout and pay for the consultation
- The Adviser receives an email with the payment confirmed
- The Seeker receives an email with the confirmation
- The link to connect to the advisor becomes active

**Subtasks:**
1. Order model
2. Create checkout form
3. Create checkout views 
4. Create checkout template
5. Connect stripe
6. Send payment intent to stripe
7. Add on page notification of order processed
8. Send email to seeker with consultation schedule and payment link
9. Remove button on checkout to pay after the consultation has been paid (redirect to order page)


### USER STORY 14: Notify advisor of consultation confirmed

As an adviser, 

I want to be notified about the payment success and the consultation confirmation 

so that I can get ready for the meeting.

**Acceptance Criteria**
- Send an email to the Adviser with the payment confirmation and the link to access the chat.

**Subtasks:**
1. Create send the email logic
2. Create the email template


Mapping out the user stories helped me easily identify the problems the application solves:

- This app helps seekers who are not sure where to find financial advice
- Advisors are selected based on the seeker need and close to their location
- Advisors can find new clients easily that they can help as they specialise in the seekers' need
- Advisors can find clients nationwide
- Advisors don't need to handle online payments of install any technology
- Payments are happening securely online


## Features

In the following paragraphs, we are going to see what features appear on the website and where they meet the users' needs.

### 1. Main navigation

   The main navigation in different from logged in users and logged out users.

   Logged out users can only see the links to login and register to the app.

   Navigation is also different for users that have completed the signup process and users that haven't completed the sign up process.

   Users that haven't completed the signup process can only see a link to logout.

   Users that have completed the signup process see different navigation whether they are seekers or advisors.

   Advisors see the following links:

   ![Advisors nav](./media/README-files/navigation-advisor.png)  

   They are self explenatory. The difference between a match and a client is that a client has accepted a consultation, a match hasn't.

   Seekers see the following links:

   ![Advisors nav](./media/README-files/navigation-seeker.png)  


### 2. The signup - User creation

The first part of the signup process requires the user to create an account with their personal informations.

   ![Advisors nav](./media/README-files/navigation-seeker.png)  

### 2. The signup - User choice

The second part of the signup process requires users to select whether they are a seekers or advisors.

### 2. The signup - Seeker or advisor profile creation

The third step of the signup process requires users to complete the seeker or advisor forms with information specific to each user type.

**Advisor form**
   ![Advisors nav](./media/README-files/advisor-form.png)  

**Seeker form**
   ![Advisors nav](./media/README-files/seeker-form.png)  


### 3. The matching page

On the matching page, seekers are presented with their best matches. Should they decide to match with another advisor, they have the option to do it.

The seeker is matched with an advisor based on the following criteria:
1. seeker's need is equal to the advisor specialisation
2. seeker's location is equal to the advisor location
3. a randomiser select 1 advisor out of the restricted pool to make sure it isn't always the same advisor

In case there isn't an advisor in the same city, the match is based on the need and the randomiser.
There should always be an advisor for every specialisation, however in case it is also missing, the advisor selection is randomised.

Below the best match, the is the remaining list of advisors available in random order in case the seeker wants to choose a different advisor.

To be included in the matching logic, the advisor must:
1. have been approved (by Advice Found)
2. not be inactive (advisors can deactivate their profile if they don't want to be matched)

Currently, the seekers can't be rematched. This feature can be added in the future. Anyway generally, this is a long lasting relationship.

### 4. The seeker profile

On this page, the seeker can review their generalities and update them if needed.

### 5. The seeker's advisor

On this page, the seekers can see the main information about their advisors and can send a message.

Here is where the seekers will receive the messages and the consultation proposals.

On this same page, on the consultation proposals, the seeker can accept the consultation and go through the checkout.

Only after the checkout is completed, the seeker receives the video conference link to meeet the advisor on the date agreed.

### 6. The checkout

On the checkout page, the seekers can review their fees, their personal details and pay.

The checkout page doesn't appear if there are not consultations to checkout.

### 7. The checkout success

After the checkout is completed, the user sees a checkout completed page with a recap of their order.

They receive an email with the details of the consultation.

The can now see the meeting link also on their advisor's consultation proposal.

### 8. The advisor profile page

The advisor can review their personal details on their profile page.

For security reasons, if the advisor needs to make an change to their profile, the amendments needs to be approved by Advice Found.

This is to make sure that the advisor are real businesses and registered.

From this page, the advisor can deactivate their profile. Deactivating the profile means that the advisor will not receive new clients.

The advisor can't cancel their profile as the seekers will need to be re-matched. This fetuare could be developed on a future sprint.

### 9. The advisor's appointments page

On this page, the advisors can see all the appointment they have scheduled and their status. An appointment must be paid by 
the seeker before it's confirmed.

From this page the advisor can also navigate to the seeker's profile pages.

### 10. The adviror's seekers profiles

On their client personal pages, the advisor can see all the main details about a client as well a schedule a meeting and send a normal message.

The advisor can schedule only 1 meeting at a time. If their is a consultation pending confirmation, the option to schedule another meeting is disabled.

On this page the advisor also see the full conversation wit the client.

### 11. The consultation scheduler
With the meeting scheduler, the advisor can schedule a meeting with the seeker.

The fields required are date (can't be a past date), time and consultation fee.

The meeting link is automatically generated with a thid party tool https://gotalk.to/. it's fee to use and doesn't require an account.

The seeker receives the meeting link after the payment is completed.

### 12. The clients page

On the clients page, the advisor sees a list of all of their clients, and a link to go to their personal profiles.

### 13. Login

A form to authenticate the user to the app. A non authenticated user who tries to navigate the site will always be redirected to the sign in page.

Page feedback has been implemented when a user logs in and signs up.

![Login](./media/README-files/sign-in.png)  

### 14. Feedbacks and popups

The application let the users know every time they perform an action whether it has been completed or not.

![Defensive design](./media/README-files/defensive-design.png)  

![Feedback](./media/README-files/feedback.png)  

### 15. 404 and 500 error pages

The 404 and 500 error pages handle errors nicely explaining to the user what is happening and offering a way to exit the error.

[Custom 404 page](./media/README-files/404.png)  

## Where user stories meet features

In the following table, I’m going to match features with user stories and the issues the app solves. All the user stories, features and needs outlined in the paragraphs above have a number that corresponds to the number you see in the table below.

|                    User stories                    | Features  |
|:--------------------------------------------------:|-----------|
| E1 US1 - Advisor profile creation                  | 2         |
| E1 US2 – Advisor edit profile                      | 8         |
| E1 US3 – Admin registration approval               |           |
| E1 US4 – Seeker profile creation                   | 2, 14     |
| E1 US5 – Seeker profile edit and cancel            | 4, 14     |
| E2 US6 – Matching logic                            | 3, 14     |
| E2 US7 - Clients view                              | 1, 12     |
| E3 US8 - The chat - Seeker                         | 1, 14     |
| E3 US9 - The chat - Advisor                        | 1, 10, 14 |
| E3 US10 - Advisor view                             | 1, 7      |
| E3 US11 - Schedule consultation                    | 1, 11     |
| E3 US12 - Appointments                             | 1, 8, 14  |
| E3 US13 - The checkout                             | 6         |
| E3 US14 - Notify advisor of consultation confirmed | 14        |


## Wireframes

The first draft of the website was completed by creating wireframes using Balsamic.

Below you can find a link the initial wireframes created. The main goal when I created 
the wireframes was to fulfil the user story requirements. Later on during the development
I've upgraded the styling getting to the final version that you see live.

![Wireframe](./media/README-files/wireframes.pdf)  


## Features to be implemented

- Let advisors cancel their profile and handle advisor's clients
- Let seekers find a different advisor
- Create admin dashboard to see Advice Found revenue
- Build a report to see the most active advisors and those scheduling more meetings


## Design

In the following paragraph, I'm going to explain the colours, typography and imagery choices.

### Colours

I've used a similar colour palette to a project I previously realised (pp2 and pp4) so the reasoning behind the colour choice is very similar.

The main colour used is a shade of blue (sapphire). Blue is a calm and serene colour. It is often associated with stability and reliability. I've increased a bit the contrast ratio with light backgrounds to achieve accessibility best scores.

All the main buttons are in brown. It's different enough to differentiate from the main sapphire colour. The secondary buttons are white with brown borders.

A lighter shade of brown was used to highlight the best match, the seeker's advisor and the advisor's clients profiles.
It was also used to color the background of the messages sent.

![Color Palette](./media/README-files/colors.png)  

All the text colour combinations have been tested for accessibility and they all achieve WCAG AAA.
- [Colour contrast test: shappire on white](https://webaim.org/resources/contrastchecker/?fcolor=054FB9&bcolor=FFFFFF)   
- [Colour contrast test: brown on white](https://webaim.org/resources/contrastchecker/?fcolor=9D3801&bcolor=FFFFFF)   

Tested with [Contrast checker](https://webaim.org/resources/contrastchecker/).

### Typography

The typography was chosen for my liking, again I've used it in previous projects PP2. Open Sans is a very popular font if not the most popular.

I used [Open Sans](https://fonts.google.com/specimen/Open+Sans) for all body elements.  

The fallback font used is Helvetica for all body elements.

### Imagery

The only image used in this project is the favicon.


## Accessibility

As mentioned above, all the colour combinations used for text passed a contrast ratio test.

I've also aria labels to describe links.  
The pages have been structured using semantic HTML markup.  


## SEO

This app has been created for advice seeker to find indipendent financial advice. The main action and offering of the homepage is giving users a way to get financial advice. Therefore, the search intent I'm going after is those of users looking for financial advice. 

With a quick brainstorming I thought that users looking for financial advice on Google would look for:
- Find a financial advisor
- find a financial advisor in Ireland
- financial advice
- financial advisor finder
- financial planners
- financial advisors
- Indipendent financial advisors 
- Indipendent financial advisors in Ireland

Then I validated my ideas with Google Ads keywords planner.

From here the question is: what do people looking for financial advisors want to know? 
I need to answer this question to make the content exhaustive.
By looking at the serp results seems like the majority of results are actual advisors.
So looking at what content they have on their page, the most common topics are:

- what benefits seekers can get from them
- the services / products they cover
- testimonials / client stories

So this is what I'm going to include on the homepage.
In a real world, I would include also:

- number of clients and advisors using the platform (social proof)
- review widgets, the like of Trustpilot (social proof + I can add schema markup on the page)

![Google Snippet](./media/README-files/google.png)  

The only 4 public pages of my site are:

- The homepage 
- signup
- login
- password reset

On all of the 4 pages I've set:

- Open graph tags ( to render the image and title nicely when the page is shared on social media)
- meta description
- meta robots
- canonical link
- title tag

Those are not necessary for all of the other pages since the are behind a login wall and search engine crawlers can't crawl (and so index) them.

I also made sure that:
- There aren't broken internal links
- All external links have a rel tag attribute
- 404 errors and server errors are handled nicely
- accessibility score is good (more on the Lighthouse report below)
- Core web vitals are good (more on the Lighthouse report below)


## Planning

To build this app I've used [Jira](https://kiria.atlassian.net/jira/software/c/projects/AF/boards/3/backlog?atlOrigin=eyJpIjoiYzI4YTU2NjJkY2IyNDBkZGJkNWM5Nzg5MGNkNWI5ODciLCJwIjoiaiJ9) (Access was given to the CI assessment team) as an agile tool. 

The development took 5 sprints of different lengths in terms of days but with similar total story points (around 27-29 per sprint).

The tasks in each sprint were prioritised using the moscow method and the priority settings in the task details as well as using labels. With the moscow method, user stories and tasks are categorised in: Must do, Should do, Could do, Won't do.

In every sprint, about 60% of the user stories had a priority level of Must do or Should do. The remaining 40% was Could do or Won't do.
Many of the tasks and user stories that were marked as won't do in a sprint, were marked as should do or must do in the following sprint.

You have probably seen the epics and user stories few paragraphs above. They are also available in the Jira board.


## Data model  
For this app, I've created 10 data models and inherited others from Django Allauth.

In this paragraph I'm going to focus on the data models I've created and the most important inherited ones.

For more details on all the fields and models available and their relations, you can view this [database schema](/media/README-files/data-model-advice-found.png).

**Location**
Contains an Irish city or town.
- city 

**Specialisation**
Contains an area of specialisation of the financial advisors or need of the seekers.
- type

**User model**  
Contains the personal details of a user:
- username
- first name
- last name
- email address
- password

**UserProfile**
Contains the type of user (seeker or advisor):
- user_type
- user FK

**AdvisorUserProfile**  
Contains the business generalities of the user:
- user FK
- business_name
- business_description
- postcode
- town_or_city FK
- street_address
- specialisation FK
- registration_number
- approved
- active

**SeekerUserProfile**
Contains the generalities of the seeker.
- user FK
- postcode
- town_or_city FK
- street_address
- need FK

**Match**
Contains the FK to seeker and advisor who matched.
- advisor FK
- seeker FK
- matched_on (date of match)

**Consultation**
Contains the details of the online appointment setup by thr advisor.
- match FK
- price
- date
- time
- link
- status (confirmed or not)
- created (created on)

**Order**
Contains the details of the order:
- order_number
- consultation FK
- seeker FK
- name
- last_name
- email
- postcode
- town_or_city FK
- street_address
- date
- fee
- af_fee
- grand_total
- stripe_pid
- paid

**Message**
Contains the message send from a seeker to the advisor in the chat or viceversa.
- match FK
- user
- body
- created_on


For more information on the field types and the relations between models, view this [database schema](/media/README-files/data-model-advice-found.png).


## Technologies and tools used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://it.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- Version control: [Git](https://git-scm.com/)
- Public repository: [GitHub](https://github.com/)
- Google Font: [Open Sans](https://fonts.google.com/specimen/Open+Sans)
- Wireframes: [Balsamiq](https://balsamiq.com/)
- Colours accessibility: [Webiam](https://webaim.org/resources/contrastchecker/)
- Uniform alert on all browsers: [SweetAlert](https://sweetalert2.github.io/)
- Colors darkener: [Color darkener](https://mdigi.tools/darken-color/)
- Color lightener: [Color lightener](https://mdigi.tools/lighten-color/)

## Testing

I've carried out the following tests:

1. [HTML validation](#html-validation)
2. [CSS validation](#css-validation)
3. [JavaScript validation](#js-validation)
9. [Automated python testing](#automanted-teting)
4. [Manual testing](#manual-testing)
5. [Browsers compatibility](#browser-compatibility)
6. [Responsiveness testing](#responsiveness-testing)
7. [User stories testing](#user-stories-testing)


### HTML validation

All the pages passed the HTML validation with no errors or warnings.
- [account/signup.html](./media/README-files/signup-w3c.pdf)  
- [account/login.html](./media/README-files/signin-w3c.pdf)  
- [account/signout.html](./media/README-files/signout-w3c.pdf) 
- [dashboard.html](./media/README-files/dashboard-w3c.pdf)  
- [my-projects.html](./media/README-files/my-projects-w3c.pdf)  
- [my-approvals.html](./media/README-files/my-approvals-w3c.pdf)  
- [project-details.html](./media/README-files/project-details-w3c.pdf)  
- [create-project.html](./media/README-files/create-project-w3c.pdf)  
- [edit-project.html](./media/README-files/edit-project-w3c.pdf)  
- [400.html](./media/README-files/404-w3c.pdf)  
- [notifications.html](./media/README-files/notification-w3c.pdf)  


### CSS validation

Style.css passed the CSS validation with no errors.
- [css validation]()  


### JS validation 
The JavaScript files have been passed through [Jshint](https://jshint.com/): I have added a few semicolumns and removed unused variables. There are no issues with the code.

There are also no errors in the Console (Google Developer Tools).


### Automated testing

I've used [Django testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/) to test the application python code.

The tests were run on the SQLite3 local database.

I've tested the following files in project_management:

[test_forms.py](https://github.com/jannis-kiriasis/the-checklistar/blob/7ba211de1ec5f6ccd62c0eda53cb7d490ebfe32e/project_management/tests_forms.py)  
[test_models.py](https://github.com/jannis-kiriasis/the-checklistar/blob/7ba211de1ec5f6ccd62c0eda53cb7d490ebfe32e/project_management/tests_models.py)  
[test_views.py](https://github.com/jannis-kiriasis/the-checklistar/blob/7ba211de1ec5f6ccd62c0eda53cb7d490ebfe32e/project_management/tests_views.py)  

I've tested the following files in the notification folder:
[test_models.py](https://github.com/jannis-kiriasis/the-checklistar/blob/7ba211de1ec5f6ccd62c0eda53cb7d490ebfe32e/notification/tests_models.py)

Over 84% of the python code has been tested with automated tests:

Project management tests coverage  
![project_management](./media/README-files/project-man-tests.png)  

Notification tests coverage  
![notification](./media/README-files/notification-tests.png)  


### Manual testing

I've tested that the different functionalities of the website work as intended.

| Test Label                                                              | Test Action                                                                                                                                        | Expected Outcome                                                                                                                                                                                                                   | Test Outcome |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Nav / mobile nav - Logo click                                           | Click on the logo in the navigation.                                                                                                               | It redirects to the homepage (“/”).                                                                                                                                                                                                | PASS         |
| Nav – sign up                                                           | Click on sign up in the navigation.                                                                                                                | It redirects to the sign-up page “/accounts/signup/”.                                                                                                                                                                              | PASS         |
| Sign up – form validation                                               | On “/accounts/signup/” enter an incorrect form value or not enter a value (exclude the optional fields). Click sign up.                            | Sign-up will fail and a failing error will appear next to the field failed.                                                                                                                                                          | PASS         |
| Sign up - redirect                                                      | On “/accounts/signup/” complete the form and click on sign up.                                                                                     | You will be redirected to the homepage (“/”).                                                                                                                                                                                      | PASS         |
| Sign in - feedback                                                      | On “/accounts/signup/” complete the form and click on sign up.                                                                                     | After the redirect, a green feedback message will appear on the bottom left.                                                                                                                                                        | PASS         |
| Nav / mobile nav - login                                                | Click on the login in the navigation.                                                                                                                 | It redirects to the login page “/accounts/login/”.                                                                                                                                                                                 | PASS         |
| Sign in – form validation                                               | On “/accounts/login/” enter an incorrect form value or not enter a value. Click sign in.                                                           | Sign-in will fail and a failing error will appear next to the field failed.                                                                                                                                                          | PASS         |
| Sign in - redirect                                                      | On “/accounts/login/” complete the form and click on sign in.                                                                                      | You will be redirected to the homepage (“/”).                                                                                                                                                                                      | PASS         |
| Sign in - feedback                                                      | On “/accounts/login/” complete the form and click on sign in.                                                                                      | After the redirect, a green feedback message will appear on the bottom left.                                                                                                                                                        | PASS         |
| Nav / mobile nav – create a project                                     | Click on ‘Create a project' in the nav.                                                                                                            | You’ll be redirected to “/create-project”.                                                                                                                                                                                         | PASS         |
| Create a project – form validation                                      | In “/create-project” test all inputs but ‘document’ and the approvers' fields are required. Click on ‘create project’.                              | Submit will fail if you haven’t entered the required input.                                                                                                                                                                          | PASS         |
| Create a project – form validation approvers                            | In “/create-project” enter either the approver name or approval due date and click ‘create project’.                                               | Submit will fail. Both fields are required if one of the 2 is entered.                                                                                                                                                             | PASS         |
| Create a project – Add approvers                                        | In “/create-project” use the + and – buttons to add or remove as many approvers as needed.                                                         | Clicking on + will add a slot for an extra approver. Clicking on – will remove the last slot.                                                                                                                                      | PASS         |
| Create a project – form submits | In “/create-project” complete the form correctly and fully. Click ‘submit project’.                                                                | After the click, you will be redirected to the homepage. Access the admin panel to find records of the project and approvers created in the database.                                                                              | PASS         |
| Create a project - feedback                                             | In “/create-project” complete the form correctly and fully. Click ‘submit project’.                                                                | After the submission, a green feedback message will appear on the bottom left of the screen.                                                                                                                                        | PASS         |
| Create a project - notification                                         | In “/create-project” complete the form correctly and fully. Click ‘submit project’.                                                                | A notification will appear to the approvers selected.                                                                                                                                      | PASS         |
| Create a project – title test                                           | In “/create-project” create 2 projects with the same title.                                                                                        | An error message will say that the title already exists when creating the second project.                                                                                                                                                                                                                                   | PASS         |
| Nav / mobile nav - notification                                         | In the nav click on Notifications.                                                                                                                 | A list of notifications will appear if any.                                                                                                                                                                                        | PASS         |
| Notification                                                            | In “/notifications” click on a notification and then navigate back to “/notifications”.                                                            | The notification you have clicked on disappeared from the list because you read it already.                                                                                                                                        | PASS         |
| Nav / mobile nav – all projects                                         | In the nav click on All projects.                                                                                                                  | You are redirected to (“/”).                                                                                                                                                                                                       | PASS         |
| Nav / mobile nav – My projects                                          | In the nav click on My projects                                                                                                                    | You are redirected to (“/my-projects”).                                                                                                                                                                                            | PASS         |
| Nav / mobile nav – My approvals                                         | In the nav click on My approvals                                                                                                                   | You are redirected to (“/my-approvals.”).                                                                                                                                                                                          | PASS         |
| Nav / mobile nav – Logout                                               | In the nav click on Logout                                                                                                                         | You are asked if you are sure you want to log out.                                                                                                                                                                                  | PASS         |
| Logout                                                                  | In the nav click on Logout and confirm the logout on the second screen.                                                                            | You are logged out. You can’t see the navigation options and you can click on any buttons on the /project-details pages. You are redirected to the page “/”. A Green feedback box on the bottom left will say you have logged out. | PASS         |
| All projects – project approvers                                        | In (“/”). Click on ‘View approvers’ on any project you want.                                                                                       | The project expands and you can see all approvers and their de dates.                                                                                                                                                              | PASS         |
| All projects – view details                                             | In (“/”). Click on ‘View details on any project you want.                                                                                         | You are redirected to the project details page.                                                                                                                                                                                    | PASS         |
| All projects / My projects / My approvals – completed or approved colour | Complete or approve a project.                                                                                                                     | In “/” or “/my-approvals” or “/my-projects” the project background colour turns light green if you are signed in and you are the PM (my projects) or an approver (my-approvals)                                                     | PASS         |
| Project details                                                         | Look at any project you have created on all the pages where a project collapsed or not collapsed appears.                                           | You can always see the project id, title, owner due date, attachment (if any), completion status, approvers (if any), approvers department and approvers due date.                                                                 | PASS         |
| Project details – PM buttons                                            | Log in and click on ‘view details for a project where you are not the owner.                                                                      | You can’t click on 'edit project', 'delete project' or 'complete project'.                                                                                                                                                               | PASS         |
| Project details – PA buttons                                            | Log in and click on ‘view details' for a project where you are not a project approver.                                                             | You can’t approve the project.                                                                                                                                                                                                     | PASS         |
| Project details – complete and delete 1                                 | Log in and view the details of a project where you are the owner. Click on delete project and complete project.                                    | Defensive design will ask you to confirm your choice.                                                                                                                                                                              | PASS         |
| Project details – complete and delete 2                                 | Log in and view the details of a project where you are the owner. Click on delete project and complete project. Approve also the defensive design. | You are redirected to the ‘my-projects’ page. A green feedback message on the bottom left will indicate the completion of your action.                                                                                             | PASS         |
| Project details - edit                                                  | On any project details page, click on Edit project.                                                                                                | You’ll be redirected to a prepopulated form where you can change the project information.                                                                                                                                          | PASS         |
| Project details – edit 2                                                | Change any field you want and click on ‘create a project’                                                                                          | If you have removed a required field, you’ll get an error. If you have added or removed an approver, the database is updated.                                                                                                      | PASS         |
| Project details – edit 3                                                | Update a project you own.                                                                                                                          | A feedback message on the bottom left will say you have updated the project after the form submission.                                                                                                                             | PASS         |
| Project details – comment form                                          | On any project you want, go to the project details page, fill in and submit a comment form.                                                           | The comment submitted will appear below the comment form in chronological order from the newest to the oldest.                                                                                                                     | PASS         |
| My approvals page                                                       | Go to my approvals page                                                                                                                            | You see only projects where you are an approver. Approved projects have a green background.                                                                                                        | PASS         |
| My projects page                                                        | Go to my projects page                                                                                                                             | Projects are ordered by the last created. You see only projects where you are the owner. Completed projects have a green background.                                                                                                     | PASS         |
| Approve a project                                                       | Click on ‘view details on a project where you aren’t an approver.                                                                                 | You can’t approve.                                                                                                                                                                                                                 | PASS         |
| Approve a project 2                                                     | Click on ‘view details on a project where you are an approver. Click on ‘approve project’                                                         | Defensive design will ask you to confirm the approval.                                                                                                                                                                             | PASS         |
| Approve a project 3                                                     | Click on ‘view details on a project where you are an approver. Click on ‘approve project’. Pass the defensive design.                             | A feedback message on the bottom left will say you have approved the project. You are redirected to the /my-approvals page. The background of the project you have approved will turn light green.                                | PASS         |

### Browser compatibility

All the functionality tests have been carried out and achieved a PASS on the latest versions of the following browsers:
- Google Chrome
- Safari
- Firefox
- Microsoft Edge

### Responsiveness testing

All the functionality tests have been carried out and achieved a PASS on the following screen resolutions:
- 365x667 (iPhone SE)
- 540x720 (Surface Duo)
- 1280x800 (Nest Hub Max)
- 2560x1600 (Macbook Pro M1)

The website has also been tested for responsiveness on [https://ui.dev/amiresponsive](https://ui.dev/amiresponsive?url=https://advisor-finder.herokuapp.com/).
- [dashboard.html](./media/README-files/I-am-responsive.png)  


### User stories testing

I've tested whether the user needs have been satisfied with the features created.

|                   User stories                  | Features | Result |
|:-----------------------------------------------:|:--------:|--------|
| E1 US1 - Create a project                       | 7, 11    | PASS   |
| E1 US2 – Set the project workflow               | 7        | PASS   |
| E1 US3 – Create main dashboard                  | 2, 3     | PASS   |
| E1 US4 – Edit a project                         | 7, 11    | PASS   |
| E1 US5 – Delete a workflow                      | 3, 11    | PASS   |
| E1 US6 – See all the projects open              | 4        | PASS   |
| E1 US7 - Add a comment (Create)                 | 3, 11    | PASS   |
| E1 US8 - Notify PM                              | 6        | PASS   |
| E1 US9 - Registration and sign in project owner | 8, 9     | PASS   |
| E2 US1 - See projects pending approval (Read)   | 5        | PASS   |
| E2 US2 - See project by due date                | 5, 3     | PASS   |
| E2 US3 - Approvers feedback                     | 3        | PASS   |
| E2 US4 - Approve a project                      | 3, 11    | PASS   |
| E2 US5 - Notify approvers                       | 6,       | PASS   |
| E2 US6 - Registration and sign approvers        | 8, 9     | PASS   |
| E3 US1 - The risk controller                    | 10       | PASS   |

## Issues fixed


## Known bugs

There aren't known bugs currently.

## Deployment

Below you can find all the steps to take in order to clone and deploy this application. A similar summary to setup a basic Django project and deploy it on Heroku was provided by the [Code Institute](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf).

**1. To clone the website**
1. Go to the GitHub repository [Adviser Finder](https://github.com/jannis-kiriasis/advisor-finder)
2. Open the dropdown 'Code'
3. Select the HTTPs tab
4. Copy the given url (https://github.com/jannis-kiriasis/advisor-finder.git)
5. Open 'Git Bash' on your favourite code editor and select the location where you want to save the cloned directory
6. Type `git clone https://github.com/jannis-kiriasis/advisor-finder.git` and press enter to create a local copy
7. Install the required packages by typing `pip install -r requirements.txt` in the terminal
8. In settings.py set `DEBUG=True` (Now it is set to False)
9. To push changes to the repository, type the following commands in the terminal
   - `git add .` to add changes
   - `git commit -m "Your message"`
   - `git push`

**2. To create a database with ElephantSQL**
1. Sign in with GitHub (or Sign up with GitHub) to [ElephantSQL](https://www.elephantsql.com/)
2. In the 'Instances' page click on 'Create new instance'
3. Give a name to your database, select the free 'Tiny Turtle' plan. You can leave 'tags' empty
4. Proceed to 'select region' and select the closest region to your location
5. Review and confirm your choices
6. From the dropdown menu in the navigation select the instance you have just created
7. In the 'details' view, copy the database URL

**3. Create an app on Heroku (deployment environment)**
1. Sign in (or create an account) on [Heroku](https://heroku.com/)
2. From the dashboard, click on 'Create a new app'
3. Enter a unique name and create an app
4. On the application configuration page click on "settings" (in the navigation) and then on "Reveal Config Vars"
5. Add the following Config vars keys and values:
   - 'DISABLE_COLLECTSTATIC': '1'
   - 'DATABASE_URL': 'past the database URL from ElephantSQL you have copied at point 2.7'
   - 'SECRET_KEY': 'come up with a random secret key'
6. **Back in your code editor** create a file 'env.py'
7. Add 'env.py' to the .gitignore file
8. In 'env.py' add the following code:
   - `import os`
   - `os.environ["DATABASE_URL"] = "your database URL from point 2.7"`
   - `os.environ["SECRET_KEY"] = "your secret key from point 3.5"`
9. Save
10. In 'settings.py' make sure that DATABASES and SECRET_KEY are equal to:
   - `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}`
   - `SECRET_KEY = os.environ.get('SECRET_KEY')`
11. Initialise the database with the command `python3 manage.py migrate`
12. Update the requirements.txt file with the command `pip3 freeze --local > requirements.txt`
13. Commit and push changes to GitHub (step 1.9)

**4. Host files on Cloudinary**
1. Login or create an account on [Cloudinary](https://cloudinary.com/)
2. From the dashboard, copy the "API Environment variable"
3. **On Heroku** find the Config vars (step 3.4)
4. Add the following key, value set:
   - `'CLOUDINARY_URL': 'paste your API Environment variable from step 4.2'`
5. **In your code editor** go to 'env.py' and add:
   - `os.environ["CLOUDINARY_URL"] = "your Cloudinary API Environment variable from step 4.2"`
6. Update requirements.txt (step 3.12)
7. Commit and push changes (step 1.9)

**5. Connect Heroku to GitHub**
1. **On Heroku** Go to the Application Configuration page of your application and click on the 'Deploy' tab
2. Under 'deployment method' select GitHub
3. Enter the name of the repository https://github.com/jannis-kiriasis/advisor-finder
4. Scroll down and chose automatic deployment or manual deployment then save
5. On the application configuration page click on 'Open App'.
6. Run the app https://advisor-finder.herokuapp.com/

**6. Final deployment**
1. **In 'settings.py'** set `DEBUG=False`
2. **In 'settings.py'** check if you have (or add) `X_FRAME_OPTIONS = 'SAMEORIGIN'`
3. Update requirements.txt with the command `pip3 freeze --local > requirements.txt`
4. Push to GitHub (step 1.9)
5. **On Heroku** find the Config Vars (step 3.4)
6. Remove 'DISABLE_COLLECTSTATIC': '1'
7. Deploy the app (from steps 5.4 to 5.6)


## Acknowledgements

Brian Macharia, my mentor, helped me test the website functionalities and provide excellent recommendations.

To create the README.md file I've used a previously created by me README.md [Insured README.md](https://github.com/jannis-kiriasis/insured/blob/main/README.md) and updated it as needed.

