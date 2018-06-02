#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Gui Add,Text,,ceshi
Gui Add, Edit, w150 vMyEdit
Gui,SHOW,w200 h400,menu
Menu, MySubmenu, add, Item1
Gui, Menu, MyMenuBar