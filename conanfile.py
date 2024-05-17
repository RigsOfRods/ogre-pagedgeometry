import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps
from conan.tools.files import copy

class pagedgeometry(ConanFile):
    name = "ogre-pagedgeometry"
    settings = "os", "compiler", "build_type", "arch"

    def layout(self):
        self.folders.generators = os.path.join(self.folders.build, "generators")

    def requirements(self):
        self.requires("ogre3d/1.11.6.1@anotherfoxguy/stable")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()