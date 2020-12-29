OtherInc = -I ./include/ \
			-I ../other/include/ 
object = ${patsubst %.c,%.o,$(notdir $(wildcard ./src/*.c))}
all:$(object) other
$(object):%.o:src/%.c include/%.h
	$(CC) -c $(CFLAGS) $< -o $@ $(OtherInc)
other:
	mv $(object) $(MAJOR_DIR)/$(C_OBJ)