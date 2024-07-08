
include_directories(${CMAKE_SOURCE_DIR}/include)

FILE(GLOB sources *.cpp ${CMAKE_SOURCE_DIR}/include/*.h)

set(LIBNAME "PagedGeometry")
ADD_LIBRARY(${LIBNAME} STATIC ${sources})

# install the library
INSTALL(TARGETS ${LIBNAME}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION ${LIB_INSTALL_DIR}
        ARCHIVE DESTINATION ${LIB_INSTALL_DIR}
)

# install the headers: both source and build headers
INSTALL(DIRECTORY ${CMAKE_SOURCE_DIR}/include/ DESTINATION include/PagedGeometry FILES_MATCHING PATTERN "*.h")

# --- Threading support (still needed for GCC even with C++11)
set( CMAKE_THREAD_PREFER_PTHREAD YES )
find_package( Threads REQUIRED )
target_link_libraries( ${LIBNAME} PRIVATE
  Threads::Threads
)

# --- Ogre 3D graphics engine ---
if(TARGET OGRE::OGRE)
  target_link_libraries(${LIBNAME} PRIVATE OGRE::OGRE)
else()
  target_link_libraries(${LIBNAME} PRIVATE ${OGRE_LIBRARIES})
  target_include_directories(${LIBNAME} PRIVATE ${OGRE_INCLUDE_DIRS})
endif()