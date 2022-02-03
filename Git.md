# git add filename OR git add -A

## Git add filename always used for single file name has been changed and put on stage
## area where git add -A used when user want to add all files changed in one time

### $ git add filename
### $ git add -A

# git gommit

## git commit use whenuser want to write what been changed and let the other users know
## before pushed to the staging area

### $ git commit -m 'Adding change message'

## If add the file to staged area and change your mind to get out from staging area use
	git reset HEAD filename 
## Example
	touch newfile
	git add newfile
	
	- Now we take out from staged branch
	git reset HEAD newfile

	HEAD refers to the last commit on the current branch we are on.

	## This will add the file and commit them in short way instead of using add then commit
	git commit -a -m 'Add the file'

	## If you change your mind you can use:
	git reset --soft HEAD^

	## --amend add the message to last commit and 
	git add file.txt
	git commit --amend -m 'Modify read and add file.txt'

	The above will reset the last commit and bring the file to saging area

	## Undo last commits and all changes
	git reset --hard HEAD^

	## Undo last 2 commits and all changes
	git reset --hard HEAD^^

	## add first time to the link using following
	git remote add origin https://github.com/DilshadGit/python/Git.md

	git push -u origin master

	## add new remotes
	git remote add (name) (https://address.com)

	## to remove remotes
	git remote rm (name

	## -u help to not use next time the branch name
	git push -u (name) (branch)

	## heroku create
	git remote -v

	heroku git@heroku.com: dev-server-1234.git (fetch)
	heroku git@heroku.com: dev-server-1234.git (push)
	origin https://github.com/Dilshadgit/git-test.git (fetch)
	origin https://github.com/Dilshadgit/git-test.git (push)

	git push heroku master
# Create new branch 

## git branch branchname is to create new branch and git checkout branchname is to move to
## new branch has been created

### $ git branch branchname 
### $ git checkout branchname 

# Create new branch and move to the new branch in one time
## Create new branch and move to the creanch is created
### $ git checkout -b branchname

# Git push -u origin master first and git push origin master second

## The first push used when the branch is new and push first time change which user use -u
## the second push used when user already pushed first branch in this case don't type -u

### $ git push -u origin master
### $ git push origin master

# Git Remote 

## The git remote display the location repository of the git

### $ git remote -v
origin	git@github.com:DilshadGit/Python.git (fetch)
origin	git@github.com:DilshadGit/Python.git (push)

### git remote -v
origin	git@bitbucket.org:DilMac/ecomma.git (fetch)
origin	git@bitbucket.org:DilMac/ecomma.git (push)

# Display different on the file has been changed

## To know what been changed use diff

### $ git diff filename

## If you added the file to staging area and you write git diff filename nothing
	display to check what has been change in stage area enter (git diff --staged)



# git pull origin respository branch

## When you do pull always use origin before the branch name will pull all has been changed
## since the last time pushed to server

### $ git pull origin master git pull origin feature/pages

# Important
# git merge

## You use git merge when you are in new branch which already created and made the changes
## added to the current branch and already pushed. You checkout from the new branch to the 
## master branch like following:

### $ 1. git branch new_branch # That is the branch eveything changed and pushed
### $ 2. git checkout master
### $ 3. git pull origin master # this used to make surer if anyone has mage changes and 
###		 pushed to master branch
### $ 4. git branch --merged
### $ 5. git merge feature/new_branch
### $ 6. git push origin master
### $ 7. git branch --merged to make sure is up to date before using delete branch
### $ 8. git branch -d feature/new_branch
### To make sure if branch deleteon the local repository do following
### $ git branch -a
### Here you already deleted from local machine but still display on the remote repository
	to delete from remote repository use 
### $ git push origin --delete feature/new_branch

#

##

### $

#

##

