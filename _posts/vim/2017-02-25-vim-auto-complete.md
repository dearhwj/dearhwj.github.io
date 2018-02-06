---
layout: post
title: Vim自动完成
category: Vim
keywords: Vim
--- 

## Ctrl-N 和 Ctrl-P
vim 有个非常好的关键字自动完成系统. 就是说你可以只输入很长的词的一部分, 按一个键, vim帮你把这个词自动补全. 比如说在你的代码中有一个变量叫iAmALongAndAwkwardVarName, 你可能不愿意每次用这个变量都把整个词打一遍, 这时候就可以用自动完成功能.
要使用关键字自动完成, 只要输入一个字串的前几个字母 (比如 iAmAL) 然后按 Ctrl-N或者Ctrl-P. 如果vim没有选择你需要的字串, 继续按Ctrl-N或者Ctrl-P – vim会遍历所有和你输入的前几个字母匹配的字串.