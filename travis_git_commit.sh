#!/bin/sh

setup_git() {
  cd ../
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout $DEPLOY_BRANCH
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