FSWD Logs Analysis Project
=========================================================================

App Overview
-------------------------------------------------------------------------
This application analyses data in the news database and return the following information:
- Top 3 Most Popular Articles
- Most Popular Article Authors
- Days Where More Than 1% of Requests Lead to Errors

Installation and Setup
-------------------------------------------------------------------------
First, you will need to install Python on your computer:
- Go to [Python.org](https://www.python.org/downloads/) and install Python (we are running version 2.7.14)

Then, you will need to install Git in order to run this program on your local host.
- Go to [Git's website](https://git-scm.com/downloads) and install Git (we are running version 2.18.0)

Next, you will need to install Vagrant and VirtualBox.
- For Vagrant, go to [Vagrantup.com](https://www.vagrantup.com/downloads.html) (we are running version 2.1.2)
- For the VirtualBox, go to [Virtualbox.org](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) (we are running version 5.1.38)

Now, you need to configure the VirtualMachine (VM):
- Download the ZIP file [here](https://github.com/udacity/fullstack-nanodegree-vm)
  - Select **Clone or download**
  - Then select **Download ZIP**
- Save the ZIP file in desired location on your computer
- Unzip/extract all files
- Open the command prompt using Git or Git Bash
- Navigate to the **vagrant** subdirectory within the *fullstack-nanodegree-vm* folder
- Run the command `vagrant up`
- Once the vagrant up process completes, run `vagrant ssh`

If you get a shell prompt that starts with the word **vagrant**, you have successfully logged into your VM! *Keep your command prompt open as we will be coming back to it later.*

Next, you need to download the logs analysis program:
- Download the program's ZIP file [here](https://github.com/srdmdev8/logs-analysis-project)
  - Select **Clone or download**
  - Then select **Download ZIP**
- Save the ZIP file in the **vagrant** subdirectory within the *fullstack-nanodegree-vm* folder
- Unzip/extract all files

Lastly, we need to download and load the database the program will be analyzing:
- Download the database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Put the **newsdata.sql** file into the *vagrant* subdirectory within the *fullstack-nanodegree-vm* folder
- Then go back to your command prompt and `cd` into your **/vagrant** directory
- Then run the command `psql -d news -f newsdata.sql`

Once this process completes, the database has been loaded.

Running the Program
-------------------------------------------------------------------------
Ensure that you are still logged into your VM and are in the **/vagrant** directory in the Git or
Git Bash command prompt, then:
- `cd` into the **news** directory
- Run the command `python news.py`
- Once your local host is running successfully:
 - Open a web browser and enter **localhost:8000** in the URL field and press enter

Thank you for checking out my Logs Analysis Project!
