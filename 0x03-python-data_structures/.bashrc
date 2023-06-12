function gitpush() {
    read -p "Enter your commit message: " message
    read -p "Enter your GitHub username: " username
    git add .
    git commit -m "$message"
    git push -u origin master --username $username
}
