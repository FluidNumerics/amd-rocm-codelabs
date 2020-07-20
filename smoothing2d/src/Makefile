
#CC=gcc
CC=hipcc
OPT=-O0 -g
# -DGPU
LIB=-lm
INC=

.PHONY: clean

smoother2d: main.o smoother.o
	${CC} ${OPT} *.o ${LIB} ${INC} -o $@

main.o : main.c smoother.o
	${CC} ${OPT} -c main.c ${LIB} ${INC} -o $@

smoother.o : smoother.c
	${CC} ${OPT} -c smoother.c ${LIB} ${INC} -o $@

clean :
	rm *.o smoother2d
