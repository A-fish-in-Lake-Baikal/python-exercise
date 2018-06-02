#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Gui,font,s20
Gui,font,cffffff
Gui, Color, EEAA99
Gui +LastFound  ; 让 GUI 窗口成为 上次找到的窗口 以用于下一行的命令.
WinSet, TransColor, EEAA99 255
Gui -Caption

Gui,add,text,vMytext w600,xxxxx  yyyyy
Gui,add,text,vMytext1 w600
SetTimer,updateOSD,200
gosub,updateOSD
gui,show,AutoSize
return

updateOSD:
        time=%A_MM%月%A_DD%日
        time2=%A_Hour%:%A_Min%:%A_Sec% 
        GuiControl,,MyText,%time%,%time2%

F10::
ExitApp