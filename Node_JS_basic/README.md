0. Executing basic javascript with Node JS
In the file 0-console.js, create a function named displayMessage that prints in STDOUT the string argument.
1. Using Process stdin
Create a program named 1-stdin.js that will be executed through command line:
2. Reading a file synchronously with Node JS
Using the database database.csv (provided in project description), create a function countStudents in the file 2-read_file.js
3. Reading a file asynchronously with Node JS
Using the database database.csv (provided in project description), create a function countStudents in the file 3-read_file_async.js
4. Create a small HTTP server using Node's HTTP module
In a file named 4-http.js, create a small HTTP server using the http module:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
Displays Hello Holberton School! in the page body for any endpoint as plain text
5. Create a more complex HTTP server using Node's HTTP module
In a file named 5-http.js, create a small HTTP server using the http module:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
It should return plain text
When the URL path is /, it should display Hello Holberton School! in the page body
When the URL path is /students, it should display This is the list of our students followed by the same content as the file 3-read_file_async.js (with and without the database) - the name of the database must be passed as argument of the file
CSV file can contain empty lines (at the end) - and they are not a valid student!
6. Create a small HTTP server using Express
Install Express and in a file named 6-http_express.js, create a small HTTP server using Express module:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
Displays Hello Holberton School! in the page body for the endpoint /
7. Create a more complex HTTP server using Express
In a file named 7-http_express.js, recreate the small HTTP server using Express:

It should be assigned to the variable app and this one must be exported
HTTP server should listen on port 1245
It should return plain text
When the URL path is /, it should display Hello Holberton School! in the page body
When the URL path is /students, it should display This is the list of our students followed by the same content as the file 3-read_file_async.js (with and without the database) - the name of the database must be passed as argument of the file
CSV file can contain empty lines (at the end) - and they are not a valid student!
8. Organize a complex HTTP server using Express
Obviously writing every part of a server within a single file is not sustainable. Let's create a full server in a directory named full_server.