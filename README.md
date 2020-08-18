[![Gitter Chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Response "Gitter Chat")
[![Travis CI Build Status](https://travis-ci.com/CiscoSecurity/tr-05-jwt-generator.svg?branch=develop)](https://travis-ci.com/CiscoSecurity/tr-05-jwt-generator)

# Threat Response JWT Generator

Single Python CLI command that:

1. Prompts the user to enter the required third-party credentials for a given
integration, encodes them into a `JWT` and signs it with a randomly generated
`SECRET_KEY`. If the credentials are already in a JSON file, then the user may
just pass the file as an additional argument to the script using the optional
`-f/--file` parameter, e.g. `-f credentials.json` or `--file credentials.json`.

2. Prints the `JWT` and `SECRET_KEY` along with a couple of extra links:

   - the link to the corresponding AWS Console page for editing environment
   variables of the user's Lambda;

   - the links to the corresponding Threat Response pages (in all available
   regions so that the user can select the appropriate one) for creating a
   module of a given type (the module type depends on the actual integration).

3. Instructs the user what to do next.

**NOTE.** The script assumes that in its the working directory there are two
configuration files: `zappa_settings.json` and `module_settings.json`. Check
the [Relay Template](https://github.com/CiscoSecurity/tr-05-serverless-relay)
repository to get more insight into how such files may look like.

## Installation

- Local

```
pip install --upgrade .
pip show threatresponse-jwt
```

- GitHub

```
pip install --upgrade git+https://github.com/CiscoSecurity/tr-05-jwt-generator.git[@branch_name_or_release_version]
pip show threatresponse-jwt
```

## Usage

`jwt --help`

```
usage: jwt [-h] [-f FILE] stage

positional arguments:
  stage                 a Zappa stage defined in the 'zappa_settings.json'
                        file

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  a JSON file with some credentials to encode into a JWT
```

## Execution

`jwt dev`

```
Enter: Gigamon ThreatINSIGHT API Key: kfy0d9D-MpTDTdoeaPVKFA
The JWT for the Gigamon ThreatINSIGHT module is:
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZnkwZDlELU1wVERUZG9lYVBWS0ZBIn0.QWE9wwC2U_6UeJaav2kUXPFTF3aljGL-T0oMaZfMT5k
The SECRET_KEY to validate the JWT is:
    2qNjghi9O6TFndbifgqwffnXpFyDybHgsQOSIZddvzt4IIRtc0mbHL27TarcK67c
Use this URL to navigate to the AWS Console and configure the SECRET_KEY environment variable using the above value:
    https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/tr-gigamon-threatinsight-relay-dev/edit/environment-variables?tab=configuration
Use one of these URLs to navigate to Threat Response in your region and create the Gigamon ThreatINSIGHT module using your Lambda's URL and the JWT:
    US: https://securex.us.security.cisco.com/settings/modules/available/f4b2cf01-0447-436e-8dc1-b0b15049888b/new
    EU: https://securex.eu.security.cisco.com/settings/modules/available/cdf11c33-0891-491a-8e36-201e4decd3d0/new
    APJC: https://securex.apjc.security.cisco.com/settings/modules/available/904e961f-ff81-48f5-aeb0-5c033e2054b7/new
```

**NOTE.** The example above uses the configuration files
(i.e. `zappa_settings.json` and `module_settings.json`) from the
[Gigamon ThreatINSIGHT Relay](https://github.com/CiscoSecurity/tr-05-serverless-gigamon-threatinsight)
repository.
