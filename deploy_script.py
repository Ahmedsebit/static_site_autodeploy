import subprocess
import os


def deploy_static(git_repo, git_repo_name, git_branch):
    subprocess.call(['git', 'clone', git_repo])
    subprocess.call(['cp', 'gazette_index.jsonlines', 'OpenGazettes/'])
    os.chdir(git_repo_name)
    subprocess.call(['git', 'checkout', git_branch])
    subprocess.call(['git', 'branch'])
    subprocess.call(['python', 'bin/build-index.py'])
    subprocess.call(['chmod', '755', './deploy.sh'])
    subprocess.call(['touch', '.env'])  # prevents FileNotFound error
    subprocess.call(['./deploy.sh'])


def get_new_no_of_items(filename):
    # opens the file safely
    with open(filename, 'r') as file_object:
        new_lines = sum(1 for line in file_object.readlines())
        print('Lines found: ', new_lines)
        return new_lines


def get_old_no_of_items(filename):
    with open(filename, 'r') as file_object:
        line_count = file_object.readline().strip()
        try:
            line_count = int(line_count)
        except ValueError as err:
            line_count = -1
            print(err, "\nContinuing...")
        print('Lines before: ', line_count)
    return line_count


def modify_item_count(filename, new_lines):

    with open(filename, 'w') as file_object:
        print('writting to line_count.txt value: ', new_lines)
        file_object.write(str(new_lines))


def main():
    print 'Starting the process\n'
    print 'dowloading index file...... \n'

    filename = 'linecount.txt'
    items_file = 'gazette_index.jsonlines'
    index_url = 'https://s3-eu-west-1.amazonaws.com/cfa-opengazettes-sn'\
                'gazettes/gazette_index.jsonlines'
    subprocess.call(['curl', index_url, '-O'])

    new_lines = get_new_no_of_items(items_file)
    line_count = get_old_no_of_items(filename)

    if line_count < new_lines:
        modify_item_count(filename, new_lines)
        # deploy the static site
        git_repo = 'https://github.com/boswellgathu/OpenGazettes.git'
        git_repo_name = 'OpenGazettes'
        git_branch = 'senegal'
        print 'deploying .......'
        deploy_static(git_repo, git_repo_name, git_branch)
    else:
        print'Nothing to see or do!'


if __name__ == '__main__':
    main()
