#!/bin/bash
IFS=$','
#lista dos diretorios -origem- itens separados por virgulas (preferencialmente caminho absoluto)
dirlist='/home/treelinux/feaw'
for i in $dirlist; do
    #Move o conteudo para a pasta /target
    mv "$i"/*.txt /target
    #apaga a origem (vazio!)
    rmdir "$i"
done
unset IFS
