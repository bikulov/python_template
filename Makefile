all:
	cp python_boilerplate.py python_boilerplate.pyx
	cython *.pyx --embed
	gcc -Os -I /usr/include/python3.5m -o python_boilerplate python_boilerplate.c -lpython3.5m -lpthread -lm -lutil -ldl
	rm python_boilerplate.pyx python_boilerplate.c