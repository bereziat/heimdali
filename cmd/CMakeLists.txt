include_directories(${HEIMDALI_INCLUDE})
include_directories(${ITKINRIMAGEIO_INCLUDE})
include_directories(${H5UNIXPIPE_INCLUDE})

set(CMD_LIST hconv
             par tpr ical itest
             so ad di mu bi min max
             sc sd lo ra car exp
             extg raz cco melg fzoom izoom
             sba sha vb vh mb mh muls norma
             mo carflo fixflo flofix logic
             cim asm rot
             detc
             med rdf ddf idf ri ma conv fmoy ce
             )
foreach(cmd ${CMD_LIST})
  ADD_EXECUTABLE(${cmd} ${cmd}.cxx)
  TARGET_LINK_LIBRARIES(${cmd}
    ${HEIMDALI_LIBRARY}
    ${ITKINRIMAGEIO_LIBRARY}
    ${ITK_LIBRARIES}
    ${H5UNIXPIPE_LIBRARIES}
    ${HDF5_LIBRARIES}
    ${MINIMAL_TRACEBACK_LIBRARIES}
    )
endforeach(cmd)

install (TARGETS ${CMD_LIST} DESTINATION bin)
