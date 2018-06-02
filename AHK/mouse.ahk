#InstallMouseHook

CustomColor = FFFFF ; 可以为任意 RGB 颜色 (在下面会被设置为透明).
Gui +LastFound +AlwaysOnTop -Caption +ToolWindow  ; +ToolWindow 避免显示任务栏按钮和 alt-tab 菜单项.
Gui, Color, %CustomColor%
Gui, Font, s32  ; 设置大字体 (32 磅).
Gui, Add, Text, vMyText cLime, XXXXX YYYYY  ; XX & YY 用来自动调整窗口大小.
Gui, add, edit,vMyedit1 w200, x
Gui, add, edit,vMyedit2 w200, y
; 让此颜色的所有像素透明且让文本显示为半透明 (150):
WinSet, TransColor, %CustomColor% 150
SetTimer, UpdateOSD, 200
gosub, UpdateOSD  ; 立即进行第一此更新而不等待计时器.
Gui, Show,NoActivate  ; NoActivate 让当前活动窗口继续保持活动状态.
return

UpdateOSD:
  MouseGetPos, MouseX, MouseY
  GuiControl,, MyText, X%MouseX%, Y%MouseY%
  ToolTip,X%MouseX%   Y%MouseY%
	GuiControl,, Myedit1, %MouseX%
    GuiControl,, Myedit2, %MouseY%
  GetKeyState, state, RButton
  If state = D
{
    GuiControl,, Myedit1, %MouseX%
    GuiControl,, Myedit2, %MouseY%
	SetTimer,UpdateOSD,off
}
return