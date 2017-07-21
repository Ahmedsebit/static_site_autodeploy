# static_site_autodeploy
Scripts to deploy jekyll

## Adding a deploy key
This is done so that travis can be able to update the index_file
 - Locally while inside the repository run the command
   `ssh-keygen -t rsa -b 4096 -C "your-email@gmail.com" -f deploy-key`
 - Add the deploy-key.pub contents to to your repo’s settings under Settings -> Deploy Keys.
 - Be sure to check the “Allow write access”. The deploy key will be used to authenticate the travis-ci build in order to push the website.
 - We will next have to encrypt the deploy-key so we can commit it to our repository safely.

#### Encrypt Deploy-key
 - First, you will need to install the travis command line tools, which is a Ruby Gem. After installing ruby, you can run the command: `gem install travis`
 - Next enable the repo on Travis
 - Inside the repository’s git repo on your own computer, run the command: `travis encrypt-file deploy-key`
 - The output for this is;
    ```
    encrypting deploy-key for boswellgathu/static_site_autodeploy
    storing result as deploy-key.enc
    storing secure env variables for decryption

    Please add the following to your build script (before_install stage in your .travis.yml, for instance):

        openssl aes-256-cbc -K $encrypted_024a67fab80c_key -iv $encrypted_024a67fab80c_iv -in deploy-key.enc -out deploy-key -d

    Pro Tip: You can add it automatically by running with --add.

    Make sure to add deploy-key.enc to the git repository.
    Make sure not to add deploy-key to the git repository.
    Commit all changes to your .travis.yml.
    ```

    - This will encrypt the deploy-key with the Travis-CI public key, therefore it can only be accessed on the Travis-CI infrastructure. The above line is very important to remember, you will copy / paste it into the .travis.yml under script
