# answer_script
make calls to chatgpt api from command line with call, or feed in a text file to chatgpt with chatfile.

1) Start in a new directory called "openai"
```mkdir openai && cd openai```

2) Download or copy call, chatfile, and chatfile.py to this directory

3) create a directory within "openai" directory called "api_key" 
```mkdir api_key```

4) Create a new file called "api_key" that contains your secret api_key for chatgpt
```nano api_key```

5) Then mv call and chatfile to your /usr/local/bin directory so they are on your $PATH
```sudo mv call chatfile /usr/local/bin```

To ask chatgpt a question from your command line use call, ex...
```call "write me a 100 word essay about America```

To feed a text file into chatgpt such as a study guide outline, or a list of terms, and get a result in a new file that you name, use chatfile. You also specify the words you want to put at the beginning and the words at the end of each prompt. ex...
```chatfile in_file.txt out_file.txt "how would i " " for ccna"


