#bin

echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:mrshicw/test.git
git push -u origin master
