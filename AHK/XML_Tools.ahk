#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn All, StdOut  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
; 监听快捷键 Ctrl + Alt + F
^!f::
    ; 获取剪贴板中的文本
    clipboard := ""
    SendInput ^c
    ClipWait, 1

    ; 如果剪贴板中的内容不是 XML 格式，则不进行格式化
    if not InStr(clipboard, "<?xml") {
        MsgBox, 48, Error, The clipboard does not contain XML data.
        return
    }

    ; 执行格式化命令
    Run, cmd /c "echo %clipboard% | xmllint --format -", , Hide

    ; 获取命令行输出的文本
    clipboard := ""
    ClipWait, 1
    SendInput ^c
    ClipWait, 1

    ; 将格式化后的文本替换回剪贴板中的内容
    clipboard := Trim(clipboard)
    Clipboard := clipboard
return