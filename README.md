## Information systems software engineering. Master's degree, 1st year
### [Digital root](https://github.com/VladyslavKharchenko/ISSE/blob/master/digital_root.py)
Digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.
#### Examples:
- 16 --> 1 + 6 = 7
- 942 --> 9 + 4 + 2 = 15 --> 1 + 5 = 6
- 132189 --> 1 + 3 + 2 + 1 + 8 + 9 = 24 --> 2 + 4 = 6
- 493193 --> 4 + 9 + 3 + 1 + 9 + 3 = 29 --> 2 + 9 = 11 --> 1 + 1 = 2
---
### [Find the outlier](https://github.com/VladyslavKharchenko/ISSE/blob/master/outlier.py)
You are given an array (which will have a length of at least 3 but could be very large) containing integers. The array is either entirely composed of odd integers or entirely of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#### Examples:
- [2, 4, 0, 100, 4, 11, 2602, 36]
  - Should return: 11 (the only odd number)
- [160, 3, 1719, 19, 11, 13, -21]
  - Should return: 160 (the only even number)
---
### [GIT](https://github.com/VladyslavKharchenko/ISSE/blob/master/reflog)
1. Init repo, create branch master
2. Switch to the develop branch
3. Create file a.txt
4. Commit file a.txt
5. Switch to branch feature1
6. Create file b.txt, commit, amend commit where you change the message
7. Switch to branch feature2 created from develop
8. Create file d.txt, commit, reset it so that you could rename your commit
9. Merge feature1 and feature2 into develop using fast-forward
10. Squash all the commits in develop using interactive rebase
11. Rebase develop into master
12. Save FULL reflog to any source and send it for verification
