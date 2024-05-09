# Django_Assessment

1.Create a virual environment
2.In the same directory create a folder called"visualizer".
3.Clone the repository using git clone <Link> command to a speific folder.copy the contents inside the repository folder into the folder called "visualizer" that was created before
4.Activate the virual envirinment using venv\Scripts\activate command
5.Go inside the projects folder("visualizer") using the commandline and install dependacies using the command "pip install -r requirements.txt"
6.open through Vs code and install sqlite extention
7.right click on the "db.sqlite3" to see the database name
8.Copy the csv files and paste inside the project directory
9.Using the command prompt run the sqlite3.exe using the command "sqlite3.exe db.sqlite3" to work with the db
  then type .mode csv and enter
  type .import <csv_file.csv> <database_name>
  once the csv s are loaded exit the terminal
10.once exited open up a new terminal and activate virtual environment and goto the project directory and type "py manage.py runserver" to run the project
