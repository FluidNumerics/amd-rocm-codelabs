
CC=gcc
OPT=-O0 -g -pg
LIB=-lm
INC=

.PHONY: clean


example: main.o smoother.o
	${CC} ${OPT} *.o ${LIB} ${INC} -o $@

main.o : main.c smoother.o
	${CC} ${OPT} -c main.c ${LIB} ${INC} -o $@

smoother.o : smoother.c
	${CC} ${OPT} -c smoother.c ${LIB} ${INC} -o $@

clean :
	rm *.o
