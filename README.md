# gmenu
Menu application that lists the programs installed.

Free to use and modify.

This program is a standalone graphical menu application
that lists all the programs installed, through the desktop files.

Required:
- python3
- gtk3
- Xorg

This program can be open and closed using a fifo file created
in this program folder.
The commands are:
echo "__open" > myfifo (show the window)
echo "__close" > myfifo (hide the window, also with the key esc)
echo "__exit" > myfifo (close the program)

Some options can be setted in the menusettings.py file.

Features:
- indipendent from anything else: just execute it and use the commands above;
- Bookmarks: can be reordered;
- searching entry: search applications by name and in the comment;
                   live search too;
- css style file; 
- two themes: the default one is with simple buttons as category selectors,
              the other one is with toggle buttons as category selectors.
- icon size;
- fixed position or centered;
- update the menu in background;
- right mouse click on an item to bookmark it (also for remove it)
- middle mouse click (on an item) to force a menu rebuild;
- the program closes after losing focus.

Known issues:
- the bookmarks sometimes cannot be reordered.
