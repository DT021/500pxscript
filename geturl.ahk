clipboard := ""

Sleep, 1000
Send {F6}
Send ^c	
Sleep, 1000
FileAppend , %clipboard%, Address.txt
MouseClick, Left, 1400, 940, 1, 50
Sleep, 2000
return

