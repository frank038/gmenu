# theme variane: 1 plain buttons - 0 toggle buttons
USER_THEME=0
# terminal: a "command" or "" to use the default one (must support the -e option)
TERMINAL="xterm"
# close on focus lost: 0 no - 1 yes
CLOSE_FOCUS_LOST=1
# category button icon size
BTN_ICON_SIZE=48
# category button label: 0 no (tooltip enabled) - 1 yes
BTN_USE_LABEL=1
# control the category buttons size: 0 no; pixel size
BTN_USE_LABEL_SIZE=0
# icon size
ICON_SIZE=64
# live searching (search for applications while typing): 0 no - 1 yes
LIVE_SEARCH=1
# number of characters to perform a seeking in label and comment
SEARCH_N=3
# window size: the width depends on the categories botton size too
WIN_WIDTH=880
WIN_HEIGHT=600
# under xorg, window position - "" for center - e.g. "100:100"
WIN_POSITION=""
# under wayland, window position: 0 bottom-left; 1 top-left; 2 top-right; 3 bottom-right
WPOS=0
# use css: 1 yes (suggested) - 0 no
USE_CSS=1
# fifo path - where the fifo file is: "" means default position; or "FULL PATH" (without /myfifo) - default: /tmp - change the bash scripts accordingly
FIFOPATH="/tmp"
# launch the applications with a single click: 0 no, 1 yes
ACTIVATE_SINGLE=1
# number of items in the view: 0 automatic; OR integer
# may depends on the scale factor used too
NUM_ITEMS=0
# fine tuning of the item width: integer
# for cosmetic purpose only
ITEMS_PAD=0