#! bin/sh
BLOG_HOME='/data/blog'
kill -9 `ps aux | grep jekyll| grep -v grep| awk '{print $2}'`
cd $BLOG_HOME
jekyll server --detach  --host 0.0.0.0

