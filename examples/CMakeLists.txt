# PagedGeometry includes
include_directories(${CMAKE_SOURCE_DIR}/include)

macro(example_app NAME)
	add_executable(${NAME} WIN32 ${NAME}.cpp)
  # --- Ogre 3D graphics engine ---
  if(DEFINED CONAN_OGRE_ROOT)
    include_directories(${CONAN_INCLUDE_DIRS_OGRE}/OGRE)
    include_directories(${CONAN_INCLUDE_DIRS_OGRE}/OGRE/Bites)
    include_directories(${CONAN_INCLUDE_DIRS_OGRE}/OGRE/Terrain)
    include_directories(${CONAN_INCLUDE_DIRS_OGRE}/OGRE/Paging)
    include_directories(${CONAN_INCLUDE_DIRS_OGRE}/OGRE/RTShaderSystem)
    target_link_libraries(${NAME} PRIVATE CONAN_PKG::OGRE PagedGeometry)
  else()
    target_link_libraries(${NAME} PRIVATE OgreMain OgreBites OgreOverlay OgreTerrain PagedGeometry)
  endif()
endmacro(example_app)

if(OFF)
# these are still using the TerrainSceneManager from Ogre 1.7
# need porting for Ogre 1.8+
example_app(Example1)
example_app(Example2)
example_app(Example3)
example_app(Example4)
example_app(Example5)
example_app(Example6)
example_app(Example7)
example_app(Example8)
example_app(Example9)
example_app(Example10)
endif()

example_app(Example11)


# Copy resources needed for execution to the build directory
add_custom_command(
  TARGET Example11 POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_SOURCE_DIR}/resources ${RUNTIME_OUTPUT_DIRECTORY}/
  COMMENT "Copy resources to build directory"
  VERBATIM
)