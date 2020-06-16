import json
import secrets
import string
import sys

from authlib.jose import jwt


def abort(message):
    """Print an error message and exit the program."""
    print('Error:', message)
    sys.exit(1)


def load_json_file(name):
    """Try to read and parse a JSON file."""
    try:
        with open(name) as file:
            return json.load(file)
    except FileNotFoundError:
        abort(f"file '{name}' does not exist")
    except json.JSONDecodeError:
        abort(f"file '{name}' is malformed")


def build_aws_lambda_env_vars_page_link(stage):
    """
    Build the direct link to the corresponding AWS Console page for editing the
    Lambda's environment variables.
    Use `project_name` and `aws_region` of the specified stage defined in the
    `zappa_settings.json` file for building the link.
    """

    try:
        zappa_settings = load_json_file('zappa_settings.json')[stage]
    except KeyError:
        abort(f"stage '{stage}' does not exist")

    project_name = zappa_settings['project_name']
    aws_region = zappa_settings['aws_region']

    lambda_name = f'{project_name}-{stage}'

    return (
        f'https://console.aws.amazon.com/lambda/home?region={aws_region}#/'
        f'functions/{lambda_name}/edit/environment-variables?tab=configuration'
    )


def generate_secret_key():
    """Generate a random 256-bit (i.e. 64-character) secret key."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(64))


def enter(prompt):
    """Keep prompting the user until a non-empty value is entered."""
    return input(f'Enter: {prompt}: ').strip() or enter(prompt)


def enter_credentials(template):
    """Keep prompting the user to enter all of his/her credentials."""
    return {
        key: enter(value)
        for key, value in template.items()
    }


def encode_jwt(payload, secret_key):
    """Encode a JWT with the given payload and secret key."""
    header = {'alg': 'HS256', 'typ': 'JWT'}
    return jwt.encode(header, payload, secret_key).decode('utf-8')


def build_tr_module_page_link(region, module_type_id):
    """
    Build the direct link to the corresponding Threat Response page in the
    given region for creating a module of the given type.
    """

    if module_type_id is None:
        return 'N/A'

    if region == 'us':
        region = ''
    if region:
        region = '.' + region

    return (
        f'https://visibility{region}.amp.cisco.com/settings/modules/available/'
        f'{module_type_id}/new'
    )


def main():
    if len(sys.argv) < 2:
        abort(f'Usage: python {sys.argv[0]} <stage>')

    stage = sys.argv[1]
    aws_lambda_env_vars_page_link = build_aws_lambda_env_vars_page_link(stage)

    module_settings = load_json_file('module_settings.json')

    secret_key = generate_secret_key()
    payload = enter_credentials(module_settings['jwt'])
    jwt = encode_jwt(payload, secret_key)

    message = '\n'.join([
        f"The JWT for the {module_settings['name']} module is:",
        f'    {jwt}',
        'The SECRET_KEY to validate the JWT is:',
        f'    {secret_key}',
        'Use this URL to navigate to the AWS Console and configure the '
        'SECRET_KEY environment variable using the above value:',
        f'    {aws_lambda_env_vars_page_link}',
        'Use one of these URLs to navigate to Threat Response in your region '
        f"and create the {module_settings['name']} module using your Lambda's "
        'URL and the JWT:',
        '\n'.join(
            f'    {region.upper()}: '
            f'{build_tr_module_page_link(region, module_type_id)}'
            for region, module_type_id in module_settings['region'].items()
        )
    ])
    print(message)


if __name__ == '__main__':
    main()
