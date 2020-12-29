//校验
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//crc校验，循环冗余校验
//x4 + x + 1
unsigned short CRC4_ITU(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0;                // Initial value
    while(length--)
    {
        crc ^= *data++;                 // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0x0C;// 0x0C = (reverse 0x03)>>(8-4)
            else
                crc = (crc >> 1);
        }
    }
    return crc;
}
//x4 + x3 + 1
unsigned short CRC5_EPC(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0x48;        // Initial value: 0x48 = 0x09<<(8-5)
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for ( i = 0; i < 8; i++ )
        {
            if ( crc & 0x80 )
                crc = (crc << 1) ^ 0x48;        // 0x48 = 0x09<<(8-5)
            else
                crc <<= 1;
        }
    }
    return crc >> 3;
}
//x5 + x4 + x2 + 1
unsigned short CRC5_ITU(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0;                // Initial value
    while(length--)
    {
        crc ^= *data++;                 // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0x15;// 0x15 = (reverse 0x15)>>(8-5)
            else
                crc = (crc >> 1);
        }
    }
    return crc;
}
//x5 + x2 + 1
unsigned short CRC5_USB(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0x1F;                // Initial value
    while(length--)
    {
        crc ^= *data++;                 // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0x14;// 0x14 = (reverse 0x05)>>(8-5)
            else
                crc = (crc >> 1);
        }
    }
    return crc ^ 0x1F;
}
// x6 + x + 1 
unsigned short CRC6_ITU(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0;         // Initial value
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0x30;// 0x30 = (reverse 0x03)>>(8-6)
            else
                crc = (crc >> 1);
        }
    }
    return crc;
}
//x7 + x3 + 1
unsigned short CRC7_MMC(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0;        // Initial value
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for ( i = 0; i < 8; i++ )
        {
            if ( crc & 0x80 )
                crc = (crc << 1) ^ 0x12;        // 0x12 = 0x09<<(8-7)
            else
                crc <<= 1;
        }
    }
    return crc >> 1;
}
// x8 + x2 + x + 1 
unsigned short CRC8(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0;        // Initial value
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for ( i = 0; i < 8; i++ )
        {
            if ( crc & 0x80 )
                crc = (crc << 1) ^ 0x07;
            else
                crc <<= 1;
        }
    }
    return crc;
}
//x8 + x2 + x + 1
unsigned short CRC8_ITU(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0;        // Initial value
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for ( i = 0; i < 8; i++ )
        {
            if ( crc & 0x80 )
                crc = (crc << 1) ^ 0x07;
            else
                crc <<= 1;
        }
    }
    return crc ^ 0x55;
}
// x8 + x2 + x + 1 
unsigned short CRC8_ROHC(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0xFF;         // Initial value
    while(length--)
    {
        crc ^= *data++;            // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0xE0;        // 0xE0 = reverse 0x07
            else
                crc = (crc >> 1);
        }
    }
    return crc;
}
//x8 + x5 + x4 + 1
unsigned short CRC8_MAXIM(unsigned char *data, unsigned int length)
{
    unsigned char i;
    unsigned char crc = 0;         // Initial value
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for (i = 0; i < 8; i++)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0x8C;        // 0x8C = reverse 0x31
            else
                crc >>= 1;
        }
    }
    return crc;
}
//x16 + x15 + x2 + 1
unsigned short CRC16_IBM(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0;        // Initial value
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0xA001;        // 0xA001 = reverse 0x8005
            else
                crc = (crc >> 1);
        }
    }
    return crc;
}
//x16 + x15 + x2 + 1
unsigned short CRC16_MAXIM(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0;        // Initial value
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0xA001;        // 0xA001 = reverse 0x8005
            else
                crc = (crc >> 1);
        }
    }
    return ~crc;    // crc^0xffff
}
//x16 + x15 + x2 + 1
unsigned short CRC16_USB(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0xffff;        // Initial value
    while(length--)
    {
        crc ^= *data++;            // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0xA001;        // 0xA001 = reverse 0x8005
            else
                crc = (crc >> 1);
        }
    }
    return ~crc;    // crc^0xffff
}
#if 0	//slow modbus
//x16 + x15 + x2 + 1
unsigned short CRC16_MODBUS(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0xffff;        // Initial value
    while(length--)
    {
        crc ^= *data++;            // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0xA001;        // 0xA001 = reverse 0x8005
            else
                crc = (crc >> 1);
        }
    }
    return crc;
}
#else	//fast modbus
static const unsigned char aucCRCHi[] = {
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
    0x00, 0xC1, 0x81, 0x40
};

static const unsigned char aucCRCLo[] = {
    0x00, 0xC0, 0xC1, 0x01, 0xC3, 0x03, 0x02, 0xC2, 0xC6, 0x06, 0x07, 0xC7,
	0x05, 0xC5, 0xC4, 0x04, 0xCC, 0x0C, 0x0D, 0xCD, 0x0F, 0xCF, 0xCE, 0x0E,
    0x0A, 0xCA, 0xCB, 0x0B, 0xC9, 0x09, 0x08, 0xC8, 0xD8, 0x18, 0x19, 0xD9,
    0x1B, 0xDB, 0xDA, 0x1A, 0x1E, 0xDE, 0xDF, 0x1F, 0xDD, 0x1D, 0x1C, 0xDC,
    0x14, 0xD4, 0xD5, 0x15, 0xD7, 0x17, 0x16, 0xD6, 0xD2, 0x12, 0x13, 0xD3,
    0x11, 0xD1, 0xD0, 0x10, 0xF0, 0x30, 0x31, 0xF1, 0x33, 0xF3, 0xF2, 0x32,
    0x36, 0xF6, 0xF7, 0x37, 0xF5, 0x35, 0x34, 0xF4, 0x3C, 0xFC, 0xFD, 0x3D,
    0xFF, 0x3F, 0x3E, 0xFE, 0xFA, 0x3A, 0x3B, 0xFB, 0x39, 0xF9, 0xF8, 0x38,
    0x28, 0xE8, 0xE9, 0x29, 0xEB, 0x2B, 0x2A, 0xEA, 0xEE, 0x2E, 0x2F, 0xEF,
    0x2D, 0xED, 0xEC, 0x2C, 0xE4, 0x24, 0x25, 0xE5, 0x27, 0xE7, 0xE6, 0x26,
    0x22, 0xE2, 0xE3, 0x23, 0xE1, 0x21, 0x20, 0xE0, 0xA0, 0x60, 0x61, 0xA1,
    0x63, 0xA3, 0xA2, 0x62, 0x66, 0xA6, 0xA7, 0x67, 0xA5, 0x65, 0x64, 0xA4,
    0x6C, 0xAC, 0xAD, 0x6D, 0xAF, 0x6F, 0x6E, 0xAE, 0xAA, 0x6A, 0x6B, 0xAB,
    0x69, 0xA9, 0xA8, 0x68, 0x78, 0xB8, 0xB9, 0x79, 0xBB, 0x7B, 0x7A, 0xBA,
    0xBE, 0x7E, 0x7F, 0xBF, 0x7D, 0xBD, 0xBC, 0x7C, 0xB4, 0x74, 0x75, 0xB5,
    0x77, 0xB7, 0xB6, 0x76, 0x72, 0xB2, 0xB3, 0x73, 0xB1, 0x71, 0x70, 0xB0,
    0x50, 0x90, 0x91, 0x51, 0x93, 0x53, 0x52, 0x92, 0x96, 0x56, 0x57, 0x97,
    0x55, 0x95, 0x94, 0x54, 0x9C, 0x5C, 0x5D, 0x9D, 0x5F, 0x9F, 0x9E, 0x5E,
    0x5A, 0x9A, 0x9B, 0x5B, 0x99, 0x59, 0x58, 0x98, 0x88, 0x48, 0x49, 0x89,
    0x4B, 0x8B, 0x8A, 0x4A, 0x4E, 0x8E, 0x8F, 0x4F, 0x8D, 0x4D, 0x4C, 0x8C,
    0x44, 0x84, 0x85, 0x45, 0x87, 0x47, 0x46, 0x86, 0x82, 0x42, 0x43, 0x83,
    0x41, 0x81, 0x80, 0x40
};
unsigned short CRC16_MODBUS(unsigned char *puchMsg, unsigned int usDataLen)
{
    unsigned char ucCRCHi = 0xFF;
    unsigned char ucCRCLo = 0xFF;
    int iIndex;

    while( usDataLen-- )
    {
        iIndex = ucCRCLo ^ *( puchMsg++ );
        ucCRCLo = ( unsigned char )( ucCRCHi ^ aucCRCHi[iIndex] );
        ucCRCHi = aucCRCLo[iIndex];
    }
    return ( unsigned short )( ucCRCHi << 8 | ucCRCLo );
}
#endif
//x16 + x12 + x5 + 1
unsigned short CRC16_CCITT(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0;        // Initial value
    while(length--)
    {
        crc ^= *data++;        // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0x8408;        // 0x8408 = reverse 0x1021
            else
                crc = (crc >> 1);
        }
    }
    return crc;
}
//x16 + x12 + x5 + 1
unsigned short CRC16_CCITT_FALSE(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0xffff;        //Initial value
    while(length--)
    {
        crc ^= (unsigned short)(*data++) << 8; // crc ^= (uint6_t)(*data)<<8; data++;
        for (i = 0; i < 8; ++i)
        {
            if ( crc & 0x8000 )
                crc = (crc << 1) ^ 0x1021;
            else
                crc <<= 1;
        }
    }
    return crc;
}
//x16 + x12 + x5 + 1
unsigned short CRC16_X25(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0xffff;        // Initial value
    while(length--)
    {
        crc ^= *data++;            // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0x8408;        // 0x8408 = reverse 0x1021
            else
                crc = (crc >> 1);
        }
    }
    return ~crc;                // crc^Xorout
}
//x16 + x12 + x5 + 1
unsigned short CRC16_XMODEM(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0;            // Initial value
    while(length--)
    {
        crc ^= (unsigned short)(*data++) << 8; // crc ^= (uint16_t)(*data)<<8; data++;
        for (i = 0; i < 8; ++i)
        {
            if ( crc & 0x8000 )
                crc = (crc << 1) ^ 0x1021;
            else
                crc <<= 1;
        }
    }
    return crc;
}
//x16 + x13 + x12 + x11 + x10 + x8 + x6 + x5 + x2 + 1
unsigned short CRC16_DNP(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned short crc = 0;            // Initial value
    while(length--)
    {
        crc ^= *data++;            // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0xA6BC;        // 0xA6BC = reverse 0x3D65
            else
                crc = (crc >> 1);
        }
    }
    return ~crc;                // crc^Xorout
}
// x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1 
//fcs帧的校验和计算函数，其中整个数据的最后四个字节是fcs帧，前面的都是crc32要计算的，结果和最后四个字节比较，相同则表示帧无误
#if 0	//slow crc32
unsigned int CRC32(unsigned  char *data, unsigned int length)
{
    unsigned  char i;
    unsigned int crc = 0xffffffff;        // Initial value
    while(length--)
    {
        crc ^= *data++;                // crc ^= *data; data++;
        for (i = 0; i < 8; ++i)
        {
            if (crc & 1)
                crc = (crc >> 1) ^ 0xEDB88320;// 0xEDB88320= reverse 0x04C11DB7
            else
                crc = (crc >> 1);
        }
    }
    return ~crc;
}
#else	//fast crc32
unsigned long long  Reflect(unsigned long long  ref, unsigned char ch)
{
	int i;
	unsigned long long  value = 0;
	for (i = 1; i < (ch + 1); i++)
	{
		if (ref & 1)
			value |= 1 << (ch - i);
		ref >>= 1;
	}
	return value;
}
void gen_normal_table(unsigned int *table)
{
	unsigned int gx = 0x04c11db7;
	unsigned int temp, crc;
	for (int i = 0; i <= 0xFF; i++)
	{
		temp = Reflect(i, 8);
		table[i] = temp << 24;
		for (int j = 0; j < 8; j++)
		{
			unsigned long int t1, t2;
			unsigned long int flag = table[i] & 0x80000000;
			t1 = (table[i] << 1);
			if (flag == 0)
				t2 = 0;
			else
				t2 = gx;
			table[i] = t1^t2;
		}
		crc = table[i];
		table[i] = Reflect(table[i], 32);
	}
}

unsigned int CRC32(unsigned char *data, unsigned int len)
{
	unsigned int crc = 0xffffffff;
	unsigned char *p = data;
	unsigned int table[256];
	int i,sum = 256;
	gen_normal_table(table);
	for (i = 0; i <len; i++)
		crc = table[(crc ^ (*(p + i))) & 0xff] ^ (crc >> 8);
	return  ~crc;
}

#endif
//x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1
unsigned int CRC32_MPEG_2(unsigned    char *data, unsigned int length)
{
    unsigned  char i;
    unsigned int crc = 0xffffffff;  // Initial value
    while(length--)
    {
        crc ^= (unsigned int)(*data++) << 24;// crc ^=(uint32_t)(*data)<<24; data++;
        for (i = 0; i < 8; ++i)
        {
            if ( crc & 0x80000000 )
                crc = (crc << 1) ^ 0x04C11DB7;
            else
                crc <<= 1;
        }
    }
    return crc;
}
//BCC校验，异或校验
#define bcc_max 4*1024
unsigned int BCC_XOR(unsigned char *data,unsigned int data_len)
{
	unsigned int bcc = 0x00;
	unsigned char bcc_data[bcc_max];
	int i = 0;
	memset(bcc_data,0,bcc_max);
	memcpy(bcc_data,data,data_len);
	while(data_len--)
	{
		bcc ^= bcc_data[i];
		i++;
	}
	return bcc;
}


//十进制转换成十六进制
void DecToHex(unsigned short value, unsigned char buffer[])
{
    unsigned short i=(sizeof(unsigned short)*2);
    unsigned short temp;
   	int j=0;
	unsigned char zreo_prev=1;//true;
    while(i--)
    {
        temp = (value&(0xf<<(4*i)))>>(4*i);
		if((temp == 0 )&&(zreo_prev == 1/*true*/))//去除前面的0，如“001780”，这里将剔除变成“1780”
			continue;
		else 
			zreo_prev = 0;
        if(temp>9)
            buffer[j] = 'A'+temp-10;
      	else
         	buffer[j] = '0'+temp;
      	j++;
    }
}

int getIndexOfSigns(unsigned char ch)
{
    if(ch >= '0' && ch <= '9')
    {
        return ch - '0';
    }
    if(ch >= 'A' && ch <='F') 
    {
        return ch - 'A' + 10;
    }
    if(ch >= 'a' && ch <= 'f')
    {
        return ch - 'a' + 10;
    }
    return -1;
}
//十六进制转换成十进制
unsigned int HexToDec(unsigned char buffer[])
{

	unsigned int sum = 0;
    unsigned int t = 1;
    int i, len;
 printf("%s",buffer);
    len = strlen(buffer);
    for(i=len-1; i>=0; i--)
    {
        sum += t * getIndexOfSigns(*(buffer + i));
        t *= 16;
		printf("sum is %d,t is %d",sum,t);
    }  
 	return sum;
}
void HexToUtf8(unsigned char* src,char* dst,int len)
{
	char hex[19];
	unsigned char b[9];
	memcpy((void *)b,(void *)src,9);
	for (int i=0;i<9;i++) 
		sprintf((char *)hex+i*2,"%02X",(unsigned char)src[i]);
	dst=&hex;
	printf("hex to utf-8: %x\n",hex);//输出的就是utf-8的hex格式。
}
/*
//未知校准（HJ/T212-2017的循环冗余校验算法）
unsigned int Crc16_Checkout(unsigned char *puchMsg,unsigned int usDataLen)
{
	unsigned short i,j,crc_reg,check;
	crc_reg=0xffff;
	for(i=0;i<usDataLen;i++)
	{
		crc_reg=(crc_reg>>8)^puchMsg[i];
		for(j=0;j<8;j++)
		{
			check=crc_reg&0x0001;
			crc_reg>>=1;
			if(check==0x0001)
				crc_reg^=0xa001;
		}
	}
	return crc_reg;
}

int main()
{
	unsigned char data[4*1024];
	while(scanf("%s",data))
	{
		//unsigned short data_del;
		unsigned int data_del[21];
		unsigned int data_len = 0;
		data_len = strlen(data);
		data_del[0] = Crc16_Checkout(&data[0],data_len);
		for(int i=0;i<1;i++)
			printf("%x,%d\n",data_del[i],i);
	}
	return 0;
}

*/
