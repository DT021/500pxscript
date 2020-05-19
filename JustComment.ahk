
Random, delay, 500, 1000
Sleep,delay

MouseClick, Left, 438, 968, 1, 100

x:=1
while(x<6)
	{
		Click, WheelDown
		Sleep, 200
		x:=x+1
	}

Random, delay, 1000, 2000
Sleep,delay	
MouseClick, Left, 1200, 680, 1, 100
Send, %1%
Sleep, 200
Send, %2%
Random, delay, 500, 1000
Sleep,delay
MouseClick, Left, 1460, 760, 1, 100

Sleep, 500

x:=1
while(x<10)
	{
		Click, WheelUp
		Sleep, 200
		x:=x+1
	}

Send,{Right}
	
return