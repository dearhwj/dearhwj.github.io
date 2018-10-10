---
keywords: XtraFinder
layout: post
title: 用XtraFinder增强Mac的Finder
category: 工具和效率
--- 

## 正文


### 安装
安装XtraFinder需要先关闭MAC的系统完整性保护（ System Integrity Protection，简称 SIP）。安装步骤如下：

* 重启你的 Mac；
* 在听到启动声后，按住 Command + R（⌘R） 组合键，直到出现  标志，进入恢复模式（如果担心错过时机，你也可以在状态下先按下组合键，再按开机键）;
* 选择「以简体中文作为主要语言」（或其他语言），点击向右的箭头。在「实用工具」菜单栏中选择「终端」;
* 输入csrutil enable --without debug，回车确认（你也可以输入csrutil disable以完全关闭 SIP，但不推荐这么做）;
* 重启，再安装 XtraFinder 即可。


### 主要功能
1. 指定位置打开终端：打开终端软件（iterm/xterm/terminal)并定位到选中目录。
2. 拷贝到/移动到 :可以直接在文件/文件夹上点击右键，将该文件/文件夹拷贝到指定的地方，并不需要先打开目标路径然后粘贴，有点类似于 Windows 上的「发送到」功能。
3. 剪切和粘贴 – 支持Command+X（剪切） Command+V（粘贴）