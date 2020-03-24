{"changed":true,"filter":false,"title":".bashrc","tooltip":"~/.bashrc","value":"# .bashrc\n\nexport PATH=$PATH:$HOME/.local/bin:$HOME/bin\n\n# load nvm\nexport NVM_DIR=\"$HOME/.nvm\"\n[ \"$BASH_VERSION\" ] && npm() {\n    # hack: avoid slow npm sanity check in nvm\n    if [ \"$*\" == \"config get prefix\" ]; then which node | sed \"s/bin\\/node//\";\n    else $(which npm) \"$@\"; fi\n}\n# [ -s \"$NVM_DIR/nvm.sh\" ] && . \"$NVM_DIR/nvm.sh\"  # This loads nvm\nrvm_silence_path_mismatch_check_flag=1 # prevent rvm complaints that nvm is first in PATH\nunset npm # end hack\n\n\n# modifications needed only in interactive mode\nif [ \"$PS1\" != \"\" ]; then\n    # Set default editor for git\n    git config --global core.editor /usr/bin/nano\n\n    # Turn on checkwinsize\n    shopt -s checkwinsize\n\n    # keep more history\n    shopt -s histappend\n    export HISTSIZE=100000\n    export HISTFILESIZE=100000\n    export PROMPT_COMMAND=\"history -a;\"\n\n    # Source for Git PS1 function\n    if ! type -t __git_ps1 && [ -e \"/usr/share/git-core/contrib/completion/git-prompt.sh\" ]; then\n        . /usr/share/git-core/contrib/completion/git-prompt.sh\n    fi\n\n    # Cloud9 default prompt\n    _cloud9_prompt_user() {\n        if [ \"$C9_USER\" = root ]; then\n            echo \"$USER\"\n        else\n            echo \"$C9_USER\"\n        fi\n    }\n\n    PS1='\\[\\033[01;32m\\]$(_cloud9_prompt_user)\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]$(__git_ps1 \" (%s)\" 2>/dev/null) $ '\nfi\n\n[[ -s \"$HOME/.rvm/environments/default\" ]] && source \"$HOME/.rvm/environments/default\"\n# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.\nexport PATH=\"$PATH:$HOME/.rvm/bin\"\n\nalias run=\"python3 manage.py runserver $IP:$PORT\" ","undoManager":{"mark":9,"position":11,"stack":[[{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":1},"action":"insert","lines":["a"],"id":3},{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"insert","lines":["l"]},{"start":{"row":51,"column":2},"end":{"row":51,"column":3},"action":"insert","lines":["i"]},{"start":{"row":51,"column":3},"end":{"row":51,"column":4},"action":"insert","lines":["e"]},{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"insert","lines":["a"]}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"remove","lines":["a"],"id":4},{"start":{"row":51,"column":3},"end":{"row":51,"column":4},"action":"remove","lines":["e"]}],[{"start":{"row":51,"column":3},"end":{"row":51,"column":4},"action":"insert","lines":["a"],"id":5},{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"insert","lines":["s"]}],[{"start":{"row":51,"column":5},"end":{"row":51,"column":6},"action":"insert","lines":[" "],"id":6},{"start":{"row":51,"column":6},"end":{"row":51,"column":7},"action":"insert","lines":["r"]},{"start":{"row":51,"column":7},"end":{"row":51,"column":8},"action":"insert","lines":["u"]},{"start":{"row":51,"column":8},"end":{"row":51,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"insert","lines":["+"],"id":7}],[{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"remove","lines":["+"],"id":8}],[{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"insert","lines":["="],"id":9}],[{"start":{"row":51,"column":10},"end":{"row":51,"column":12},"action":"insert","lines":["\"\""],"id":10}],[{"start":{"row":51,"column":11},"end":{"row":51,"column":48},"action":"insert","lines":["python3 manage.py runserver $IP:$PORT"],"id":11}],[{"start":{"row":51,"column":49},"end":{"row":51,"column":50},"action":"insert","lines":[" "],"id":12},{"start":{"row":51,"column":50},"end":{"row":51,"column":51},"action":"insert","lines":["`"]}],[{"start":{"row":51,"column":50},"end":{"row":51,"column":51},"action":"remove","lines":["`"],"id":13}]]},"ace":{"folds":[],"scrolltop":471.2265625,"scrollleft":0,"selection":{"start":{"row":51,"column":50},"end":{"row":51,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":31,"state":"start","mode":"ace/mode/sh"}},"timestamp":1585048553062}