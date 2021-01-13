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
int out_day(int in,int set_value)
{
	int out;
	if(set_value==1){//开始
		out=in;
	}
	else if(set_value==2){//结束
		out=1;
	}
	else{//全年
		out=1;
	}
	return out;
	printf("out is %d\n",out);
}
int time_one(int year,int month,int day,int set_value){
	int reseult=0;
	int run =0,end=0,all_day;
	int i,j,start_month,start_day;
	
	if(set_value==1){//开始
		i=month,j=day,start_month=12;
	}
	else if(set_value==2){//结束
		i=1,j=1,start_month=month,end=1;
	}
	else{//全年
		i=1,j=1,start_month=12;
	}
	if((year%100!=0)&&(year%4==0)||(year%400==0))
	{
		run = 1;
	}
	for(i;i<=start_month;i++)
	{
		printf("\n%i month\n",i);
		if((i==1)||(i==3)||(i==5)||(i==7)||(i==8)||(i==10)||(i==12))
		{
			if(end)
				all_day=day;
			else
				all_day=31;
			j=out_day(day,set_value);
			for(j;j<=all_day;j++)
			{
				printf("%4d",j);
				reseult++;
				if(j % 8 == 0)
				{
					printf("\n");
				}
			}
		}
		else if((i==2)&&(run))
		{
			if(end)
				all_day=day;
			else
				all_day=29;
			j=out_day(day,set_value);
			for(j;j<=29;j++)
			{
				printf("%4d",j);
				reseult++;
				if(j % 8 == 0)
				{
					printf("\n");
				}
			}
		}
		else if(i==2)
		{
			if(end)
				all_day=day;
			else
				all_day=28;
			j=out_day(day,set_value);
			for(j;j<=28;j++)
			{
				printf("%4d",j);
				reseult++;
				if(j % 8 == 0)
				{
					printf("\n");
				}
			}
		}
		else{
			if(end)
				all_day=day;
			else
				all_day=30;
			j=out_day(day,set_value);
			for(j;j<=30;j++)
			{
				printf("%4d",j);
				reseult++;
				if(j % 8 == 0)
				{
					printf("\n");
				}
			}
		}
		printf("\n");
	}
	return reseult;
}
int sum_date(int year,int month,int day)
{
	int sum_day=0;
	time_t curtime;
	struct tm *info;

	time ( &curtime );
	info = localtime(&curtime);
	int curr_year,curr_month,curr_day;
	curr_year = 1900 + info->tm_year;
	curr_month = info->tm_mon+1;
	curr_day = info->tm_mday;
    
	if(year<curr_year)
	{
		sum_day += time_one(year,month,day,1);
		sum_day += time_one(curr_year,curr_month,curr_day,2);
	}
	else if(year==curr_year)
	{
		int start=time_one(year,month,day,2);
		int end= time_one(curr_year,curr_month,curr_day,2);
		sum_day=end-start;
		printf("2021time is %d=%d-%d\n",sum_day,start,end);
	}
	else
	{
		printf("you input big.\n");
	}
	for(int i=year+1;i<=curr_year-1;i++)
	{
		sum_day += time_one(i,0,0,0);
	}

	return sum_day;
}

int main()
{
	int toes=10;
	printf("toes=%d,toes square=%d,toes twice=%d",toes,toes*toes,2*toes);
  
	system("pause");
	return 0;
}

