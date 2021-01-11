#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "crc.h"
#include "main.h"
/*
#define PARSE_ERROR 0
uint8_t UTF8ToUnicode(uint8_t *utf8, uint32_t *unicode) {
    const uint8_t lut_size = 3;
    const uint8_t length_lut[] = {2, 3, 4};
    const uint8_t range_lut[] = {0xE0, 0xF0, 0xF8};
    const uint8_t mask_lut[] = {0x1F, 0x0F, 0x07};

    uint8_t length = 0;
    uint8_t b = *(utf8 + 0);
    uint32_t i = 0;

    if(utf8 == NULL) {
        *unicode = 0;
        return PARSE_ERROR;
    }
    // utf8编码兼容ASCII编码,使用0xxxxxx 表示00~7F
    if(b < 0x80) {
        *unicode =  b;
        return 1;
    }
    // utf8不兼容ISO8859-1 ASCII拓展字符集
    // 同时最大支持编码6个字节即1111110X
    if(b < 0xC0 || b > 0xFD) {
        *unicode = 0;
        return PARSE_ERROR;
    }
    for(i = 0; i < lut_size; i++) {
        if(b < range_lut[i]) {
            *unicode = b & mask_lut[i];
            length = length_lut[i];
            break;
        }
    }
    // 超过四字节的utf8编码不进行解析
    if(length == 0) {
        *unicode = 0;
        return PARSE_ERROR;
    }
    // 取后续字节数据
    for(i = 1; i < length; i++ ) {
        b = *(utf8 + i);
        // 多字节utf8编码后续字节范围10xxxxxx‬~‭10111111‬
        if( b < 0x80 || b > 0xBF ) {
            break;
        }
        *unicode <<= 6;
        // ‭00111111‬
        *unicode |= (b & 0x3F);
    }
    // 长度校验
    return (i < length) ? PARSE_ERROR : length;
}
uint8_t UnicodeToUTF16(uint32_t unicode, uint16_t *utf16) {
    // Unicode范围 U+000~U+FFFF
    // utf16编码方式：2 Byte存储，编码后等于Unicode值
    if(unicode <= 0xFFFF) {
		if(utf16 != NULL) {
			*utf16 = (unicode & 0xFFFF);
		}
		return 1;
	}else if( unicode <= 0xEFFFF ) {
		if( utf16 != NULL ) {
		    // 高10位
		    *(utf16 + 0) = 0xD800 + (unicode >> 10) - 0x40;
            // 低10位
		    *(utf16 + 1) = 0xDC00 + (unicode &0x03FF);
		}
		return 2;
	}

    return 0;
}

int main() {
    // 严 utf8 E4 B8 A5
    uint32_t buffer;
    uint8_t utf8[] = "严";
    uint16_t utf16[2] = {0};

    uint8_t len = UTF8ToUnicode(utf8, &buffer);

    printf("len:%d\n", len);
    printf("buffer:%x\n", buffer);

    len = UnicodeToUTF16(buffer, utf16);

    printf("len:%d\n", len);
    printf("utf16[0]:%x\n", utf16[0]);
    printf("utf16[0]:%x\n", utf16[1]);
	printf("utf16=%s",utf16);
	system("pause");
	return 0;

}*//*
#define paster( n , b) printf( "token " #n "and" #b " = %d\n ", token##n > token##b ? token##n :token##b )
#define MAX_LEN 100
typedef struct{
	int bianhao;
	uint8_t schoolname[MAX_LEN];
	student stu_param;
}school;
typedef struct {
	int banji;
	int nianji;
	uint8_t name[MAX_LEN];
	uint8_t password[MAX_LEN];
	uint8_t username[MAX_LEN];
	family family_param;
}student;
typedef struct mather_or_father_param{
	uint8_t name[MAX_LEN];
	uint8_t diag[MAX_LEN];
}mafather;
typedef struct{
	uint8_t addr[MAX_LEN];
	mafather ma_param;
	mafather fa_param;
}family;
typedef struct EDU{
	uint8_t start;
	uint8_t area_name[MAX_LEN];
	int paiming;
	school school_Param;
	uint8_t end;
}edu;
edu edu_run;
edu edu_save;
void write_sed_run(edu *edu_tmp)
{
	if((edu_tmp.start != 0x01)||(edu_tmp.end != 0x01))
	{
		memcpy(edu_tmp.area_name,"baidu.edu",strlen("baidu.edu"));
		edu_tmp.paiming=1;
		edu_tmp.school_Param.bianhao=0;
		memcpy(edu_tmp.school_Param.schoolname,"baidu",strlen("baidu"));
		edu_tmp.school_Param.stu_param.banji=11;
		edu_tmp.school_Param.stu_param.nianji=3;
		memcmp(edu_tmp.school_Param.stu_param.name,"ahua",strlen("ahua"));
		memcpy(edu_tmp.school_Param.stu_param.password,"0000",strlne("0000"));
		memcpy(edu_tmp.school_Param.stu_param.username,"admin",strlen("admin"));
		memcpy(edu_tmp.school_Param.stu_param.family_param.addr,"beijing",strlen("beijing"));
		memcmp(edu_tmp.school_Param.stu_param.family_param.fa_param.name,"fa",strlen("fa"));
		memcmp(edu_tmp.school_Param.stu_param.family_param.fa_param.diag,"135",strlen("135"));
		memcpy(edu_tmp.school_Param.stu_param.family_param.ma_param.name,"153",strlen("153"));
		return 0;
	}
	else{
		return -1;
	}
}
hhh(char *da)
{
	return *da;
}*/

#include <time.h>
int main()
{
	int year,month,day,all_day;
	char run =0;
	printf("please input your birth year:");
	scanf("%d",&year);
	printf("month:");
	scanf("%d",&month);
	printf("day:");
	scanf("%d",&day);
	for(int i=year+1;i<2021;i++)
	{
		if((i%100!=0)&&(i%4==0)||(i%400==0))
		{
			run=1;
			all_day+=1;
		}
		all_day +=365;
	}
	for(int i=month+1;month<=12;i++)
	{
		if(month == 1)&&(month == 3)&&(month == 5)&&(month == 7)&&(month == 8)&&(month == 10)&&(month == 12)
			all_day+=31;
		else if(month ==2)&&(run==1)
			all_day+=29;
		else if(month ==2)
			all_day+=28;
		else
			all_day+30;
	}
	printf("your age is %d,and your all day is %d",2021-year,all_day);
	system("pause");
	return 0;
}

