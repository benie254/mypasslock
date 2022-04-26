# myPassLock

A password manager project generated with [Python](https://www.python.org/) version 3.8.10

# myPassLock
#### This repo creates an app for managing passwords of various user accounts--with an option to save and delete accounts.
## Author
[Benson Langat](https://github.com/benie254)

## Description

The app enables users to save any account with its credentials (username, phone, email, password). Users can add new accounts to myPassLock, search to find existing accounts, display all existing accounts, and delete an existing account after searching it. Initializing the app is a user authenticator, which offers the option to create a new myPassLock account and the option to log in to an existing account. Only non-existing usernames can be created, and only an existing username & password can log a user in.

## Screenshot

<img src="https://user-images.githubusercontent.com/99865051/165284366-55a26f02-7a59-407b-838e-29b1ddc04ec9.png" >
,
<img src="https://user-images.githubusercontent.com/99865051/165284466-fa92d37d-88e0-496f-b000-4875dbbe7d03.png">

## Behavior Driven Development--BDD

1. User receives a welcome message. 
- OUTPUT: "Welcome to your myPassLock account!"
2. Short codes
3. 
4. 
5. OUTPUT: "Typer lg to LOG IN \ Typer sg to SIGN UP"
INPUT: "sg"
OUTPUT: "Account Sign Up"
OUTPUT: "Create a PassLock username ..."
INPUT: "benie" 
OUTPUT: "One more thing, benie! \ Create a password."
OUTPUT: "Enter C to Create a PassLock password ... \ Enter G to Generate a PassLock password."
INPUT: "C"
OUTPUT: "Create New Password"
INPUT: "testerPass123!"
OUTPUT: "Account creation successful. Your new password is: testerPass123! \ Keep it safe for future reference."
INPUT: "G"
OUTPUT: "Account creation successful. Your generated password is: @kYYd2901?! \ Keep it safe for future reference."
OUTPUT: "Type lg to LOG IN \ Type sg to SIGN UP"
INPUT: "lg"
OUTPUT: "Enter your PassLock username ... :"
INPUT: "benie"
OUTPUT: "One more thing, benie!"
OUTPUT: "Enter your PassLock password ... :"
INPUT: "@kYYd2901?!"
OUTPUT: "Login successfull ...... You are in."
OUTPUT: "Hello, benie. This is your PassLock account. Wanna have a look around?"
OUTPUT: "Use these short codes:"
OUTPUT: "se - save existing acc, cn - create new acc, da - display accs, fa - find acc, del - delete acc, ex - exit"
INPUT: "se"
OUTPUT: "Add Existing Account"
OUTPUT: "Account name ...", "Username ...", "Password", "Email--if relevant", "phone number--if relevant"
INPUT: "Twitter", "benie254", "hala123!", "benie@gmail.com", "0712 345 678"
OUTPUT: "Existing Account Twitter for username: benie254 saved."
OUTPUT: "Use these short codes:"
OUTPUT: "se - save existing acc, cn - create new acc, da - display accs, fa - find acc, del - delete acc, ex - exit"
INPUT: "da"
OUTPUT: "Here is a list of all your accounts", "Acc: Twitter | eml... benie@gmail.com | usr... benie254 | pass... hala123!"
OUTPUT: "Use these short codes:"
OUTPUT: "se - save existing acc, cn - create new acc, da - display accs, fa - find acc, del - delete acc, ex - exit"
INPUT: "fa"
OUTPUT: "Enter the account you want to search for:"
INPUT: "Twitter"
OUTPUT: "Results for ......", "Account name: Twitter", "Email ...... benie@gmail.com", "Phone number ...... 0712 345 678", "Password ...... hala123!"
OUTPUT: "Use these short codes:"
OUTPUT: "se - save existing acc, cn - create new acc, da - display accs, fa - find acc, del - delete acc, ex - exit"
INPUT: "del"
OUPUT: "Enter the account you want to delete:"
INPUT: "Twitter"
OUTPUT: "Are you sure you want to delete this pass account? *** y (for YES) / n (for NO)"
INPUT: "n"
OUTPUT: "Account will not be deleted"
INPUT: "y"
OUTPUT: "Your account Twitter has been deleted"
OUTPUT: "Use these short codes:"
OUTPUT: "se - save existing acc, cn - create new acc, da - display accs, fa - find acc, del - delete acc, ex - exit"
INPUT: "ex"
OUTPUT: terminates operations--breaks out of app.




## Setup/Installation Requirements

* To use this open-source repo, clone it; to contribute, fork it. 
* Open your Terminal (CTRL + ALT + T on Ubuntu/Linux). 
* Make a destination directory in your preferred path (where you would like to clone the repo into.)
* Run the command ``` cd yourDestinationDirectory ```
* Run the command ``` git clone https://github.com/benie254/mypasslock.git ``` to clone the repo into your destination directory. 
* Run the command ``` cd myPassLock ``` to move you into this repo's directory.
* Run the command ``` atom . ``` for Atom or ``` code . ``` for VSCode --opens the directory in your preferred code editor. (it is okay if you use something different.)
* Happy coding!

## Known Bugs

No known bugs. Please report any issues or encountered bugs! 

## Technologies Used

* [Python](https://www.python.org/) 

## Important resources 

* Unittest- test framework for [Python](https://www.python.org/)

## Support and contact details

Reach out with any issues, concerns, or contributions to [Benie-throughMail](davinci.monalissa@gmail.com)

### License

*Copyright (c) 2022* ***Benson Langat***

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*

###
Copyright (c) 2022 **Benson Langat**

[Python](https://www.python.org/) version 3.8.10
