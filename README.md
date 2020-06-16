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

## Example Output

```
python3 jwt_generator.py dev
Enter: Gigamon ThreatINSIGHT API KEY: kfy0d9D-MpTDTdoeaPVKFA
The JWT for the Gigamon ThreatINSIGHT module is:
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZnkwZDlELU1wVERUZG9lYVBWS0ZBIn0.QWE9wwC2U_6UeJaav2kUXPFTF3aljGL-T0oMaZfMT5k
The SECRET_KEY to validate the JWT is:
    2qNjghi9O6TFndbifgqwffnXpFyDybHgsQOSIZddvzt4IIRtc0mbHL27TarcK67c
Use this URL to navigate to the AWS Console and configure the SECRET_KEY environment variable using the above value:
    https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions/tr-gigamon-threatinsight-relay-dev/edit/environment-variables?tab=configuration
Use one of these URLs to navigate to Threat Response in your region and create the Gigamon ThreatINSIGHT module using your Lambda's URL and the JWT:
    US: https://visibility.amp.cisco.com/settings/modules/available/3113dda1-1018-4586-a8bf-f5363e1b3aed/new
    EU: N/A
    APJC: N/A
```
