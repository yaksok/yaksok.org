import os
import sys

import jinja2


def main():
    _, file_name = sys.argv
    base_path = os.path.abspath(os.path.dirname(__file__))
    target_path = os.path.join(base_path, 'yaksok.org')
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(base_path),
    )
    open(os.path.join(target_path, file_name), 'wb+').write(
        env.get_template(file_name).render().encode('utf-8'))


main()
