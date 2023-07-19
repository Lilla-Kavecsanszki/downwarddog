# DownwardDog Yoga Studio

This website is designed to bring together all yoga fans who are also dog owners, creating a safe place for them to practise yoga together and the opportunity for a vibrant community. 
The main focus is to be straight forward enough to save time for the user, yet to be engaging and motivating at the same time.

The user can interact with the website in various ways such as viewing relevant and uselful information on the articles page. The users, if they are registered and logged in, then can comment on the articles and also can express their opinion with a like. They can later also unlike the article, in case they changed their mind. 
The users can also see a selection of yoga classes, then also a selection of available dates and times for the relevant classes to choose from through the Yoga page. If they are logged in, they will be able to book, register their interest. After admin approval, the user is able to follow up their bookings on the My Bookings page, and also to delete the bookings that they are not able to attend anymore.  

This full-stack framework project was built using Django framework, Python, HTML, Bootstrap and CSS. Furthermore, the webiste stores all vital information and data in an external database, Cloudinary.

![Application](readme-images/responsive.png "Application")

[Link to the live project](https://downwarddog.herokuapp.com/)

# Contents

- [User Experience (UX)](https://github.com/Lilla-Kavecsanszki/downwarddog#user-experience-ux)
- [Ideal client](https://github.com/Lilla-Kavecsanszki/downwarddog#ideal-client)
- [User stories](https://github.com/Lilla-Kavecsanszki/downwarddog#user-stories)
- [Flow Charts](https://github.com/Lilla-Kavecsanszki/downwarddog#flow-charts)
- [Design](https://github.com/Lilla-Kavecsanszki/downwarddog#design)
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
  - [Content - Data Model](https://github.com/Lilla-Kavecsanszki/downwarddog#content---data-model)
  - [Acknowledgments and Code](https://github.com/Lilla-Kavecsanszki/downwarddog#acknowledgments-and-code)
  - [Disclaimer](https://github.com/Lilla-Kavecsanszki/downwarddog#disclaimer)

# User Experience (UX)

### Ideal client

The ideal client for this business is:

-	English speaking
-	Practices yoga
-	A dog owner
-	Individuals, or couples

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
- The 
- The 
- The 

This website:

- Is easy to navigate by the menu and buttons
- Gives the customers options and access to useful and learnable information.
- Gives the customers the information they need without overloading them or distracting them from their original ideas or
  wishes.
- Guides them by their curiosity about the goal of the website.
- Easy to use, due to redirecting links, that warn the user if they are about to book the same class again or redirecting them to the Sign In page, in case they are not signed in but wanted to book a class.
- Easy to follow up, delete their bookings after signing in, from the My Bookings page, where all their bookings are organised

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

### User stories

1.	As a user of 


[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Flow Charts

<p>
<details><summary>Home page - Menu</summary><br/>
<img src="readme-images/flowchart-menu.jpg" alt="menu flow chart">
</details>

<p>
<details><summary>Option1 - Print Product List</summary><br/>
<img src="readme-images/option1-flow.jpg" alt="Print Product List flow chart">
</details>

<p>
<details><summary>Option2 - Add New Product</summary><br/>
<img src="readme-images/option2-flow.jpg" alt="Add New Product flow chart">
</details>

<p>
<details><summary>Option3 - Delete Product</summary><br/>
<img src="readme-images/option3-flow.jpg" alt="Delete Product flow chart">
</details>

<p>
<details><summary>Option4 - Get the Order List</summary><br/>
<img src="readme-images/option4-flow.jpg" alt="Get the Order List flow chart">
</details>

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Design

![colour_palette](README_images/colorkit.png "colour_palette")
[Colour Palette](https://colorkit.co/palette/ffff-f2eae3-c36d4e-322925/)

Fonts

![colour_palette](README_images/poiret_one.png "colour_palette")
![colour_palette](README_images/montserrat.png "colour_palette")


# Languages Used

Python was used to complete this project.

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Frameworks, Libraries, Programs & Technologies Used

- [Miro](https://miro.com/) was used to create the flow charts
- Github was used as the repository for the projects code after being pushed from Git
- Git was used for version control by the Gitpod terminal to commit to Git and Push to GitHub; to create and edit all
  original code
- Google Spreadsheets was used as the external data store for stock data used by the project
- Google Drive API was used to generate credentials used in the project to securely access the Google Spreadsheet
- Google Sheets API was used to support interactions (e.g. read/write functionality) between the code and data stored in
  the Google Spreadsheet
- gspread is the Python API for Google Sheets
- Google Auth is the Google authentication library for Python required to use the credentials generated for Google Drive
  API
- datetime is a standard library in Python that provides classes for working with dates and times
- tabulate is a library in Python that provides a way to display data in a visually appealing way, allowing to create
  tables from data
- Heroku was used to deploy the application and provides an enviroment in which the code can execute

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Features

#### Home - The Menu

The menu is displayed when the application starts to keep the interface simple to use and uncluttered. The menu features five options, functionalities for the user to choose from; 1) Print Product List, 2) Add New Product, 3) Delete Product, 4) Get the Order List and 5) Exit.

![f_menu](readme-images/f_menu.png "f_menu")

The user is prompted to choose one of the menu options by entering the option number. In the event of an invalid input, an error message will be displayed and the main menu will be displayed again.

![invalid input menu](readme-images/invalid_menu_input.png "invalid input menu")

The menu will continue to be displayed repeatedly until the user inputs a valid response and after the completion of each options (1-4). The application will be terminated only when the user selects option 5 from the menu.

#### Option 1 - Print Product List

If the user selects option 1 from the menu they are shown the list of the products that are currently on the stocks sheet in the Google Spreadsheet.

This is data taken from the Google Spreadsheet, all information listed under each other from its first column.

![Option1](readme-images/print_product_list.png "Option1")

Products added or deleted while using the application will be reflected on the list when the 'Print Product List' option is subsequently run.

![Updated spreadsheet](readme-images/updated_option_1.png "Updated spreadsheet")

#### Option 2 - Add New Product

The user can add a new product by choosing option 2 from the menu. The application displays a message on screen listing the input requirements and also an example input string of values for better understanding.

![Option2](readme-images/add_new_product.png "Option2")

In the event that the user inputs do not satisfy the validation criteria, they will be prompted to re-enter the required information. The explanation of the data needed is displayed again too.

The rules for the input values:

- Inputs are separated by commas
- 4 values are required
- The fourth value, the par level, needs to be an integer so that the program can use it for calculations later on

![Invalid input for option2](readme-images/invalid_option2_input.png "Invalid input for option2")

![Invalid literal input for option2](readme-images/integer_error_option2_input.png "Invalid literal input for option2")

When the user inputs valid data the application displays multiple messages to assure the user with information on how the data is being processed and a new row is added to the stocks spreadsheet for the new product. Once the operation is complete it returns to the menu.

![Valid input for option2](readme-images/valid_input_option2.png "Valid input for option2")

The updated Google Spreadsheet:

![Updated Spreadsheet for option2](readme-images/updated_spreadsheet_option2.png "Updated Spreadsheet for option2")

#### Option 3 - Delete Product

The user can remove, delete an already existing product by choosing option 3 from the menu. The application displays a message on screen explaining the input requirement and also an example input string of value for better understanding.

![Option3](readme-images/delete_product.png "Option3")

In the event that the user inputs do not satisfy the validation criteria, they will be prompted to re-enter the required information. The explanation of the data needed is displayed again too.

The rules for the input values:

- At least 1 string of input is required, not a whitespace
- The product name cannot be left empty

![Invalid input for option3](readme-images/invalid_option3_input.png "Invalid input for option3")

When the user inputs valid data the application displays multiple messages to assure the user with information on how the data is being processed. There are two ways where the operation can go; if the program finds a match with the input on the stocks spreadsheet, another message will be displayed and the first found (matched) item, with its entire row relevantly gets deleted from the stocks spreadsheet for the mentioned product. Always only the first match, in case the user needs the other copy to stay in stocks. Once the operation is complete it returns to the menu.

![Valid input for option3](readme-images/valid_input_option3.png "Valid input for option3")

The updated Google Spreadsheet:

![Updated Spreadsheet for option3](readme-images/updated_spreadsheet_option3.png "Updated Spreadsheet for option3")

When the program doesn't find a match with the input on the stocks spreadsheet, again a message will be dispayed; explaining that the mentioned product is currently not on stock. The product therefore cannot be deleted as does not exist and the program will take the user back to the menu so they can carry on with their work accordingly.

![Product is not found option3](readme-images/product_is_not_on_stock_option3.png "Product is not found option3")

#### Option 4 - Get the Order List

The main function of the program is when the user can gather relevant information on how much they need to order of their products on stock. They can do this by choosing option 4 from the menu. The application displays a message on screen prompting the user for the first action that they need to do and listing the input requirements, while also providing an example input string of values for better understanding. The program will always ask for the number of data that reflects the current product list on the stocks sheet. This number is calculated by the app by counting the length of the first column with values on the stock sheet and then subtracting 1 from it, in order to take the heading row into consideration.
Therefore this number gets updated each time a new product was added or an existing one was deleted beforehand.

![Option4](readme-images/get_the_order_list.png "Option4")

In the event that the user inputs do not satisfy the validation criteria, they will be prompted to re-enter the required information. The explanation of the data needed is displayed again too.

The rules for the input values:

- Inputs are separated by commas
- 'x' values are required, as many values as the program currently requires
- The input values need to be integers or floats so that they reflect stock take method standards and also the program can use them for calculations later on

![Invalid input for option4 by the amount of values](readme-images/invalid_input_option4_bythenumber.png "Invalid input for option4 by the amount of values")

![Invalid input for option4 by their type](readme-images/invalid_input_option4_bythetype.png "Invalid input for option4 by their type")

When the user inputs valid data the application displays multiple messages to assure the user with information on how the data is being processed. First the program updates the stocks sheet with the user inputs and also adds the current date to the heading of the Current Stock Holding column (5th col) so the user can reference it. After that, the application calculates how much the user needs to order of each products. The application calculates this by taking the par level values from the 4th column and from those it subtracts the previously input current stock holding values, 5th column. The results then are uploaded in the stocks spreadsheet, in the 6th column named, How much to order.

![Valid input for option4](readme-images/valid_input_option4.png "Valid input for option4")

The updated Google Spreadsheet:

![Updated Spreadsheet for option4](readme-images/updated_spreadsheet_option4.png "Updated Spreadsheet for option4")

After performing the necessary calculations and updating the stocks sheet with all the required data, the program presents the information to the user in a table format. This makes it easy and quick for the user to read and gather all the necessary information for placing a new order.
Once the operation is complete it returns to the menu.

![Order information](readme-images/order_information.png "Order information")

#### Option 5 - Exit

The user can exit and terminate the application by choosing option 5 from the menu. As a final touch, the program displays a Goodbye message to the user.

![exit](readme-images/exit.png "exit")

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)

# Deployment

**How to Clone**
<p>
<details><summary>Steps</summary><br/>

1. Go to the <https://github.com/Lilla-Kavecsanszki/order-easy> repository
2. Click the Code button to the left of the green Gitpod button, then choose Local.
3. Click on headings for HTTPS, SSH, and Github CLI to find their individual URL links. Choose the HTTPs one.
4. Open your own terminal in your editor and change the current working directory to the location of where you want the
   cloned directory to be.
5. In the terminal type git clone, and then paste the URL you copied from the repository page.
6. Press enter to complete.

</details>
<br>

**How to create and configure the Google spreadsheet and APIs**
<p>
<details><summary>Steps</summary><br/>

1. Log in (or create) to your Google account
2. Create a Google Spreadsheet (order_spreadsheet) on Google Drive. Mine has 1 page; 'stocks'.
3. In row 1 of the stocks sheet, create the headings: Products, Unit, Price, Par level, Current Stock Holding, How much to
   order
4. Then go ahead and fill out the sheet as needed. For the initial sample data used in this project click [here](https://github.com/Lilla-Kavecsanszki/order-easy#content---data-model)
5. Set up APIs on the [Google Cloud Platform](https://console.cloud.google.com/welcome?project=ordereasy-378810)
6. Create a new project, so click on the “Select a project” button and then select “new project”. and
7. Give it a unique name, then by clicking on “Select Project” again, go to dashboard
8. Setup Google Drive credentials
9. From the side menu (hamburger menu on the top) select "APIs and Services" and then "Library"
10. Search for Google Drive API
11. Select Google Drive API and click on the 'enable' button, which will take you to the API overview page.
12. Click the “Create credentials” button, then there is a form the fill out.
13. From the "Which API are you using?" dropdown menu, choose Google Drive API
14. For the "What data will you be accessing?" question, select Application Data
15. For the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?"     question, select No, I'm not using them
16. Click Next
17. Enter a Service Account name, then click Create
18. In the Role Dropdown box choose Basic > Editor then press Continue
19. You got taken to the next page, where those options can be left blank, click Done
20. On the next page, click on the Service Account that has been created
21. On the next page, click on the Keys tab
22. Click on the Add Key dropdown and select Create New Key
23. Select JSON and then click Create, which will trigger your credentials file to be downloaded  
    into our computer files
24. You also need to enable your Google Sheets API. So go back to the library again, and search for “google sheets”.  
25. Select the Google Sheets API, then click “enable” (there's no need for more credentials here)
Now you have your APIs enabled, and have your credentials file downloaded.  
26. Add your credentials file that you downloaded in step 23; so locate the json file wherever it is within your computer
    files and simply drag and drop it into your Gitpod workspace.
27. Rename it to "creds.json" to make it easier to use
28. Open up the json file and find the client_email value here, copy this email address generated for your credentials.
    Copy it without the quotes around it.
29. Go back to your spreadsheet and click the share button here
30. Paste in the client email, make sure “Editor” is selected, untick “Notify People”, and then click "share"
31. Make sure that gitignore file contains your creds.json file, then save and commit
32. Install gspread and google-auth libraries in the development environment using the
    command 'pip3 install gspread google-auth'

</details>
<br>

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

**Menu:** Load or run the program to confirm that the menu is displayed correctly and responds as expected. The menu is also displayed after the completion of each option (1-4). The program terminates when the user chooses option 5 to exit. Enter any number other than 1-5 or a word to confirm that an error message is displayed explaining that it is a wrong input, reminding the user of the requirements, and displaying the menu again to prompt for another input.

**Option 1 - Print Product List:** Enter the number 1 and press enter to confirm that a reassuring message is displayed, followed by the list of current products. Use option 2 to add a new product or option 3 to delete a product, and then choose option 1 again to confirm that the Products List is updated accordingly.

**Option 2 - Add New Product:** Enter the number 2 and press enter to confirm that a message is displayed explaining what the user needs to do next, including the required user input and an example.
**Validation:** Enter more or less than the 4 required details to confirm that an error message is displayed explaining that the input data is invalid, and reminding the user of the requirements and the number of details entered. Enter 4 details with the fourth detail not being a number to confirm that an error message is displayed explaining that the input data is invalid, and also printing out the last detail that was entered, along with the requirement that it needs to be an integer.
**Functionailty:** Enter valid values to confirm that the application displays multiple messages to reassure the user that their request is being processed. After completion, open the Google Sheet to confirm that the new product is uploaded after the previously last row. I also confirm that the product name starts with a capital letter, regardless of whether the input started with a capital letter or not.

**Option 3 - Delete Product:** Enter the number 3 and press enter to confirm that a message is displayed explaining what the user needs to do next, including the required user input and an example.
**Validation:** Press enter or input one or more spaces to confirm that an error message is displayed explaining that the input data is invalid, reminding the user of the requirements, and notifying the user that the product name cannot be empty.
**Functionailty:** Enter valid values, but a product name that is not currently on the stock list to confirm that the application displays multiple messages to reassure the user that their request is being processed and in the last message it says that the product is not currently on stock. I confirm that in this case nothing gets deleted from the Google Sheet.
Enter valid values, with an existing product name, to confirm that the application displays multiple messages to reassure the user that their request is being processed. After completion, open the Google Sheet to confirm that the mentioned product is deleted from the list. I also confirm that the function finds the mentioned product regardless of whether the input started with a capital letter or not.
Use option 2 to add a new product and add the same product twice. Then, choose option 3 to delete the same product and confirm that only the first match will be deleted. View this result in Google Sheet.

**Option 4 - Get the Order List:** Enter the number 4 then hit enter to confirm that a message is displayed explaining what the user needs to do next, including the required user input and an example.
**Validation:** Enter more or less than the required amount of details to confirm that an error message is displayed explaining that the input data is invalid, and reminding the user of the requirements and the number of details entered. Enter the correct amount of details with one detail not being a number to confirm that an error message is displayed explaining that the input data is invalid, and also printing out the invalid detail that was entered, along with the requirement that it needs to be a float or an integer.
**Functionailty:** Enter valid values to confirm that the application displays multiple messages to reassure the user that their request is being processed. In the end, a table is printed, that presents all data from the Stocks Sheet in an easily readable format. After completion, open the Google Sheet to confirm that the 'Current Stock Holding' column is uploaded and today's date is also displayed in the heading. Also confirm that the 'How much to order' column is uploaded too and all calculations are correct.
Use option 2 to add a new product or option 3 to delete a product, and then choose option 4 again to confirm that the data and therefore the validation requirements are updated accordingly, and the programs runs smoothly with no issues.

**Option 5 - Exit:** Enter the number 5 and press enter to confirm that the goodbye message is displayed, and the application terminates.

[Back to top](https://github.com/Lilla-Kavecsanszki/downwarddog#contents)
</details>

### User Stories Testing

<p>
<details><summary>Details</summary><br/>

1.	As a user of the application, I want to easily navigate the app, so I can find what I need quickly.

    - After the application loeaded, the first 'page' that the user can see is the Menu. The menu breaks down the functionalities into 5 main actions or options to select. The menu will continue to be displayed repeatedly after the completion of each options (1-4). The application will only be terminated when the user selects option 5 from the menu and exits. Therefore, the opportunity to easily select from the menu again is always available to the user after they finish a task.

2.	As a potential new user to the application, I want to understand what my options are

    - The menu is the first interaction with the user and pops up again after each task completion.

   ![Menu](readme-images/app.png "Menu")

3. As a user of the application, I want to be able to retrieve the list of products that I have on stocks to make the
    stock count, and therefore the later input faster, more efficient.

    - The first option, Print Product List, in the menu helps the user just with that. It gathers all product names that are currently on the stock list and presents them under each other. In case there were products added or deleted from the stock while using the application, those will be reflected on the list when the 'Print Product List' option is subsequently run again.

    ![List of Products](readme-images/print_product_list.png "List of Products")

    - After a new product was added.

    ![Updated Product List](readme-images/updated_option_1.png "Updated Product List")

4. As a user of the application, I want to be able to add a new product to the stock list, in case my business needs a
    new, different product with time.

    -	The second option, Add New Product, in the menu helps the user just with that. First, the program displays its requirements, and what details it needs from the user to input to be able to upload the new product to the Google sheet and add it to the stock list. When the user inputs the correct, valid data, the program will display some messages to reassure the user that their request is being processed and completed.

    ![Updated Stocks sheet - new product](readme-images/updated_spreadsheet_option2.png "Updated Stocks sheet - new product")

5. As a user of the application, I want to be able to remove, delete an existing product from the stock list, in case my
    business doesn't need that specific product anymore.

    - The third option, Delete Product, in the menu helps the user just with that. First, the program displays its requirements, and what details it needs the user to input to be able to find the mentioned product in the Google Sheet and then delete it from the stock list. When the user inputs the correct, valid data, the program will display some messages to reassure the user that their request is being processed and completed. In case there is a repetition in the list, the app will only delete the first copy, leaving the rest of them on the list.

    ![Updated Stocks sheet - deleted product](readme-images/updated_spreadsheet_option3.png "Updated Stocks sheet - deleted product")

6. As a user of the application, I want to be able to see the results, as in how much I need to order and the date when
    the data was entered, and requested too.

    -	The fourth option, Get the Order List, in the menu helps the user just with that. First, the program displays its requirements, and what details it needs from the user to input, which is their stock take results. Once the user enters the correct and valid data, the program reassures the user with messages that their request is being processed. The application updates the date in the heading to today's date and uploads the inputted values to the Google Sheet and calculates the required quantity for each item. The calculation is based on the par level values and their difference with the previously taken stock take values. Once all calculations and actions are completed, the application displays the data from the stocks sheet in a table format for easy readability by the user.

    ![Updated Stocks sheet - orders](readme-images/updated_spreadsheet_option4.png "Updated Stocks sheet - orders").  

7. As a user of the application, I want to be able to see the relevant information of each product when I am ready to
    order them for better consideration, including their price, units as well.

    - The table at the completion of option 4, Get the Order List, displays many useful information of each products, namely their unit, their price, their set par level, their current stock holding amounts with the date when this input was created and lastly the amount of how much the user needs to order.
    - In addition to facilitating quick decision-making on how much of each product the user should order, this information can also be utilized to identify product trends and popularity, determine potential changes required in par levels, calculate gross profit, and steer the business towards economic profitability.

    ![results - orders](readme-images/order_information.png "results - orders").

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

## Content - Data Model

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

Bugs:
- EmailJS... was not connected properly, didnt copy the correct template parameters
- slug not working for the Booking view-url, needed to the ID parameter - based on error code suggestion in Debug=True mode