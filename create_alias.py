import click
import os

def create_alias_map():
    return {
        'cd': create_cd_alias
    }

@click.command()
@click.option('-cd', 'flag_value', flag_value='cd')
@click.argument('command_env')
@click.argument('location')
def main(flag_value, command_env, location):
    functions_map = create_alias_map()
    functions_map[flag_value](command_env, location)

def create_cd_alias(command_env, location):
    returned = '~/'
    command = 'cd '
    alias_init = 'alias '

    pwd = os.getenv('PWD')
    home, user, path = pwd[1::].split('/', 2)
    complete_bash_aliases_path = '/' + home + '/' + user + '/' + '.bash_aliases'

    with open(complete_bash_aliases_path, 'w+') as bash_file:

        target_location = ''

        if location is '.':
            target_location = alias_init + command_env + '=' + '\'' + command + returned + path + '\''
        else:
            target_location = alias_init + command_env + '=' + '\'' + command + returned + path + location + '\''

        bash_file.write(target_location + '\n')

        bash_file.close()

    os.system('. ' + complete_bash_aliases_path)


main()
