---
keywords: ideavim,IntelliJ
layout: post
title: 定制ideavim
category: 开发工具

--- 



## 基本配置

```
" clear the highlighted search result
nnoremap <Space>sc :nohlsearch<CR>

nnoremap <Space>fs :w<CR>

" Quit normal mode
nnoremap <Space>q  :q<CR>
nnoremap <Space>Q  :qa!<CR>

" Move half page faster
nnoremap <Space>d  <C-d>
nnoremap <Space>u  <C-u>

" Insert mode shortcut
inoremap <C-h> <Left>
inoremap <C-j> <Down>
inoremap <C-k> <Up>
inoremap <C-l> <Right>
inoremap <C-a> <Home>
inoremap <C-e> <End>
inoremap <C-d> <Delete>

" Quit insert mode
inoremap jj <Esc>
inoremap jk <Esc>
inoremap kk <Esc>

" Quit visual mode
vnoremap v <Esc>

" Move to the start of line
nnoremap H ^

" Move to the end of line
nnoremap L $

" Redo
nnoremap U <C-r>

" Yank to the end of line
nnoremap Y y$

" Window operation
nnoremap <Space>ww <C-W>w
nnoremap <Space>wd <C-W>c
nnoremap <Space>wj <C-W>j
nnoremap <Space>wk <C-W>k
nnoremap <Space>wh <C-W>h
nnoremap <Space>wl <C-W>l
nnoremap <Space>ws <C-W>s
nnoremap <Space>w- <C-W>s
nnoremap <Space>wv <C-W>v
nnoremap <Space>w\| <C-W>v

" Tab operation
nnoremap tn gt
nnoremap tp gT


```

## 进阶配置

```
" built in search looks better
nnoremap / :action Find<CR>
" but preserve ideavim search
nnoremap <Space>/ /

nnoremap <Space>gc :action GotoClass<CR>
nnoremap <Space>ga :action GotoAction<CR>

nnoremap <Space>fp :action ShowFilePath<CR>
nnoremap <Space>pm :action ShowPopupMenu<CR>

```

## 参考
原文地址: [https://www.jianshu.com/p/ec6b4b4536aa](https://www.jianshu.com/p/ec6b4b4536aa)