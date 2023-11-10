This is a stepwise approach to how I transferred my screenshots to he github repository using SFTP
1) opened my cmd prompt on my windows system and entered "sftp host@username", pressed enter
2) entered my password as provided on the sandbox page and pressed enter
3) using mkdir directory, I crreated a new directory so that I would be able to trace my uploads
4) using lcd, I navigated my local directory to the directory where my uploads are located
5) using "put screenshots-name" I uploaded he files to my newly created sandbox directory.
6) I exited the sftp using "exit" 
7) I logged into my ssh sandbox using "ssh host@username" and password to begin the github transfer
8) I cloned the alx-system_engineering-devops, created the command_line_for_the_win
8) I navigated to my newly created sandbox directory where my uploaded files are located
9) I moved the files to the command_line_for_the_win directory
10) I git added, commited and pushed
