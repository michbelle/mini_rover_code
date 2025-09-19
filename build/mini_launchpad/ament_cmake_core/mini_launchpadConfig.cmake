# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_mini_launchpad_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED mini_launchpad_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(mini_launchpad_FOUND FALSE)
  elseif(NOT mini_launchpad_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(mini_launchpad_FOUND FALSE)
  endif()
  return()
endif()
set(_mini_launchpad_CONFIG_INCLUDED TRUE)

# output package information
if(NOT mini_launchpad_FIND_QUIETLY)
  message(STATUS "Found mini_launchpad: 0.0.0 (${mini_launchpad_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'mini_launchpad' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${mini_launchpad_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(mini_launchpad_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${mini_launchpad_DIR}/${_extra}")
endforeach()
