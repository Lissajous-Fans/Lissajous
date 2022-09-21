project(
    'Lissajous',
    'c', 'cpp',
    version: '0.0.1a',
    license: 'MIT',
    default_options: [
        'cpp_std=c++20',
        'c_std=c11'
    ]
)

qt5 = import('qt5')
qt5_dep = dependency('qt5', modules: ['Core', 'Gui', 'Widgets', 'Charts'])
resources = qt5.compile_resources(sources: 'resources.qrc')
subdir('src/')
