#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


ie := ComObjCreate("InternetExplorer.Application")  ; 创建一个浏览器对象
ie.Visible := true   ;设置浏览器可见
ie.Navigate("http://www.baidu.com")  ;访问指定URL




