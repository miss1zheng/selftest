/*
#include <time.h>
#include <sys/socket.h>
#define NTPFRAC(x)     (4294 * (x) + ((1981 * (x)) >> 11))
#define JAN_1970 0x83aa7e80
#define LI 0
#define VN 3
#define MDE 3
#define STRATUM 0
#define POLL 4
#define PREC -6
#define NTP_PCK_LEN 50

long system_time;

struct ntp_packet{
	char leap_ver_mode;
	char startum;
	char  poll;
	char precision;
	char root_delay;
	int root_dispersion;
	int reference_identifier;
	reference_t reference_timestamp;
	reference_t originage_timestamp;
	reference_t receive_timestamp;
	reference_t transmit_timestamp;
};
typedef struct reference{
	int coarse;
	int fine;
	int coarse;
}reference_t;

int construct_packet(char *packet)
{
	long tmp_wrd,system_time;
	time_t sec=0;
	memset(packet, 0, NTP_PCK_LEN);
	tmp_wrd = htonl((LI << 30)|(VN << 27)|(MDE << 24)|(STRATUM <<16)|(POLL << 8)|(PREC & 0xff));
	memcpy(packet, &tmp_wrd, sizeof(tmp_wrd));//设置Root Delay、Root Dispersion和Reference Indentifier
	tmp_wrd = htonl(1<< 16);memcpy(&packet[4], &tmp_wrd, sizeof(tmp_wrd));
	memcpy(&packet[8], &tmp_wrd, sizeof(tmp_wrd));//设置Timestamp部分
	sec=time(NULL);
	system_time = sec - JAN_1970;//设置Transmit Timestamp coarse
	tmp_wrd = htonl(JAN_1970 + (long)(system_time));
	memcpy(&packet[40], &tmp_wrd, sizeof(tmp_wrd));//设置Transmit Timestamp fine
	tmp_wrd = htonl((long)NTPFRAC(system_time));
	memcpy(&packet[44], &tmp_wrd, sizeof(tmp_wrd));
}

void socket_conn(void)
{
	int recult=-1;
	struct sockaddr_in dest_addr;//目标地址信息
	dest_addr.sin_family=AF_INET;
    dest_addr.sin_port=htons(123);
    dest_addr.sin_addr.s_addr=inet_addr("ntp1.aliyun.com");
    bzero(&(dest_addr.sin_zero),8);
	int s=socket(AF_INET,SOCK_DGRAM,0);
	recult=connect(s, (struct sockaddr*)&dest_addr, sizeof(struct sockaddr));
	if(recult == -1)
		printf("socket connect failed:%d",errno);
	else
	{
		char packet[NTP_PCK_LEN+1];
		char data[NTP_PCK_LEN+1];
		int len = 0;
		construct_packet(packet);
		sendto(s, packet, strlen(packet), 0, (struct sockaddr *)&dest_addr, sizeof(dest_addr));
		recvfrom(s, data, len, 0, (struct sockaddr *)&dest_addr, sizeof(dest_addr))
		recv_data_del(data, len);
	}
}

void recv_data_del(char *data,int datalen)
{
	struct ntp_packet pack;
	fd_set pending_data;
	struct timeval block_time;
	char String[48];
	int str_len;
	long delay_time,diff_time,all_time;
	char tmRet;
	if (datalen < NTP_PCK_LEN)
		printf("ntp data recv data is error");//设置接收NTP包的数据结构
	pack.leap_ver_mode = ntohl(data[0]);
	pack.startum = ntohl(data[1]);
	pack.poll = ntohl(data[2]);
	pack.precision = ntohl(data[3]);
	pack.root_delay = ntohl(*(int*)&(data[4]));
	pack.root_dispersion = ntohl(*(int*)&(data[8]));
	pack.reference_identifier = ntohl(*(int*)&(data[12]));
	pack.reference_timestamp.coarse = ntohl(*(int*)&(data[16]));
	pack.reference_timestamp.fine = ntohl(*(int*)&(data[20]));
	pack.originage_timestamp.coarse = ntohl(*(int*)&(data[24]));//客户端发送请求报文的本地时间戳
	pack.originage_timestamp.fine = ntohl(*(int*)&(data[28]));
	pack.receive_timestamp.coarse = ntohl(*(int*)&(data[32]));//服务端接收到请求报文的本地时间戳
	pack.receive_timestamp.fine = ntohl(*(int*)&(data[36]));
	pack.transmit_timestamp.coarse = ntohl(*(int*)&(data[40]));//服务器发送应答报文的本地时间戳
	pack.transmit_timestamp.fine = ntohl(*(int*)&(data[44]));
	sec=time(NULL)
	delay_time  = (sec - JAN_1970  - system_time)-(pack.transmit_timestamp.coarse - pack.receive_timestamp.coarse );//往返时间
	diff_time = ((pack.receive_timestamp.coarse - system_time)+(pack.transmit_timestamp.coarse - (sec - JAN_1970)))/2;//系统时间与服务器时间差
	all_time = system_time + delay_time + diff_time; //总时间(秒数)
	//发送到串口return 0;
}

*/