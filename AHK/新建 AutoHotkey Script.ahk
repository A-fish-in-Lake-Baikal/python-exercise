#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Run Notepad
Sleep 1000
WinWait 无标题 - 记事本
SendMessage, 0xC, 0, "New Notepad Title" 
PostMessage, 0x111, 40239, 0, , New Message