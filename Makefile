all:
	cp python_template.py python_template.pyx
	cython *.pyx --embed
	gcc -Os -I /usr/include/python3.5m -o python_template python_template.c -lpython3.5m -lpthread -lm -lutil -ldl
	rm python_template.pyx python_template.c

test:
	py.test test_python_template.py