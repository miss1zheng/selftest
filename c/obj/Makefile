LFLAG=-L../bin -ldynamic_dll -L./ -lstatic_lib #-L../bin -lws2_32
object = $(notdir $(wildcard *.o))
all:MAIN other 
MAIN:$(object)
	$(CC) -o myself $(object) $(LFLAG)
other:
	mv ./myself $(MAJOR_DIR)/ #$(BIN_DIR)/

