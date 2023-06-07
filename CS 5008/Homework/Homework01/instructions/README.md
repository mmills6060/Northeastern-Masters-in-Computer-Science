# Homework 1: Instructions

For this homework, you are going to work on getting your development environment setup with C and git. This will vary slightly for every student, but the goal is to get you comfortable with the tools you will be using for the rest of the semester.

For this assignment, you will
need to make sure the following is in place

1. You have a Khoury Account Setup 
   * [Apply](https://my.khoury.northeastern.edu/account/apply) and 
   * Test your [profile](https://my.khoury.northeastern.edu/session/login)
2. Have your Github.com Account Setup ([Instructions](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account))
   * Free account is fine
   * We recommend a professional email that is not tied to a school, so your account exists after you graduate.
3. If you haven't already, in your canvas shell you will be provided with a Github classroom link that will
let you use this repository as a template for your work. 

You will also need *git* installed ideally on your local system. If you are using a Windows system, you will need to install [Git Bash](https://git-scm.com/downloads). If you are using a Mac or Linux system, you should already have git installed.

## GIT Commit
Throughout this assignment you will be committing your changes to your repository. When you commit to Git.
* Commit frequently after every major change
* Use active/action verbs in your message, that are short yet descriptive
  * Here is a BAD commit message
  > changes made to readme
  * Here is an example of a better commit message
  > Added personal ident info: name, gitname, semester

See resources for into on Git Commit

**NOTICE**: All assignments will need to have _at least_ three commits to earn full points. Most assignments will have many more than that (this is the only one who reaching three may be limited).

## Part 1 - SSH 
👉🏽 **Task**  👈🏽:  SSH into the Khoury servers, and (optionally) setup your public/private keys for future use.  You will take a screenshot and submit that screenshot as proof of completion. 

1. You will want to use SSH from your local computer to log into Khoury servers. 
   1. For mac and linux it is already built in
   2. For windows it depends on your version, however for 10 and 11 it is built into windows via OpenSSH
2. (optional) After logging in once, you will want to use the resources below to setup your **ssh keys**. 
   1. While optional it is highly recommended to make your workflow easier
3. Once Logged into the khoury linux servers, type `pwd` and hit return.
   * `pwd` is a linux command that shows you the absolute path of your current (present) working directory
   ![SSH Login Example]
4. Create a directory for storing your assignments. For example: `cs5008`
5. Take a screenshot, and save it as `ssh_login_lastname.png` where *lastname* is your last name.
   * Important❗ This screenshot will be stored in your git repository (see below), but for now, store it locally on your computer to copy later.

> Besides showing you can SSH into the khoury servers, you are not *required* to work on the servers. We just like to make sure you know how to connect to them incase your  local environment is not working. 



## Part 2 - Terminal?

👉🏽 **Task** 👈🏽: Take a screenshot that you have correctly cloned the git repository for this assignment.

On the various operating systems, there are terminal applications. These are used to interact with the operating system. For example, you can use the terminal to navigate your file system, and run programs. 

For Mac OS or Linux, the application is called terminal. For Windows 10 or 11, it is also called terminal, but that runs multiple types of processes. We recommend in the windows terminal, you either use the WSL (Windows Subsystem for Linux) or PowerShell. You can also access your terminal through your IDE, such as VS Code or CLion.

If you have it setup right, all of the operating systems should allow the `ls` command. This command will list the files in the current directory. 

1. Create a directory on your computer for CS 5008. For example, `cs5008`
2. Do a git *clone* request for your hw1 repository. 
   * You can do this by clicking the green "Code" button on the main page of your repository, and copying the link using the copy button. 
     ![Clone Example]
     * IMPORTANT❗  Double check that it is your personal repo, and not the general assignment repo. 
   * Then, in your terminal, navigate to your `cs5008` directory using `cd`, and type `git clone <link>`. (see linux commands in resources)
   * For example, if your link is `https://github.com/CS5008-khoury-lionelle/lionelle-hw1.git`
   * The command would be `git clone https://github.com/CS5008-khoury-lionelle/lionelle-hw1.git`

After it is cloned, take a screen shot of your terminal, and save it as `terminal_lastname.png` where *lastname* is your last name.

> You can also do this on the Khoury servers, but in order to get git working, you will need to setup a Personal Access Token (PAT) for your Github account. Here is a [example](https://github.com/CS5008-khoury-lionelle/Resources/blob/main/pat_guide.md).

:star: HINT :star: The first time using Git, you will have to setup your email and name. You can do this by typing `git config --global user.email "your_email"` and `git config --global user.name "your_name"`.

### :star: Using and IDE :star: 
If you are using an IDE, such as VS Code or CLion, git is built into the applications, and we recommend going to 'new project from version control' and using the link to your repository. The name may change based on your IDE, but the functionality is the same. Feel free to ask in the general chat in MS Teams and students can help each other out pointing to the correct spot based on their IDE + OS. 


## Part 3 - Your First C Application
You will want to get C running on your system for the next part of this assignment. Here is a quick [reference](https://github.com/CS5008-khoury-lionelle/Resources/blob/main/InstallC.md) for various options. You can also do all this work on the Khoury servers via the terminal. 

👉🏽 **Task** 👈🏽: Fix [main.c](../main.c)

1. Open the file `main.c` in your IDE or text editor.
2. Read through the documented code. *You **DO NOT** have to know C to complete this assignment*. Instead, you should use what you know about programming languages in general to get an idea of what the code is doing. We will cover C in the next module. 
3. Compile `main.c`. Make sure you are using the `-Wall` flag. 
   * For most people the command will be `clang -Wall main.c -o main.out`
   * If you do that, you can then run the program by typing `./main.out` in the terminal. 

> Your environment may modify the compile command a bit (for example Clion using cmakefiles.txt). If you are having trouble, ask in the general chat in MS Teams and students can help each other out. You will want to make sure you are using clang or gcc, and not the MSVC compiler (which is the default for Windows).

4. You will notice there are warnings when you compile using the clang compiler! This would cause the code to fail in the autograder as your code has to compile without warnings.
   1. **FIX**: Fix the warnings in the code. 
5. Now look at the logic of the program. Proper execution of the program looks like the following
```text
Please enter your name: Bob
Please enter a number: 20

Hello Bob
You are not old enough to drink in the US
Goodbye Bob
```
or
```text
Please enter your name: Jane
Please enter a number: 21

Hello Jane
You are old enough to drink in the US
Goodbye Jane
```
6. **FIX**: Fix the logic of the program so that it works as expected. Spaces between : and the name/number are required, as are the new lines. Make sure you run the program before trying to fix it, as there may be an unusual error that you can't see in the code (it may actually cause the program to crash)

> A note on "Free"  
> In C, you have to manually free memory that you allocate. This is because C is a low level language, and it is up to the programmer to manage memory. In higher level languages, such as Python, Java, or C#, the language will automatically free memory for you. This is why you don't have to worry about it in those languages. However, what happens if you "free" memory, and then attempt to access the variable? This is called a "use after free" error, and it can cause a lot of problems. Use this knowledge to help find the mystery error. 

### Wait but I don't know C...
The errors in the code are similar to ones you can find in python or java. They are string issues or return statement issues. You also have examples throughout the code on how to do it correctly.  More importantly, as programmers making associations between languages becomes second nature to us. For many, your first job may be using a language you never programmed before, and you will be expected to pick up the language quickly. In the end, it is just a tool, and we use the best tool for the job. In this course, we use C, so you better understand what is going on 'under the hood' that many higher level languages hide.

### :star: REMINDER :star:
Make sure to commit between each change! For example, you fix spaces, you do a git commit -m'fixed spaces in strings'. Then you fix the return statement, you do a git commit -m'fixed return statement in (func name)'. Then you fix the logic, you do a git commit -m'fixed logic in (location)'.


## Part 4: README.md questions
You will notice there are questions in your readme.md file. You will want to answer these questions in the readme.md file. For this course, we will be doing a lot with Readme.md files, so it is important to get used to them. You may even want to review the [Markdown Guide](https://guides.github.com/features/mastering-markdown/) to get a better understanding of how to format your readme.md file.

Every assignment will have questions in your README.md, so make sure you review them!


## 📝 Grading Rubric

Click on the Gradescope link on the sidebar of the Canvas course. Select CS 5008, and select Homework 01. Ideally, you follow the link at the bottom of the assignment page. 

On Gradescope, select that you want to submit your code via Github, and connect your Github account with Gradescope. You'll need to authorize Gradescope to have access to your account. 

1. Learning (AG)
   * Code compiles without warnings
2. Approaching  (AG)
   * Simple errors fixed in the code (spacing, string issues, etc.)
3. Meets  (AG)
   * Harder logic errors are fixed (free, logic)
4. Exceeds  (MG)
   * Screenshot of logging into the Khoury Servers 
   * Screenshot of Git cloned repository
   * At least 3 commits
   * README.md questions answered correctly


AG - Auto-graded  
MG - Manually graded

### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade **IF** you submit by the **DUE DATE**. Submitting late may mean it isn't possible for the MG to be graded before the **AVAILABLE BY DATE**, removing any windows for your to resubmit in time. While it will be graded, it is always best to *submit by the due date*, so you have full opportunity to improve your grade.

### Instruction Home
Please note, if you are viewing these instructions in your repository copy, it is possible for your local copy to be out of sync with the official instructions. 
Double check instructions by going to: [HW 1 - Instructions](https://github.com/CS5008-khoury-lionelle/hw01/tree/main/instructions)



## 📚 Resources

### Git
* [Git Handbook](https://docs.github.com/en/get-started/using-git/about-git) -- start here
* [clone](https://github.com/git-guides/git-clone)
* [commit](https://github.com/git-guides/git-commit)
* [add](https://github.com/git-guides/git-add)
* [push](https://github.com/git-guides/git-push)
* [How to Write Better Commit Messages](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)

### SSH Key
* [What are SSH Keys](https://www.w3docs.com/learn-git/ssh-key.html)
  * Note: the line about windows is incorrect since windows 10. You can run ssh-keygen directly via powershell (see below)
* [How To Generate SSH Keys on Windows 10+](https://www.howtogeek.com/762863/how-to-generate-ssh-keys-in-windows-10-and-windows-11/)

### Adding SSH Public Key to Remote Server

* [Linux/Mac: How to add public SSH key on a remote server](https://www.howtogeek.com/168147/add-public-ssh-key-to-remote-server-in-a-single-command/)

#### Windows Upload Command
There are multiple ways to upload your public key to your remote server. The easiest simply being logging into the server and cutting and pasting the key into authorized_keys. However, the following command line will do that for you (make sure to make changes)

```console
> ssh USERNAME@login.khoury.northeastern.edu "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys2 || exit 1" < PATH-ON-WINDOWS\id_rsa.pub
```

The PATH-ON-WINDOWS is the path to your public key. Often it will be C:\Users\YOUR_WINDOWS_USER_NAME\.ssh\id_rsa.pub as that is the default location when you run keygen. 

#### Linux and Mac Upload Command
There is also a program you can install with app-get or brew. `ssh-copy-id`

```console
> ssh-copy-id USERNAME@login.khoury.northeastern.edu
```
### Visual Studio Code Remote

* [VSCode Remote Development Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
* [VSCode Remove Repositories](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-repositories)
* [Using VSCode Remote Tutorial](https://dev.to/phiilu/use-visual-studio-code-remote-to-edit-files-on-servers-382i) - note you may want to follow the ssh-key setup above as compared to the ones presented in the tutorial.


### Command Line Editors
* Vim - use `vimtutor` via the command line on the Khoury servers
* [Vim School](https://vimschool.netlify.app/)
* [Very basic emacs](http://ocean.stanford.edu/research/quick_emacs.html)
* [Emacs](https://www.gnu.org/software/emacs/tour/)
* Emacs has a built in tutorial
   * type emacs on the command line emacs   
   * then type control-h followed by t
* [Redhat Beginning Guide to Emacs](https://www.redhat.com/sysadmin/beginners-guide-emacs)
* [Guide to Nano](https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/)


### Linux
* [Customize Bash Prompt in Linux](https://phoenixnap.com/kb/change-bash-prompt-linux)
* [50 Linux Commands with examples](https://www.puttygen.com/linux-commands)

<!-- Link definitions-->
[SSH Login Example]: ssh_login_example.png
[Clone Example]: clone_example.png
