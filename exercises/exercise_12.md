# Exercise 12

1. Review the following code:

```python
import logging

# Configure the logging settings
logging.basicConfig(
    filename="example.log",
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)
```

2. Add a configuration file to the Calc App application. The name of the configuration file will be `config.yml`. The configuration should allow the setting of the log level and the name of the file the logs are written to.

3. Update the Calc App application to load the new configuration file, set the logging level and output file accordingly. Right now the application logs to the console, using the code above update the application to log to a file.

## When Done

Send me an email [eric@cloudcontraptions.com](mailto:eric@cloudcontraptions.com) when you are done.
