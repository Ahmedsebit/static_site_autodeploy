#!/bin/sh

setup_git() {
  cd ../
  git config --global user.email "boswell.gathu@andela.com"
  git config --global user.name "boswellgathu"
}

commit_website_files() {
  git checkout $DEPLOY_BRANCH
  git remote rm origin
  git remote add origin https://$GIT_USERNAME:$GITHUB_API_KEY@github.com/$GIT_USERNAME/$GIT_REPO_NAME.git
  git add $INDEX_FILE
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  echo Pushing changes... ${DEPLOY_BRANCH}
  git push origin $DEPLOY_BRANCH
}

setup_git
commit_website_files
upload_files