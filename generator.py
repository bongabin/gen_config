from jinja2 import Environment, PackageLoader
import ConfigParser

import setting



def generate_config(env, template_name):
    """Generate Configuration Files"""
    print 'generate_config()'

    template = env.get_template(template_name)
    content = template.render(the='angel', go='eating')

    print 'content:', content


def init_config():
    config_parser = ConfigParser.ConfigParser()
    config_file = open(setting.CONFIG_FILE, 'r')
    config_parser.readfp(config_file)
    req_config_names = set(['cdb_id', 'cdb_pw'])

    found_names, config_dict = set(), {}
    for name, value in config_parser.items('config'):
        found_names.add(name)
        config_dict[name] = value
    diff = req_config_names.difference(found_names)
    if diff:
        raise Exception('Error: Config file missing critical values:%s' % ','.join([item for item in diff]))

    return config_dict


def main():
    print 'main()'


    # Read config
    print 'config path:', setting.CONFIG_FILE
    config_dict = init_config()

    # Initialize Template
    env = Environment(loader=PackageLoader('generator', setting.TEMPLATE_PATH))

    # Read Option

    # Generate Configuration files
    generate_config(env, 'mytemplate.html')






if __name__ == '__main__':
    main()

