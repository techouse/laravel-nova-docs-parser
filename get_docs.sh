#!/usr/bin/env bash
git clone https://github.com/laravel/nova-docs
cd ./nova-docs
npm install
npm run docs:build
rm -rf node_modules
rm -rf package-lock.json
ln -s ./nova-docs/.vuepress/dist ./docs
cd -
