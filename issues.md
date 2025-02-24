
[ERROR]
(.venv) (base) juandomingo@hp-elitebook-840-G5:~/factoriaf5/mod01-labs/django-books-04-v2/books_manager
$ uv add mysqlclient
Resolved 7 packages in 81ms
  × Failed to build `mysqlclient==2.2.7`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta.build_wheel` failed (exit status: 1)

      [stdout]
      Trying pkg-config --exists mysqlclient
      # Options for building extension module:
        extra_compile_args: ['-I/usr/include/mysql', '-std=c99']
        extra_link_args: ['-lmysqlclient']
        define_macros: [('version_info', (2, 2, 7, 'final', 0)), ('__version__', '2.2.7')]
      running bdist_wheel
      running build
      running build_py
      copying src/MySQLdb/cursors.py -> build/lib.linux-x86_64-cpython-313/MySQLdb
      copying src/MySQLdb/connections.py -> build/lib.linux-x86_64-cpython-313/MySQLdb
      copying src/MySQLdb/_exceptions.py -> build/lib.linux-x86_64-cpython-313/MySQLdb
      copying src/MySQLdb/times.py -> build/lib.linux-x86_64-cpython-313/MySQLdb
      copying src/MySQLdb/release.py -> build/lib.linux-x86_64-cpython-313/MySQLdb
      copying src/MySQLdb/__init__.py -> build/lib.linux-x86_64-cpython-313/MySQLdb
      copying src/MySQLdb/converters.py -> build/lib.linux-x86_64-cpython-313/MySQLdb
      copying src/MySQLdb/constants/FIELD_TYPE.py -> build/lib.linux-x86_64-cpython-313/MySQLdb/constants
      copying src/MySQLdb/constants/CLIENT.py -> build/lib.linux-x86_64-cpython-313/MySQLdb/constants
      copying src/MySQLdb/constants/CR.py -> build/lib.linux-x86_64-cpython-313/MySQLdb/constants
      copying src/MySQLdb/constants/FLAG.py -> build/lib.linux-x86_64-cpython-313/MySQLdb/constants
      copying src/MySQLdb/constants/ER.py -> build/lib.linux-x86_64-cpython-313/MySQLdb/constants
      copying src/MySQLdb/constants/__init__.py -> build/lib.linux-x86_64-cpython-313/MySQLdb/constants
      running egg_info
      writing src/mysqlclient.egg-info/PKG-INFO
      writing dependency_links to src/mysqlclient.egg-info/dependency_links.txt
      writing top-level names to src/mysqlclient.egg-info/top_level.txt
      reading manifest file 'src/mysqlclient.egg-info/SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      adding license file 'LICENSE'
      writing manifest file 'src/mysqlclient.egg-info/SOURCES.txt'
      copying src/MySQLdb/_mysql.c -> build/lib.linux-x86_64-cpython-313/MySQLdb
      running build_ext
      building 'MySQLdb._mysql' extension
      cc -pthread -fno-strict-overflow -Wsign-compare -Wunreachable-code
      -DNDEBUG -g -O3 -Wall -fPIC -fPIC "-Dversion_info=(2, 2, 7, 'final', 0)"
      -D__version__=2.2.7 -I/home/juandomingo/.cache/uv/builds-v0/.tmpRBPZbY/include
      -I/home/juandomingo/snap/code/182/.local/share/uv/python/cpython-3.13.2-linux-x86_64-gnu/include/python3.13
      -c src/MySQLdb/_mysql.c -o build/temp.linux-x86_64-cpython-313/src/MySQLdb/_mysql.o -I/usr/include/mysql
      -std=c99

      [stderr]
      error: command 'cc' failed: No such file or directory

      hint: This usually indicates a problem with the package or the build environment.
  help: `mysqlclient` (v2.2.7) was included because `django-books-04-v2` (v0.1.0) depends on `mysqlclient`
  

[SOLUTION]
sudo apt update
sudo apt install build-essential default-libmysqlclient-dev python3-dev
