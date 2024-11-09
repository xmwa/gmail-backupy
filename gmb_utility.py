
import platform, tomllib

def get_python_version():
    return platform.python_version_tuple()

def gmb_config():
    with open("gmb_config.toml", "rb") as f:
        return tomllib.load(f)

