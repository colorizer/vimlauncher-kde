# vimlauncher-kde
Python code for launching vim from anywhere. I am using this to input latex anywhere.
## Dependencies
1. xdotool
2. xclip
3. python3
4 konsole

## Bugs
- [ ] Unable to paste the output through command.
- [ ] Not able to set shortcut for launching

## Workarounds
- Change the shortcut for saving & closing the vim to `CTRL-d` so that you can `CTRL-d` `CTRL-v` for fast input. This can be done by appending the following lines to the end of `.vimrc` file.
```
" Remap save and exit to <ctrl>d
inoremap <C-d> <esc>:wq!<cr>               " save and exit
nnoremap <C-d> :wq!<cr>
```
- Manually set the shortcut through KDE settings.

## Thanks
This code is mainly derived out of Gilles Castel's works on making tex input faster. Those shortcuts are part of my daily workflow now. Here is a link to his [profile](https://github.com/gillescastel).

