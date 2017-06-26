# 6-26-17
# nat
# 'git from the bottom up' notes

# REPOSITORY
# - changes are committed to the repository from the staging area using git-commit
# - collections of commits
# - each is an archive of what the proj's working tree looked like in past
# - contains set of branches and tags to identify certain commits by name
# - earlier states of the working tree can be checked out from repository at any time with `git-checkout`


# STAGING AREA
# - commit changes are first registered here, not the repository
# - way of "confirming" changes before commit (which records all changes at once)

# WORKING TREE
# - changes to the WORKING TREE are registered in the index with git-add
# - working tree == any directory on your file system with REPOSITORY associated
# - (you can tell if repository associated when sub-dir is named .git)
# - includes all files and sub-dirs in that directory

# COMMIT
# aka a BRANCH or a REFERENCE
# - snapshot of your working tree at some point in time
# - the state of HEAD at the time commit is made, becomes that commit's parents
#       - this forms REVISION HISTORY


# TAG
# - also a name for COMMIT, but ALWAYS NAMES THE SAME COMMIT
# - can have its own description text

# MASTER
# - main dev in most repositories is done on a branch called **master**
# -- i think this is just convention

# HEAD
# - defines what is currently CHECKED OUT
# - and therefore indicates that the branch name should be updated after next commit


# DETACHED HEAD
# if you checkout a specific commit, HEAD refers to that commit only
#       - i.e. if you check out a tag name
