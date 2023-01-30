# answer_script
make calls to chatgpt api from command line with call, or feed in a text file to chatgpt with chatfile.

1) Starting from your home directory
```cd ~/```

2) Download or copy call, chatfile, and chatfile.py to this directory
```git clone https://github.com/alien-food/answer_script```

3) create a directory within "answer_script" directory called "api_key" 
```cd answer_script && mkdir api_key && cd api_key```

4) Create a new file called "api_key" that contains your secret api_key for chatgpt
```nano api_key```

5) Give permissions to call and chatfile to execute
```chmod +x call && chmod +x chatfile```

6) Then mv call and chatfile to your /usr/local/bin directory so they are on your $PATH
```sudo mv call chatfile /usr/local/bin```

7) Make sure jq is installed on your system (JSON processor)

*macOS ```brew install jq```

*Linux Debian/Ubuntu ```sudo apt-get update && sudo apt-get install jq```

To ask chatgpt a question from your command line use call, ex...
```call "write me a 100 word essay about America"```

To feed a text file into chatgpt such as a study guide outline, or a list of terms, and get a result in a new file that you name, use chatfile. You also specify the words you want to put at the beginning and the words at the end of each prompt. Format of executing the command would look like "chatfile in_file out_file "pre-prompt" "post-prompt"
ex...
```chatfile in_file.txt out_file.txt "how would i " " for ccna"```

This will create out_file.txt with all the answers chatgpt has given you for each line from in_file.txt, where each line had "how would i " added to the beginning of the line, and " for ccna" added to the end of each prompt to specify what answer you want


