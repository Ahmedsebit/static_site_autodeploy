
import subprocess


def deploy_static(git_repo, git_repo_name, git_branch):
    # subprocess.call(['git', 'clone', git_repo])
    subprocess.call(['cp', 'gazette_index.jsonlines', 'OpenGazettes/'])
    subprocess.call(['cd', git_repo_name, '&&', 'git', 'checkout', git_branch])
    subprocess.call(['pwd'])
    subprocess.call(['python', 'bin/build-index.py'])
    subprocess.call(['chmod', '755', './deploy.sh'])
    subprocess.call(['touch', '.env']) # prevents FileNotFound error
    subprocess.call(['sudo', 'gem', 'install', 's3_website'])
    subprocess.call(['./deploy.sh'])

def main():
    print('Starting de plocess, woloyeyayiiii!!')

    filename = 'linecount.txt'
    index_url = 'https://s3-eu-west-1.amazonaws.com/cfa-opengazettes-sn/gazettes/gazette_index.jsonlines'
    # subprocess.call(['curl', index_url, '-O'])

       # opens the file safely
    with open('gazette_index.jsonlines', 'r') as f:
        new_lines = sum(1 for line in f.readlines())
        print('Lines found: ', new_lines)

    with open(filename, 'r') as f:
        line_count = f.readline().strip()
        try:
            line_count = int(line_count)
        except ValueError as e:
            line_count = -1
            print(e, "\nContinuing...")
        print('Lines before: ', line_count)
    
    if line_count < new_lines:
        with open(filename, 'w') as f:
            print('writting to line_count.txt value: ', new_lines)
            f.write(str(new_lines))
        # deploy the static site 
        git_repo = 'https://github.com/Ahmedsebit/OpenGazettes.git'
        git_repo_name = 'OpenGazettes/'
        git_branch = 'senegal'
        print('deploying .......')
        deploy_static(git_repo, git_repo_name, git_branch)
    else:
        print('Nothing to see or do!')
    

if __name__ == '__main__':
    main()
            