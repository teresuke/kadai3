#!/bin/bash -xv
# SPDX=FileCopyrightText: 2023 Shunsuke Otani
# SPDX-Licecse-Identifier: BSD-3-Clause

ng (){
		echo NG at line $1
			res=1
		}

	res=0

	### I/O TEST ###
	#out=$(seq 5 | ./plus_stdin)

	out=$(seq 5 | ./plus)
	[ "${out}" = "3 12.0 60.0" ] 
	[ "4 9.0 20.0" ] || ng ${LINENO}

	[ "$res" = 0 ] && echo OK
	exit $res
