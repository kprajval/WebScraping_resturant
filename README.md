<h1>Web Scraping Project: Extracting Restaurant Data from Dineout</h1>


<h2>Overview</h2>

This web scraping project is designed to extract restaurant data from the Dineout website (https://www.dineout.co.in/) for restaurants located in Bangalore. The script navigates through all 62 pages of the website, capturing essential information about each restaurant and storing it in a CSV file.
Modules Used
<h3>1. BeautifulSoup (bs4)</h3>

BeautifulSoup is a powerful Python library for pulling data out of HTML and XML files. In this project, it is utilized for parsing the HTML content of the Dineout website, making it easy to extract relevant information such as restaurant names, addresses, ratings, and more.

<h3>2. Requests</h3>

The Requests module is employed to send HTTP requests to the Dineout website and retrieve the HTML content. It is an essential component for accessing and fetching the web pages that contain the desired restaurant data.

<h3>3. CSV</h3>

The CSV module is used for handling CSV files. It allows the script to create and write data to a CSV file, providing a structured format for storing the extracted restaurant information.

<h2>Project Workflow</h2>

    Requesting Web Pages:
        The script uses the requests module to send HTTP requests to the Dineout website, simulating the process of visiting each page.

    Parsing HTML Content:
        BeautifulSoup is employed to parse the HTML content retrieved from each web page. This allows the script to navigate through the HTML structure and locate the relevant data.

    Extracting Restaurant Data:
        The script identifies and extracts key information about each restaurant, such as name, address, rating, etc., from the parsed HTML.

    Writing to CSV File:
        The extracted data is then written to a CSV file using the csv module. Each restaurant's information is stored as a separate row in the CSV file.


<h2>How to Run the Script</h2>

    Clone the repository to your local machine.
    Install the required modules using pip install requests beautifulsoup4.
    Run the script in your preferred Python environment.

<h2>Output</h2>

The script generates a CSV file named restaurants_bangalore.csv containing the extracted data. You can open this file using spreadsheet software like Excel or Google Sheets for further analysis.

<h2>Contact Information</h2>

For any inquiries or assistance, you can reach out to the project maintainer:

    Name: Prajval
    Email: spyde40@gmail.com
    Phone number: 7483588366
