MainInc = -I ./include/ -I ../other/include/ -I ../library/include/ \
			-I ../library/dynamic_dll/include/ -I ../library/static_lib/include/
object = ${patsubst %.c,%.o,$(notdir $(wildcard ./src/*.c))}
all:$(object) other
$(object):%.o:src/%.c include/%.h
	$(CC) -c $(CFLAGS) $< -o $@ $(MainInc)
other:
	mv $(object) $(MAJOR_DIR)/$(C_OBJ)