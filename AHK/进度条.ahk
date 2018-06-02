#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


;~ GUI,add,text,,我叫马维畅
;~ Gui,show,autosize,title
;~ WinSet, Style, -0xC00000,title
;~ return
i :=1
number := 100

CustomColor = FFFFF ; 可以为任意 RGB 颜色 (在下面会被设置为透明).
Gui +LastFound +AlwaysOnTop -Caption +ToolWindow  ; +ToolWindow 避免显示任务栏按钮和 alt-tab 菜单项.
Gui, Color, %CustomColor%
Gui, Font, s10  ; 设置大字体 (32 磅).
WinSet, TransColor, %CustomColor% 255
Gui, Add, Button,x10 y50, Start
Gui, Add, Progress,x10 y20 vMyProgress w416
Gui, Add, Text,x10 y20 vMyText w416 ; wp 表示 "使用之前的宽度"
Gui, Show,AutoSize


return

ButtonStart:
Loop
{
	GuiControl +Background800080, MyText
    GuiControl,, MyProgress, %A_Index%
    GuiControl,, MyText, %i%/100
	i := i+1 
    Sleep 50
}until,i>100
GuiControl,, MyText, 写入完成
GuiControl,,mygui,show
Sleep,1000
Gui, Destroy ;销毁窗口
Gui,mygui:add,text,,我是第二个窗口
Gui, mygui:Show
return

GuiClose:
Gui,Destroy
ExitApp





