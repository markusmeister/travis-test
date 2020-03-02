#!/bin/sh

set -e

[ -z "${GITHUB_PAT}" ] && exit 0
[ "${TRAVIS_BRANCH}" != "master" ] && exit 0

git config --global user.email "meister4@mac.com"
git config --global user.name "Markus Meister"

# git clone -b gh-pages https://${GITHUB_PAT}@github.com/${TRAVIS_REPO_SLUG}.git failure-output
git clone -b master https://${GITHUB_PAT}@github.com/${TRAVIS_REPO_SLUG}.git failure-output
cd failure-output
cp -r ../bookdown-demo.Rmd ./ # retrieve the knitted file
git add --all *
git commit -m"Update the book" || true
# git push -q origin gh-pages
git push -q origin master
