libInc = -I ./include/ -I ../main/include/ \
			-I ../other/include/ 
#CFLAGS  := -g -Wall -O3
#CXXFLAGS:= $(CFLAGS) -DHAVE_CONFIG_H
#SHARE   := -fPIC -shared -o
object = ${patsubst %.c,%.o,$(notdir $(wildcard ./src/*.c))}
subfile = dynamic_dll static_lib
all:$(object) $(subfile)
#test.dll:$(object)#若run.dll改成run则生成的是.exe可执行文件了
#	$(CC) $(CXXFLAGS) $(SHARE) $@ $(object)
#all:$(object) other#加载全部的obj文件，下面生成lib
#	ar cru test.lib $(object)
#	ranlib test.lib
$(object):%.o:src/%.c include/%.h
	$(CC) -c $(CFLAGS) $< -o $@ $(libInc)
#other:$(subfile)
#	mv ./$(object) $(MAJOR_DIR)/$(BIN_DIR)

$(subfile):Echo
	make -C $@
Echo:
	@echo $(SUBDIRS)
	@echo begin compile