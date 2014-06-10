from jinja2 import Environment, PackageLoader


def test_hello():
    env = Environment(loader=PackageLoader('test_jinja', 'templates'))
    template = env.get_template('mytemplate.html')
    print template.render(the='variables', go='here')


def test_module():
    env = Environment(loader=PackageLoader('test_jinja', 'templates'))
    template = env.get_template('module.html')
    m = template.module
    if m.info['pk_field']:
        print m.info['pk_field']

    if m.info['query']:
        for query in m.info['query']:
            print query

    print '========================'
    print template.render(data=m.info)
    print '========================'


def main():
    #test_hello()
    test_module()



if __name__ == '__main__':
    main()
