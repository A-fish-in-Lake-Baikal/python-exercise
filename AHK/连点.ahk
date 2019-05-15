#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.








F2::
	Sleep,300
	loop
	{
		Send,1{Click}
		Sleep,70
		if GetKeyState("F2")
		{
			break
		}
	}
return