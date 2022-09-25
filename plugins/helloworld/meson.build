qt5_dep = dependency('qt5', modules: ['Core', 'Widgets'])
moc_files = qt5.compile_moc(headers : 'helloworld.h',
                            include_directories: api,
                            dependencies: qt5_dep)
helloworld_plugin = static_library('helloworld', ['helloworld.cpp', moc_files], include_directories: [api], dependencies: [qt5_dep])
