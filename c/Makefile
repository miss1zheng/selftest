CC=i686-w64-mingw32-gcc#i686-w64-mingw32-g++
BIN_DIR = bin
SUBDIRS = project obj
C_OBJ = obj
MAJOR_DIR = $(shell pwd)
export
all:CHECK_DIR $(SUBDIRS)
CHECK_DIR:
	mkdir -p $(BIN_DIR)
$(SUBDIRS):Echo
	make -C $@
Echo:
	@echo $(SUBDIRS)
	@echo begin compile
.PHONY:
clean:
	rm ./$(C_OBJ)/*.o