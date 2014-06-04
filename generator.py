from cement.core import foundation


def main():
    app = foundation.CementApp('generator')
    try:
        app.setup()
        app.run()
        print('Hello World')
    finally:
        app.close()

if __name__ == '__main__':
    main()
