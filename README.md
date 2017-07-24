# static_site_autodeploy
Scripts to deploy jekyll

### Committing from Travis
 - This requires a token from github(personal access token)
 - After creating this token add it to as environment variable `GITHUB_API_KEY` on Travis
 - After this, other Environ Variables to add will be `GIT_USERNAME`, `GIT_REPO_NAME`, `DEPLOY_BRANCH` and `INDEX_FILE`

    * `GIT_REPO_NAME` - name of this Github Repo
    * `DEPLOY_BRANCH` - The branch from which the script is ran
    * `INDEX_FILE` - The file which is being pushed to github from Travis
### Running the program
- Clone the repo
  ```
  git clone https://github.com/Ahmedsebit/static_site_autodeploy.git
  
  ```
- Create a python enviroment

  ```
  virtualenv -p python3 env
  
  ```
  
- Activate the enviroment
  ```
  source env/bin/activate
  
  ```

- Install the requirements
  ```
  pip install -r requirements.txt
  
  ```

- Add the country to the enviroment
  ```
  export COUNTRY = 'country'
  
  ```

- Run the python file
  ```
  python deploy_script.py
  
  ```
   
