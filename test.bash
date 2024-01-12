#!/bin/bash -xv
# SPDX=FileCopyrightText: 2024 Shunsuke Otani
# SPDX-Licecse-Identifier: BSD-3-Clause

ng (){
		echo NG at line $1
			res=1
		}

	res=0

	### I/O TEST ###
	out=$(./kakuritu.py)
	[ "${out}" = "5" ] 
	[ "15" ] 
	[ "13" ] || ng ${LINENO}

	[ "$res" = 0 ] && echo OK
	exit $res
