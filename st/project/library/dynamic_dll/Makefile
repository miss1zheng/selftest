libInc = -I ./include/ -I ../../main/include/ \
			-I ../../other/include/ 
CFLAGS  := -g -Wall -O3
CXXFLAGS:= $(CFLAGS) -DHAVE_CONFIG_H
SHARE   := -fPIC -shared -o
object = ${patsubst %.c,%.o,$(notdir $(wildcard ./src/*.c))}
all:dynamic_dll.dll other
dynamic_dll.dll:$(object)#若run.dll改成run则生成的是.exe可执行文件了
	$(CC) $(CXXFLAGS) $(SHARE) $@ $(object)
#all:$(object) other#加载全部的obj文件，下面生成lib
#	ar cru test.lib $(object)
#	ranlib test.lib
$(object):%.o:src/%.c include/%.h
	$(CC) -c $(CFLAGS) $< -o $@ $(libInc)
other:
	mv ./dynamic_dll.dll $(MAJOR_DIR)/$(BIN_DIR)
	rm ./$(object)
