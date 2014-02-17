This file will contain interesting tidbits learned while doing flask and also highlight some articles and resources that were especially helpful.

The article on decorators for Python
http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

Another aritcle on Decorators, although a good one with strong historical perspective:
http://www.artima.com/weblogs/viewpost.jsp?thread=240808



## Git Stuff ##

Git does nothing with a directory until files are added to that directory. Thus, if you create an empty directory, you will not see it in the remote repo even after a commit.

git rm --cached filename - this removes a file from a repo on commit but does not delete the local copy

git rm --cached -r directoryname - removes the directory and everything in it in a recursive fashion but only from the master/remote repo. Nothing local is impacted
