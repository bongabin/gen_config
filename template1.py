from jinja2 import Environment, PackageLoader
from jinja2 import Template


def hello_template():
    template = Template('Hello {{ name }}!')
    hello = template.render(name='Mark Jone')

    print hello


def basic_template():
    env = Environment(loader=PackageLoader('template1', 'templates'))
    template = env.get_template('mytemplate.html')
    print template.render(the='variables', go='here')


def main():
    env = Environment(loader=PackageLoader('template1', 'templates'))
    template = env.get_template('example.tmpl')
    print template
    #for func in template.blocks:




if __name__ == '__main__':
    main()
