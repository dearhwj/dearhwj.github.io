# Python的__getitem__方法

__getitem__ 专用方法很简单。像普通的方法 clear，keys 和 values 一样，它只是重定向到字典，返回字典的值。但是怎么调用它呢？哦，你可以直接调用 __getitem__，但是在实际中你其实不会那样做：我在这里执行它只是要告诉你它是如何工作的。正确地使用 __getitem__ 的方法是让 Python 来替你调用。
(2)  这个看上去就像你用来得到一个字典值的语法，事实上它返回你期望的值。