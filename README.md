# JWT Generator

Simple Python (3.6+) script that:

1. Prompts the user to enter the required third-party credentials for a given
integration, encodes them into a `JWT` and signs it with a randomly generated
`SECRET_KEY`.

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
to get more insight into how such files may look like.

## Example Output

```
python3 jwt_generator.py dev
Enter: Gigamon ThreatINSIGHT API Key: kfy0d9D-MpTDTdoeaPVKFA
The JWT for the Gigamon ThreatINSIGHT module is:
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZnkwZDlELU1wVERUZG9lYVBWS0ZBIn0.QWE9wwC2U_6UeJaav2kUXPFTF3aljGL-T0oMaZfMT5k
The SECRET_KEY to validate the JWT is:
    2qNjghi9O6TFndbifgqwffnXpFyDybHgsQOSIZddvzt4IIRtc0mbHL27TarcK67c
Use this URL to navigate to the AWS Console and configure the SECRET_KEY environment variable using the above value:
    https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/tr-gigamon-threatinsight-relay-dev/edit/environment-variables?tab=configuration
Use one of these URLs to navigate to Threat Response in your region and create the Gigamon ThreatINSIGHT module using your Lambda's URL and the JWT:
    US: https://visibility.amp.cisco.com/settings/modules/available/f4b2cf01-0447-436e-8dc1-b0b15049888b/new
    EU: https://visibility.eu.amp.cisco.com/settings/modules/available/cdf11c33-0891-491a-8e36-201e4decd3d0/new
    APJC: https://visibility.apjc.amp.cisco.com/settings/modules/available/904e961f-ff81-48f5-aeb0-5c033e2054b7/new
```
