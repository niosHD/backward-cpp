from conans import ConanFile, CMake
import os

class BackwardCpp(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    name = 'backward'
    url = 'https://github.com/bombela/backward-cpp'
    license = 'MIT'
    version = '1.4'
    no_copy_source = True
    scm = {
        "type": "git",
        "url": "https://github.com/niosHD/backward-cpp.git",
        "revision": "auto"
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_id(self):
        self.info.header_only()
