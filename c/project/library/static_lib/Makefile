libInc = -I ./include/ -I ../../main/include/ \
			-I ../../other/include/ 
#CFLAGS  := -g -Wall -O3
#CXXFLAGS:= $(CFLAGS) -DHAVE_CONFIG_H
#SHARE   := -fPIC -shared -o
object = ${patsubst %.c,%.o,$(notdir $(wildcard ./src/*.c))}
#all:test.dll other
#test.dll:$(object)#若run.dll改成run则生成的是.exe可执行文件了
#	$(CC) $(CXXFLAGS) $(SHARE) $@ $(object)
all:$(object) #加载全部的obj文件，下面生成lib
	ar cru static_lib.lib $(object)
	ranlib static_lib.lib
	mv ./static_lib.lib $(MAJOR_DIR)/$(C_OBJ)
	rm ./$(object)

$(object):%.o:src/%.c include/%.h
	$(CC) -c $(CFLAGS) $< -o $@ $(libInc)


