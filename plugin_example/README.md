# Solscan, Plugin Example

This repository contains an example of plugin for Solscan.

See the [detector documentation](https://github.com/khulnasoft-lab/solscan/wiki/Adding-a-new-detector).

## Architecture

- `setup.py`: Contain the plugin information
- `solscan_my_plugin/__init__.py`: Contain `make_plugin()`. The function must return the list of new detectors and printers
- `solscan_my_plugin/detectors/example.py`: Detector plugin skeleton.

Once these files are updated with your plugin, you can install it:
```bash
python setup.py develop
```

We recommend to use a Python virtual environment (for example: [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)).
