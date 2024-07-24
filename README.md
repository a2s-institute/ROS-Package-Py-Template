# ROS Package Python Template



## Getting started
```bash
pip3 install cruft
cruft create https://github.com/a2s-institute/ROS-Package-Py-Template
```

### Python interpreter location
This tool will ask the location of your Python interpreter (often for PC `/usr/bin/env python` and for Docker `/usr/bin/python3`).

Check it in advance using:
```bash
which python
```
In the case of an empty return, try with
```bash
which python3
```

## Check and update your project when the template is updated
To check if the template has been updated compared the version used for your project:
```bash
cruft check
```

To update your project based on the latest structure given by the template:
```bash
cruft update 
```

For more information visit the doc of [cruft](https://cruft.github.io/cruft/#updating-a-project)

## Contributing
Please consider to either raise an issue or contribute by sending a pull request. Thank you!
