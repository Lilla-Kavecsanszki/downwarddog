# DownwardDog Yoga Studio

This website is designed to bring together all yoga fans who are also dog owners, creating a safe place for them to practise yoga together and the opportunity for a vibrant community. 
The main focus is to be straight forward enough to save time for the user, yet to be engaging and motivating at the same time.

The user can interact with the website in various ways such as viewing relevant and uselful information on the articles page. The users, if they are registered and logged in, then can comment on the articles and also can express their opinion with a like. They can later also unlike the article, in case they changed their mind. 
The users can also see a selection of yoga classes, then also a selection of available dates and times for the relevant classes to choose from through the Yoga page. If they are logged in, they will be able to book, register their interest. After admin approval, the user is able to follow up their bookings on the My Bookings page, and also to edit or delete the bookings that they wish to.  

This full-stack framework project was built using Django framework, Python, HTML, Bootstrap and CSS. Furthermore, ElephantSQL and Cloudinary was also used to store data, images and CSS.

![Application](readme-images/responsive.png "Application")

[Link to the live project](https://downwarddog.herokuapp.com/)

# Contents

- [User Experience (UX)](https://github.com/Lilla-Kavecsanszki/downwarddog#user-experience-ux)
  - [Ideal client](https://github.com/Lilla-Kavecsanszki/downwarddog#ideal-client)
  - [User stories & Epics](https://github.com/Lilla-Kavecsanszki/downwarddog#user-stories-and-epics)
- [Planning](https://github.com/Lilla-Kavecsanszki/downwarddog#planning)
- [Design](https://github.com/Lilla-Kavecsanszki/downwarddog#design)
  - [Wireframes](https://github.com/Lilla-Kavecsanszki/downwarddog#wireframes)
  - [Entity Relationship Diagrams](https://github.com/Lilla-Kavecsanszki/downwarddog#entity-relationshi-diagrams)
  - [Theme](https://github.com/Lilla-Kavecsanszki/downwarddog#theme)
- [Languages Used](https://github.com/Lilla-Kavecsanszki/downwarddog#languages-used)
- [Frameworks, Libraries, Programs & Technologies Used](https://github.com/Lilla-Kavecsanszki/downwarddog#frameworks-libraries-programs--technologies-used)
- [Features](https://github.com/Lilla-Kavecsanszki/downwarddog#features)
- [Deployment](https://github.com/Lilla-Kavecsanszki/downwarddog#deployment)
- [Testing](https://github.com/Lilla-Kavecsanszki/downwarddog#testing)
  - [Manual Testing](https://github.com/Lilla-Kavecsanszki/downwarddog#manual-testing)
  - [User Stories Testing](https://github.com/Lilla-Kavecsanszki/downwarddog#user-stories-testing)
  - [Further Testing](https://github.com/Lilla-Kavecsanszki/downwarddog#further-testing)
  - [Bugs](https://github.com/Lilla-Kavecsanszki/downwarddog#bugs)
- [Credits](https://github.com/Lilla-Kavecsanszki/downwarddog#credits)
  - [Content](https://github.com/Lilla-Kavecsanszki/downwarddog#content)
  - [Acknowledgments and Code](https://github.com/Lilla-Kavecsanszki/downwarddog#acknowledgments-and-code)
  - [Disclaimer](https://github.com/Lilla-Kavecsanszki/downwarddog#disclaimer)

# User Experience (UX)

### Ideal client

The ideal client for this business is:

-	English speaking
-	Practices yoga
-	A dog owner
-	Individuals, or couples or friends

Visitors of this website search for:

- A knowledgeable website that is easy to use
- That helps the user gain information about the topic of yoga, and practicing yoga with dogs
- That is reliable and accurate
- That encourage the visitors to create a communnity, through being able to communicate, comment and like articles
- That allows them to bring their dog to the yoga sessions
- That offers the visitors different choices on yoga classes to chose from
- That offers the visitors different dates and times when each classes are available
- That offers flexibility and so the user can delete a booked class in case they are no longer available

This website is the best way to help them achieve these goals because:

- The menu makes the access of different activities very easy to reach
- The content on the website is carefully curated and updated to ensure that the visitors receive reliable information
- The website offers interactive features as commenting, liking articles, encouraging the visitors to engage with the 
  contect and to create a community 
- The website offers dog-friendly yoga sessions, creating a unique yet inclusive experience for its visitors who would like to
  bring along their furry friends
- The website provides a wide range of yoga classes to chose from, allowing its visitors to choose based on their current 
  needs
- The website also displays multiple availabilities of each yoga class, allowing the visitors to choose the most convenient 
  one for their free time 
- The website offers flexibility in booking as it allows its visitors to delete a booked class, in case they are no 
  longer available, providing a hassle-free experience

This website:

- Is easy to navigate by the menu and buttons, offers an inclusive and engaging platform
- Gives the customers options and access to useful and learnable information.
- Gives the customers the information they need without overloading them or distracting them from their original ideas or
  wishes.
- Gives the customers the opportunity to connect with like-minded individuals
- Gives the the customers the opportunity to seamlessly manage their yoga sessions with their dogs

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

### User stories and Epics

##### Introduction and Navigation Epic

- #1  As a user, I can read the homepage so that I can get more information about the studio, the team, the approach to dogs 
      and yoga in general.
- #2  As a user, I can click on the navbar so that I go to the specific page I am interested in.

##### Account Management Epic

- #3  As a user, I can register to the website so that I have a higher level of permission and access.
- #4  As a user/admin, I can log in to the website so that I have the ability to book a class and/or comment on an article, 
      or like/unlike it.
- #5  As a user, I can see whether I logged in or registered so that I know that it was successful.
- #6  As a user, I can log out from the website so that I can protect my privacy and information.

##### Articles, Comments & Likes Epic

- #7  As a user, I can click on the article so that I can read the entire text about the topic and learn.
- #8  As a user, if I am logged in, I can like or unlike the articles so that I have the opportunity to show my interest 
      and appreciation.
- #9  As a user, if I am logged in, I can comment on the articles so that I can leave my feedback and/or thoughts 
      regarding the article.

##### Booking Epic

- #10 As a user, I can read more information about each classes so that I can choose which one suits me the best to book. 
- #11 As a user, if I am logged in, I can create a booking so that I can book and join a class.
- #12 As a user, I can choose the date of my future class so that I can book it on the date that suits my schedule.
- #13 As admin, I can authorize or disapprove booking enquiries so that I can assure that the classes are not overbooked.
- #14 As a user, if I am logged in, I can edit my booking so that I can change the number of dogs I would like to bring along
- #15 As a user, if I am logged in, I can cancel my spot, my booking, so that I can give my space back to others and I can 
    join the class when I am available.

##### Management Epic

- #16 As an admin, I can authorize or disapprove comments so that I can assure that a respectful language is used at all times.
- #17 As an admin I can create, read, update and delete articles so that I can manage the content.
- #18 As an admin I can see each booking; the day and class combination, to understand how many clients has enquired/ booked 
    it so that I can analyse popularity and busy/ weak days.

##### Contact Epic

- #20 As a user, I can fill out a contact form so that I can communicate with the management, give my feedback, leave a review to the teachers and the studio

##### Future ambition - Planned for the next sprint

- #21 create a share button to be able to share the articles
- #22 after successfully creating a booking, for the user to receive a confirmation text or email and/or reminder before the class also
- #23 users to be able to add the booking information to their calendar

(#19 US was deleted during production)

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Planning

The planning process started with determining the target clientele, by creating a Persona Profile - by using Code Institutes template - based on design thinking. Therefore the website aims to cater to the needs, expectations and preferences of the identified persona.
You can see the persona profile [HERE](README_docs/design_thinking_persona_template.pdf).

Given the prevalence of mobile usage among our target users, creating a responsive website was a top priority in our design approach. To achieve this, we leveraged the power of Bootstrap grids, elements, and responsive utilities combined with custom CSS, to ensure seamless adaptability across various devices.

#### Agile Methodology

In this project Github issues were used to create the User stories and groupped into Epics, in a Github Project. This served as the Agile tool. The issues' development was managed through a Kanban board. Currently, all the issues have been marked as "Done”.

For easy access, you can find the Epics, User Stories/ Issues, and Kanban board [HERE](https://github.com/users/Lilla-Kavecsanszki/projects/5).

# Design

### Wireframes

### Entity Relationship Diagrams

### Colour Scheme

- White
- Whitesmoke #f5f5f5
- Very dark (mostly black) cyan #141c1e
- Dark moderate lime green #48a04f
- Bright red #ed3833

![colour_palette](README_docs/images/colorkit.png "colour_palette")
[My Colour Palette](https://colorkit.co/palette/f5f5f5-f8d649-48a04f-44aedd-8f4ec4-ed3833-141c1e/)

I picked these specific colours based on the purpose of the website and what the studio wishes to achieve. I made that decision for a playful and fun aesthetics that can also give a calming effect to the visitors at the same time. 

### Typography

The primary font used for the website is Poiret One. It was chosen because I found this font to be

![Poiret One](README_docs/images/poiret_one.png "poiret_one")

The secondary font used for the body is Montserrat, which was selected for its clear readability, which works well with Poiret One to maintain the airy yet fun outcome.

![Montserrat](README_docs/images//montserrat.png "montserrat")

# Languages Use

- HTML5
- Python
- CSS3
- Javascript

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Frameworks, Libraries, Programs & Technologies Used

- [Lucid](https://lucid.app/documents#/documents?folder_id=recent) was used to create the ER Diagrams
- Github was used as the repository for the projects code after being pushed from Git
- Git was used for version control by the Gitpod terminal to commit to Git and Push to GitHub; to create and edit all
  original code
- [Google Fonts](https://fonts.google.com/) used for the Montserrat and Poiret One fonts
- [Font Awesome](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes
- [Fonticon](https://gauger.io/fonticon/) was used to create the favicon
- [Bootstrap](https://getbootstrap.com/) was used to build a responsive website quicker
- Microsoft Word was used to create the wireframes during the design process.
- [Django](https://www.djangoproject.com/) was used as the framework of the application
- [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku
- Django allauth used for account registration and authentication
- Django crispy forms used for form rendering
- Summernote used to to enable "WYSIWYG" (What You See Is What You Get) editing functionality to provide an intuitive and user-friendly interface
- [Cloudinary](https://cloudinary.com/) used to store the images and data used by the website
- [Heroku] was used to deploy the application and provides an enviroment in which the code can execute

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Features

## Home Page

### F01 Navigation Bar

The navigation bar provides easy access to all active pages for the user.

**Menu Options:**

- **Logo:** Essentially it indicates the name of the website, while it also serves as a button that is linked to the homepage as an instant solution for the user. The logo also includes a "jumping" paw icon in the website's signature orange colour, adding an eye-catching and playful effect that draws the user's attention to the business name
- **Home:** This button serves as a quick link to the homepage, enabling users to navigate back to the main landing page at any point.
- **Articles:** Users can explore and read articles by clicking on this button, which further leads them to a detailed page showcasing various content if they want to. The logged-in user will also be able to comment the articles or like them. The non-logged-in user can only view.
- **Yoga:** The "Yoga" button takes users to a list of available classes. Each class is presented with relevant information and a button, 'Availabilities', which through the Users can choose their preferred date and time, and go ahead to book their desired class. At the end, only logged-in user can proceed with a booking, non-logged in users will be redirected to the Login page.

##### Logged-In Users

For logged-in users, the navigation bar includes two additional menu options:

- **My Bookings:** This button provides quick access to view and manage the user's booked classes.
- **Logout:** Users can log out by clicking on this option.
  
![Navbar Logged_In](README_docs/images/navbar_loggedin.png "navbar_logged_in")

##### Not Logged-In Visitors

For non-logged-in users, the following options are available instead:

- **Register:** Users can register and create an account to gain access to more features and personalized content.
- **Login:** Clicking on this button allows users to log in with their credentials and access personalized content and more features.
  
![Navbar Not Logged_In](README_docs/images/navbar_nonloggedin.png "navbar_not_logged_in")

##### Special Case for Administrators

For the administrator or superuser who is logged in, an extra menu option is displayed:

- **Admin:** This button offers a direct link to the main site administration page, eliminating the need to manually append '/admin' to the homepage URL.
  
![Navbar Admin](README_docs/images/navbar_admin.png "navbar_admin")

##### Decorative Element

On the right-hand side of the navigation bar, a muted text adds a touch of decoration. If a user is logged in, their username, along side by a user icon, is displayed. Otherwise, the text "Breathe.. or bark?" is shown, adding a playful and welcoming touch to the user interface.

The navigation bar is fully responsive, adjusting to different screen sizes, and it collapses on mobile screens, displaying a hamburger icon for easy navigation.

![Navbar Hamburger](README_docs/images/navbar_hamburger.png "navbar_hamburger")

![Navbar Hamburger Open](README_docs/images/navbar_hamburger_open.png "navbar_hamburger_open")

### F02 Hero Image and Overlay Text

Underneath the navbar, the Home page features a very relevant photo of a woman doing yoga with a dog next to her. There is also a text overlay on top of the image, displaying the name of the website and the business, and also gives a clear idea of its purpose too.

![Hero Image and Text](README_docs/images/hero_feature.png "hero_image&text")

### F03 Encouragement Text and Get started button

Underneath the hero image, there is a larger text displayed, that encouraging the user to discover the available classes and with the button below it, instantly leads to the goal of the website, which is to get the user to book a class/ classes. The button therefore directs the user to the Yoga page, that lists the classes that can be booked.

![Encouragement Text and Button](README_docs/images/goal.png "encouragement_text&button")

### F04 Encouragement Text and Get started button

Below F03 the user can see a section that includes 2 parts, where the website offers an introduction to the business namely its Story and its Team. On the opposite side of the texts, a stylized image of a stretching pug is displayed as a decorative element, visually capturing the essence and ambiance of the business.

![Introduction](README_docs/images/introduction.png "Introduction")

### F05 Contact section

F05 includes a section through that the user can find the business and/or reach out. The title on top makes this purpose very clear, then underneath of that the address is shown. On the opposite side, a contact form is provided. The user is required to fill in their name, email, and message before they can submit the form using the 'Send Message' button. The button is disabled until all required fields are correctly filled out. Additionally, the email field validates the input to ensure it includes an '@' sign before submission. 
When the contact form is filled out as required and submitted, the user will see a reassuring message popping up in green, letting them know that their message was successfully sent, then will also disappear in 2 seconds.
In case of an error, and so failure of sending the message, a red message pops up informing the user that the submition failed and prompts them to try again.

![Contact](README_docs/images/contact.png "contact")

### F06 Footer 

Just as the navigation bar, the footer is also presented on each page. It is at the very bottom, displaying information about the website creator, along with convenient links to the developer's Github and LinnkedIn profils. It also shows a disclaimer, clarifying that the website was created for educational use only. 

![Footer](README_docs/images/footer.png "footer")

## Articles page

### F07 List of the articles

On this page, users can browse through four articles per page, each displaying their titles, relevant images, author names, publication dates, and the number of likes they have received. 
Pagination allows users to navigate to the next set of four articles using the "Next" button located below the last article. 

![Pagination Button](README_docs/images/pagination_button.png "pagination_button")

![Articles List](README_docs/images/articles_list.png "articles_list")

### F08 Articles Detail page

By clicking on the article titles, users are brought onto the Articles Detail page to read the full content and view likes, and any associated and approved comments.

![Article](README_docs/images/article.png "article")

![Like & Comment](README_docs/images/like&comment.png "like&comment")

Logged-in users have additional privileges, as they can like and comment on the articles as well. This enhanced functionality enriches the overall user experience and encourages engagement with the content and other users in the community. 
Likes are explained in F09, and Comments in F10 in more detail.

### F09 Like an article

In order for a user to like an article, they must first log in to their account. Once logged in, they can proceed to view the article's full content on the Articles Detail page and there simply click on the heart icon displayed beneath the article's content.
If the user changes their mind, they can click on the heart icon again to unlike the article. 
When the article is liked by the current user, the heart icon appears filled with the website's distinctive orange color. Additionally, a like counter is displayed next to the heart icon, indicating the number of likes the article has received from all the users.

![Likes](README_docs/images/likes.png "likes")

### F10 Comment on an article

In order for a user to comment on an article, they again must first log in to their account. Once logged in, they can proceed to view the article's full content on the Articles Detail page and there scroll to the bottom. There, next to the existing Comments section, there is a form to leave their own comment. A clear message prompts the user to leave a comment and where it should be filled in. The username also appears above the form, showing who the comment will come from. The user needs to type in their comment into the text box then press the submit button. All comments then must be approved by the administrator before they will be visible on the Articles Detail page. Once approved, the comments will appear in the comments section at the bottom of the Articles Detail page, starting with the latest one.

For the admin to approve a comment, they need to log in to the admin pages. There they need to click onto the Comments table, tick and select the comment or comments that they wish to authorise, choose the 'Approve Comments' button from the drop-down menu and finally click on 'Go'.
The second way to achieve the same is to click on the individual comment (on the name row) and there select 'Approved' box then finally press save.

There is also a comment counter, next to the like counter, that tracks the number of comments were approved for the specific article.

![Comment](README_docs/images/comment.png "comment")

![Comment Approve](README_docs/images/comment_approve.png "comment_approve")

![Individual Approve](README_docs/images/individual_approve.png "individual_approve")

## Yoga page

### F11 Video background and Overlay Text

The top of the Yoga page features a muted video of a girl doing yoga with a dog next to her. The video serves as a motivation for users to start moving as soon as they see it. To blend the video into its environment, there is a faded black overlay on top of it. Additionally, there is a text overlay suggesting the purpose of the page, and a "jumping" arrow urges the user to scroll down to explore the different yoga classes available to choose from.

![Video & Overlay](README_docs/images/video%overlay.png "video&overlay")

### F12 Yoga Class Cards

Underneath the video, users can view the different yoga classes and relevant information about them, presented on orange cards. Each class has an 'Availabilities' button that takes the user to the Yoga Detail page of the chosen class. The Yoga Detail page is also detailed under F13.

![Yoga Classes](README_docs/images/yoga_classes.png "yoga_classes")

### F13 Yoga Detail Cards

The Yoga Detail cards are displayed on the Yoga Detail page, which looks exactly the same as the Yoga page. The difference is the content of the orange cards, that this time are the yoga detail cards.
The cards show the available dates and times of the chosen class. Underneath that information on each card there is a dropdown menu, where the user can select how many dog or dogs they wish to bring to the chosen class. The default is set to 1. After the user choses this detail and if they are logged in, they can proceed and book through the cards' own 'Book Now' button. If the user is not logged in, then the button will redirect them to the Sign in page. The Book Now button is explained further in details in F15.

![Yoga Detail](README_docs/images/yoga_detail.png "yoga_detail")

### F14 Warning Text

Above the yoga detail cards on the yoga detail page, a polite warning message is displayed, explaining that users need to be logged in to book a class.

![Warning Text](README_docs/images/warning.png "warning")

### F15 Book Now

As mentioned in F13, the "Book Now" button redirects users to the Sign-in page if they are not logged in. However, for logged-in users, it handles the creation of a booking.

![Book](README_docs/images/book.png "book")

When the logged-in user press the "Book Now" button, it takes them to the My Bookings page, displaying the relevant titles and paragraphs from that, which is in this case a pending status.

![Pending Booking](README_docs/images/pending.png "pending")

If a logged-in user attempts to press the "Book Now" button twice for the same class, date and time, the constraints in the Booking model prevent that. The user will be redirected to the "My Bookings" page, where they will see a message explaining that they have already attempted to book this class and should wait for approval.

![Already Booked](README_docs/images/already_booked.png "already_booked")

## F16 My Bookings page

Logged-in users enjoy an additional option on their navbar: the "My Bookings" page. This page conveniently lists all approved bookings for the user, including the class title, username, date and time, and the number of dogs that it was booked with.
Underneath there is also a friendly and welcoming message says: See you soon! 
Under each booking in the list, users will find two buttons and a dropdown menu. The "Delete" button, detailed later in F17, allows users to cancel their bookings. On the other hand, the "Update" button, along with the dropdown menu (F18), serves to modify booking details as needed.
Additionally, a disclaimer appears at the bottom of the page, informing users that all bookings are subject to admin approval.

![Approved Booking](README_docs/images/approved_bookings.png "approved_booking")

In case the user has no (approved) bookings yet, the "My Bookings" page will display a special message indicating that the user currently has no bookings. This message serves as a notification that the user has not yet made any bookings, encouraging them to explore available classes and make their first booking.

![No Booking](README_docs/images/no_booking_yet.png "no_booking")

## F17 Delete button

Logged-in users 

![Approved Booking](README_docs/images/approved_bookings.png "approved_booking")

## F18 Update button and Dropdown

Logged-in users 

![Approved Booking](README_docs/images/approved_bookings.png "approved_booking")

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Deployment

**How to Clone**



<details><summary>Steps</summary><br/>

1. Go to the <https://github.com/Lilla-Kavecsanszki/order-easy> repository
2. Click the Code button to the left of the green Gitpod button, then choose Local.
3. Click on headings for HTTPS, SSH, and Github CLI to find their individual URL links. Choose the HTTPs one.
4. Open your own terminal in your editor and change the current working directory to the location of where you want the
   cloned directory to be.
5. In the terminal type git clone, and then paste the URL you copied from the repository page.
6. Press enter to complete.

</details>
<br

**How to Fork**
<p>
<details><summary>Steps</summary><br/>

1. Go to the <https://github.com/Lilla-Kavecsanszki/order-easy> repository
2. Click the fork button in the top right of the screen, between the watch, and the star buttons.

</details>
<br>

**Deployment to Heroku**
<p>
<details><summary>Steps</summary><br/>

The OrderEasy website is deployed using Heroku, this was done by:

1. Add dependencies in GitPod to requirements.txt file with command "pip3 freeze > requirements.txt"
2. Commit and push to GitHub
3. Go to the Heroku Dashboard
4. Click "Create new app"
5. Name app and select location
6. Choose the Settings tab and add Config Vars for Creds and Port (creds.json file)
   (as a second entry also add PORT for the key and 8000 for the value)
7. Add the buildbacks to Python and NodeJS in that order
8. Now go to Deploy tab
9. Select GitHub as deployment method
10. Connect to GitHub and link to repository
11. Enable automatic deployment or deploy manually
12. Click on Deploy

</details>
<br>

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Testing

<p>
<details><summary>Python Validator result on the run.py file</summary><br/>
<img src="readme-images/python_validator.png" alt="Python Validator">
</details>

### Manual Testing

<p>
<details><summary>Details</summary><br/>

**Menu:** Load or run the program to confirm that the menu is displayed correctly and responds as expected. The menu is also displayed after the completion of each option (1-4). The program terminates when the user chooses option 5 to exit. Enter any option 1 again to confirm that the Products List is updated accordingly.

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)
</details>

### User Stories Testing

<p>
<details><summary>Details</summary><br/>

1.	As a user of 

   ![Menu](readme-images/app.png "Menu")


[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)
</details>

### Further testing

<p>
<details><summary>Details</summary><br/>
I asked friends and family to look at the application on their browsers and report any issues they find. This time my focus was on UX and how understandable and easy the application is to use. Some print and ValueError messages were adjusted as a result of this.
</details>

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

## Bugs

An issue came up while testing the application in the meantime;

- The 'Delete Product' function got into some issues when attempting to delete an existing product due to case sensitivity. Specifically, the function was unable to locate a product if it was inputted in lowercase or capitalized incorrectly. To address this issue, I utilized the capitalize() method in both the get_new_product() and get_deleted_product() functions. This modification ensures that the user inputs are formatted to start with a capital letter, regardless of their original input. As a result, the application can accurately locate and delete the requested products.

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Credits

## Content 

I have based the model on functions used to request, validate, and return data to and from the user. These functions are called from within the 'Menu' function, which offers options to the user to decide on the order in which they want to execute them.

![Data Model](readme-images/data_model.png "Data Model")

The first option allows the user to view a list of products, which is retrieved from the "Stocks Sheet" in an external Google Sheet. The second option allows the user to add a new product to the "Stocks Sheet" by entering data that is validated and uploaded to the Google Sheet. The third option allows the user to delete a product from the "Stocks Sheet" by entering data that is validated and used to find and remove the product from the Google Sheet. The fourth option allows the user to retrieve an order list by entering data that is validated and used to calculate amounts, which are also uploaded to the "Stocks Spreadsheet" in the Google Sheet and printed back to the user in a table format. The fifth option allows the user to exit the program.

The External Google Sheet is used to store and manage the data for this system, including the "Stocks Sheet" with product names, units, prices, par levels, current stock holding values and calculated amounts. The user can also use this sheet to update the prices and par levels to keep their business in financial control.
Data is formatted using the Tabulate() method for better user experience.

The Google spreadsheet (order_spreadsheet) that the application uses has the following fictitious initial data, which was set up manually by the author:

[See it live here](https://docs.google.com/spreadsheets/d/1N0ECIjFPmC-p_JI4heZHAFZnKkr4nlBe8KIJzD_k5DU/edit#gid=597566188)

<p>
<details><summary>Stocks Sheet</summary><br/>
<img src="readme-images/updated_spreadsheet_option3.png" alt="Stocks sheet">
</details>
<br>

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

## Acknowledgments and Code

I received inspiration for this project from my personal experience working in the hospitality industry, as well as from my partner's struggles with similar issues at his job. These experiences helped me figure the logic for this project greatly. In addition, I reviewed the work of other students to gain a better understanding of project scope and to identify best practices for Milestone Project 3.

The below websites have been used to understand the logic of building this project with Python.



I also would like to express my gratitude to Elaine Roche, my mentor, and the tutoring team for their continuous support and valuable feedback. Their guidance, tips, and resources have been instrumental in my coding and testing skills.

## Disclaimer

This application is for educational use only.

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

Article Sources:

https://www.health.harvard.edu/staying-healthy/yoga-benefits-beyond-the-mat

https://www.theguardian.com/lifeandstyle/2023/jun/14/desk-yoga-de-stress-office-india-y-break

https://www.yogabasics.com/explore/yogic-lifestyle/yogic-diet/yogic-diet-guide/

https://www.yogajournal.com/lifestyle/yoga-trends/practice-yoga-dog/

https://www.shutterstock.com/video/editorial/search/puppy-yoga

Inspiration:

<<https://triyoga.co.uk/>

https://en.wikipedia.org/wiki/Doga_(yoga)

https://getbootstrap.com/docs/5.0/forms/select/

https://docs.djangoproject.com/en/4.2/

<https://getbootstrap.com/docs/5.0/getting-started/introduction/>

<https://stackoverflow.com/questions/34586259/how-to-organize-js-files-in-django>

<https://stackoverflow.com/questions/61020923/displaying-videos-in-django-template-media-link>

https://stackoverflow.com/questions/56969479/adding-video-field-in-django

https://docs.djangoproject.com/en/2.2/topics/http/file-uploads/

<https://pythonguides.com/if-statement-in-django-template/>

<https://stackoverflow.com/questions/65880813/passing-id-to-django-url>

https://stackoverflow.com/questions/46860710/django-linking-a-html-page-to-a-view

https://stackoverflow.com/questions/42628883/object-id-in-dja

<https://stackoverflow.com/questions/26334133/passing-an-id-to-a-url-link-django>

https://stackoverflow.com/questions/25345392/how-to-add-url-parameters-to-django-template-url-tag

<https://stackoverflow.com/questions/44437706/django-render-redirect-to-page-with->

<https://stackoverflow.com/questions/11293380/django-catching-integrity-error-and-showing-a-customized-message-using-template>

<https://docs.djangoproject.com/en/3.2/ref/models/querysets/>


Message alert and Reloading the page

https://stackoverflow.com/questions/30050678/show-bootstrap-alert-box-on-a-button-click

https://stackoverflow.com/questions/16955019/how-to-reload-a-page-after-the-ok-click-on-the-alert-page

https://www.w3schools.com/howto/howto_js_alert.asp

https://stackoverflow.com/questions/32394684/how-to-confirm-and-call-function-with-onclick

Rename the body field in the Comment form

https://docs.djangoproject.com/en/4.2/topics/forms/

https://stackoverflow.com/questions/73686042/how-do-i-label-fields-on-a-django-form

Dropdown HTML

https://www.freecodecamp.org/news/html-drop-down-menu-how-to-add-a-drop-down-list-with-the-select-element/

https://stackoverflow.com/questions/26450696/get-user-id-with-request-post-get-works-but-value-seems-to-be-no-integer

Bugs:
- EmailJS... was not connected properly, didnt copy the correct template parameters
- slug not working for the Booking view-url, needed to the ID parameter - based on error code suggestion in Debug=True mode